#!/usr/bin/env python3
"""Evidence-first single-enterprise competitive baseline without rankings."""

from __future__ import annotations
import datetime as dt
import json
from typing import Any, Dict, List, Mapping, Optional
import mcp_orchestration as orch

REPORT_TYPE = "competitive_analysis_direct"
BANNER = "企业竞争基准事实画像"
SERVERS = [
    "enterprise-mcp-server",
    "enterprise-operation-mcp-server",
    "patent-mcp-server",
    "trademark-mcp-server",
    "bidding-mcp-server",
    "news-mcp-server",
    "qualification-mcp-server",
]
PRODUCTS = [
    "企业基础信息",
    "经营公开线索",
    "专利统计",
    "商标统计",
    "招投标统计",
    "舆情统计",
    "资质证书概况",
]
DOMAINS = [
    ("enterprise", "主体与工商基础"),
    ("patent", "专利事实"),
    ("trademark", "商标事实"),
    ("bidding", "招投标公开活动"),
    ("operation", "经营公开线索"),
    ("qualification", "资质证书事实"),
    ("news", "舆情统计"),
]


def _effective(v: Any) -> bool:
    if v in (None, "", "-", [], {}):
        return False
    if isinstance(v, dict):
        return any(_effective(x) for x in v.values())
    if isinstance(v, list):
        return any(_effective(x) for x in v)
    return True


def _int(v: Any):
    try:
        return int(float(str(v).replace(",", "")))
    except (TypeError, ValueError):
        return None


def _base(data: Mapping[str, Any]) -> Dict[str, Any]:
    ent = data.get("enterprise") or {}
    return dict(ent.get("base") or data.get("base") or {})


def _identity(data: Mapping[str, Any], requested: str) -> tuple[str, bool, str]:
    meta = data.get("_meta") or {}
    resolved = meta.get("resolved") or {}
    canon = str(resolved.get("enterprise") or requested).strip()
    base = _base(data)
    name = str(base.get("企业名称") or base.get("name") or "").strip()
    code = str(
        base.get("统一社会信用代码") or base.get("socialCreditCode") or ""
    ).strip()
    confirmed = (
        name not in ("", "-")
        and (name == canon or name == requested)
        and code not in ("", "-")
    )
    reason = (
        "工商基础信息中的企业名称和统一社会信用代码已返回"
        if confirmed
        else "工商基础信息未返回可核验企业名称及统一社会信用代码"
    )
    return (name if confirmed else canon), confirmed, reason


def _section(
    sections: List[Dict[str, Any]],
    core: Dict[str, Any],
    key: str,
    title: str,
    body: Any,
) -> None:
    if _effective(body):
        sections.append({"key": key, "title": title, "kind": "kv"})
        core[key] = body


def _patent_total(p: Mapping[str, Any]):
    direct = _int(p.get("patentCount"))
    if direct is not None:
        return direct
    vals = [
        _int(p.get(k))
        for k in (
            "inventionAppPatentCount",
            "inventionLicPatentCount",
            "utilityModelPatentCount",
            "appearanceDesignPatentCount",
        )
    ]
    known = [v for v in vals if v is not None]
    return sum(known) if known else None


_FIELD_LABELS = {
    "staff": "人员规模",
    "turnover": "年营业额",
    "subjectMatter": "标的",
    "count": "数量",
    "percent": "占比",
    "area": "区域",
    "range": "金额区间",
    "year": "年份",
    "month": "月份",
    "negative": "负面",
    "neutral": "中立",
    "positive": "正面",
    "unknown": "未知",
    "inventionAppPatentCount": "发明申请",
    "inventionLicPatentCount": "发明授权",
    "utilityModelPatentCount": "实用新型",
    "appearanceDesignPatentCount": "外观设计",
    "patentDivAppLegal": "法律状态",
    "patentCount": "数量",
}


_ORGANIZED_KEYS = {
    "patent": (
        "专利总数",
        "发明申请",
        "发明授权",
        "实用新型",
        "外观设计",
        "专利申请年度趋势",
        "专利公开年度趋势",
        "专利法律状态",
    ),
    "trademark": (
        "商标总数",
        "有效商标数",
        "无效商标数",
        "本年新增",
        "商标类别",
        "商标状态",
        "状态统计",
        "申请年度趋势",
        "注册年度趋势",
        "类型统计",
    ),
    "bidding": (
        "中标标的分布",
        "中标区域分布",
        "中标金额分布",
        "中标趋势",
        "招投标明细",
        "招投标记录总量",
    ),
    "news": ("情感分布", "月度情感趋势"),
    "operation": ("人员规模", "年营业额", "融资轮次", "融资记录", "上榜记录"),
}


def _num_text(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, float):
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def _one_line(value: Any) -> str:
    """Readable text for nested upstream values; retains every item."""
    if isinstance(value, dict):
        if {"subjectMatter", "count"} <= set(value):
            pct = value.get("percent")
            pct_text = f"，占比 {_num_text(pct)}%" if pct is not None else ""
            return f"{value.get('subjectMatter')} {value.get('count')} 条{pct_text}"
        if {"area", "count"} <= set(value):
            return f"{value.get('area')} {value.get('count')} 条"
        if {"range", "count"} <= set(value):
            pct = value.get("percent")
            pct_text = f"，占比 {_num_text(pct)}%" if pct is not None else ""
            return f"{value.get('range')} {value.get('count')} 条{pct_text}"
        if {"year", "count"} <= set(value):
            return f"{value.get('year')} 年 {value.get('count')} 条"
        if "patentDivAppLegal" in value:
            return (
                f"{value.get('patentDivAppLegal')} "
                f"{value.get('patentCount', 0)} 条"
            )
        if "month" in value and isinstance(value.get("stats"), dict):
            stats = value["stats"]
            return (
                f"{value.get('month')} 负面 {stats.get('negative', 0)} / "
                f"正面 {stats.get('positive', 0)}"
            )
        if "year" in value and any(str(k).endswith("Count") for k in value):
            parts = [
                f"{_FIELD_LABELS.get(str(k), k)} {_num_text(v)}"
                for k, v in value.items()
                if v not in (None, "", "-") and k != "year"
            ]
            return f"{value.get('year')} 年：" + "、".join(parts)
        parts = []
        for key, item in value.items():
            if item in (None, "", "-", [], {}):
                continue
            parts.append(f"{_FIELD_LABELS.get(str(key), key)} {_one_line(item)}")
        return "；".join(parts)
    if isinstance(value, (list, tuple)):
        if all(not isinstance(x, (dict, list, tuple)) for x in value):
            return "、".join(_num_text(x) for x in value if x not in (None, "", "-"))
        return "；".join(_one_line(x) for x in value if x not in (None, "", "-"))
    return _num_text(value)


def _organized_core(core: Mapping[str, Any]) -> Dict[str, Any]:
    """Replace raw nested payloads with readable Chinese field/value text."""
    out = dict(core)
    patent = core.get("patent")
    if isinstance(patent, dict) and not any(
        k in patent for k in _ORGANIZED_KEYS["patent"]
    ):
        organized = {
            "专利总数": patent.get("patentCount"),
            "发明申请": patent.get("inventionAppPatentCount"),
            "发明授权": patent.get("inventionLicPatentCount"),
            "实用新型": patent.get("utilityModelPatentCount"),
            "外观设计": patent.get("appearanceDesignPatentCount"),
            "专利申请年度趋势": _one_line(patent.get("patentTypeAppTimeStat")),
            "专利公开年度趋势": _one_line(patent.get("patentTypePubTimeStat")),
            "专利法律状态": _one_line(patent.get("patentDivAppLegalStat")),
        }
        out["patent"] = {k: v for k, v in organized.items() if v not in (None, "", "-", [], {})}
    tm = core.get("trademark")
    if isinstance(tm, dict) and not any(
        k in tm for k in _ORGANIZED_KEYS["trademark"]
    ):
        organized = {
            "商标总数": tm.get("tmCount"),
            "有效商标数": tm.get("tmValidNumber"),
            "无效商标数": tm.get("tmInvalidNumber"),
            "本年新增": tm.get("tmNumberThisYear"),
            "商标类别": _one_line(tm.get("tmTypeList")),
            "商标状态": _one_line(tm.get("tmStatusList")),
            "状态统计": _one_line(tm.get("tmStatusStat")),
            "申请年度趋势": _one_line(tm.get("tmAppTimeStat")),
            "注册年度趋势": _one_line(tm.get("tmRegTimeStat")),
            "类型统计": _one_line(tm.get("tmTypeStats")),
        }
        out["trademark"] = {k: v for k, v in organized.items() if v not in (None, "", "-", [], {})}
    bid = core.get("bidding")
    if isinstance(bid, dict) and not any(
        k in bid for k in _ORGANIZED_KEYS["bidding"]
    ):
        organized = {
            "中标标的分布": _one_line(bid.get("winbidStatList")),
            "中标区域分布": _one_line(bid.get("winbidAreaStat")),
            "中标金额分布": _one_line(bid.get("winbidAmountStatList")),
            "中标趋势": _one_line(bid.get("winbidTrend")),
            "招投标明细": _one_line(bid.get("bidding_info")),
            "招投标记录总量": bid.get("bidding_total"),
        }
        out["bidding"] = {k: v for k, v in organized.items() if v not in (None, "", "-", [], {})}
    news = core.get("news")
    if isinstance(news, dict) and not any(
        k in news for k in _ORGANIZED_KEYS["news"]
    ):
        organized = {
            "情感分布": _one_line(news.get("newsSentimentStats")),
            "月度情感趋势": _one_line(news.get("newsSentimentTrend")),
        }
        out["news"] = {k: v for k, v in organized.items() if v not in (None, "", "-", [], {})}
    op = core.get("operation")
    if isinstance(op, dict) and not any(
        k in op for k in _ORGANIZED_KEYS["operation"]
    ):
        scale = op.get("scale") if isinstance(op.get("scale"), dict) else {}
        organized = {
            "人员规模": scale.get("staff"),
            "年营业额": scale.get("turnover"),
            "融资轮次": op.get("financing_count"),
            "融资记录": _one_line(op.get("financing_list")),
            "上榜记录": _one_line(op.get("rankings")),
        }
        out["operation"] = {k: v for k, v in organized.items() if v not in (None, "", "-", [], {})}
    return out


def _quality_nonempty(value: Any) -> bool:
    """0/False are real values; only None/''/[]/{} count as empty."""
    if value is None or value == "":
        return False
    if isinstance(value, dict):
        return any(_quality_nonempty(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return any(_quality_nonempty(v) for v in value)
    return True


def _refresh_quality_report(report: Dict[str, Any]) -> None:
    data_source = report.get("data_source")
    core = report.get("core_analysis")
    if not isinstance(data_source, dict) or not isinstance(core, dict):
        return
    sections = core.get("sections")
    if not isinstance(sections, list):
        return
    declared = [s for s in sections if isinstance(s, dict)]
    populated = sum(
        1 for section in declared if _quality_nonempty(core.get(section.get("key")))
    )
    quality = data_source.get("quality_report")
    if not isinstance(quality, dict):
        quality = {}
    # The composer declares every section it attempted before empty bodies are
    # dropped. Keep that declared total so a review pass cannot turn missing
    # dimensions into a false 100% coverage; grow it only when a section was
    # added, and fall back to the current count for foreign payloads.
    try:
        previous_total = int(quality.get("total_sections") or 0)
    except (TypeError, ValueError):
        previous_total = 0
    total = max(len(declared), populated, previous_total)
    quality["total_sections"] = total
    quality["populated_sections"] = populated
    quality["empty_sections"] = max(0, total - populated)
    quality["coverage_pct"] = round(populated / total * 100) if total else 0
    data_source["quality_report"] = quality


def apply_content_review(
    report: Mapping[str, Any], calls: Any = None
) -> Dict[str, Any]:
    """Offline content normalization for an existing competitive-analysis report."""
    reviewed = json.loads(json.dumps(report, ensure_ascii=False))
    core = reviewed.get("core_analysis")
    if isinstance(core, dict):
        sections = core.get("sections")
        organized = _organized_core({k: v for k, v in core.items() if k != "sections"})
        if isinstance(sections, list):
            organized["sections"] = sections
        reviewed["core_analysis"] = organized
    # Patent label: direct patentCount is a total, not merely a type sum.
    patent = (reviewed.get("core_analysis") or {}).get("patent") or {}
    for metric in reviewed.get("metrics") or []:
        if metric.get("label") == "专利类型统计合计" and patent.get("专利总数") is not None:
            metric["label"] = "专利总数"
            metric["hint"] = "上游 patentCount 总数；不代表质量或领先"
    subject = reviewed.get("subject") or {}
    if subject.get("resolved") is False:
        caveat = "主体未确认，仅为同名检索线索，不归属该主体"
        for metric in reviewed.get("metrics") or []:
            if caveat not in str(metric.get("hint") or ""):
                metric["hint"] = f"{metric.get('hint') or ''}（{caveat}）"
            if metric.get("label") == "招投标记录总量" and str(metric.get("value")) == "0":
                metric["hint"] = (
                    "接口明确返回 0 条；主体未确认，仅作检索线索，"
                    "不视为该主体无市场活动"
                )
        for insight in reviewed.get("insights") or []:
            interpretation = str(insight.get("interpretation") or "")
            if caveat not in interpretation:
                updated = interpretation + f" {caveat}，不能据此归属该主体。"
                insight["interpretation"] = updated
                if isinstance(reviewed.get("executive_summary"), list):
                    reviewed["executive_summary"] = [
                        str(item).replace(interpretation, updated)
                        for item in reviewed["executive_summary"]
                    ]
    caliber = reviewed.get("caliber")
    if isinstance(caliber, dict):
        note = "字段已整理为中文可读文本，数值逐项保留，未新增推断。"
        if note not in str(caliber.get("limit") or ""):
            caliber["limit"] = str(caliber.get("limit") or "") + note
    _refresh_quality_report(reviewed)
    return reviewed


def build_direct_payload(
    enterprise: str, keyword_type: str, *, dry_run: bool, skills_root: str,
    max_pages: Optional[int] = None, calls: Any = None,
) -> Dict[str, Any]:
    data = orch.collect_direct(
        enterprise, keyword_type, dry_run=dry_run, skills_root=skills_root,
        detail_max_pages=max_pages,
    )
    meta = data.get("_meta") or {}
    evidence = calls
    if evidence is None:
        evidence = data.get("calls")
    if evidence is None:
        evidence = meta.get("calls")
    errors = meta.get("errors") or {}
    canon, confirmed, reason = _identity(data, enterprise)
    sections: List[Dict[str, Any]] = []
    core: Dict[str, Any] = {}
    for key, title in (
        ("enterprise", "主体与工商基础"),
        ("patent", "专利事实"),
        ("trademark", "商标事实"),
        ("bidding", "招投标公开活动"),
        ("operation", "经营公开线索"),
        ("qualification", "资质证书事实"),
        ("news", "舆情情感统计"),
    ):
        _section(
            sections,
            core,
            key,
            title,
            _base(data) if key == "enterprise" else data.get(key),
        )
    patent = data.get("patent") or {}
    tm = data.get("trademark") or {}
    bid = data.get("bidding") or {}
    qual = data.get("qualification") or {}
    news = data.get("news") or {}
    metrics = []
    insights = []
    records = []
    pt = _patent_total(patent)
    tmn = _int(tm.get("tmCount"))
    valid_tm = _int(tm.get("tmValidNumber"))
    cert = _int(qual.get("certificateCount"))
    recent_cert = _int(qual.get("certNumberThisYear"))
    bid_total = _int(bid.get("bidding_total"))
    for label, value, hint in (
        ("专利类型统计合计", pt, "由已返回专利类型字段合计；不代表质量或领先"),
        ("商标总数", tmn, "商标数量事实"),
        ("有效商标数", valid_tm, "接口有效状态统计"),
        ("资质证书数", cert, "证书概况数量"),
        ("近一年获证数", recent_cert, "证书接口年度口径"),
        ("招投标记录总量", bid_total, "市场活动记录，不代表收入或履约质量"),
    ):
        if value is not None:
            metrics.append({"label": label, "value": str(value), "hint": hint})
    sentiment = news.get("newsSentimentStats") or {}
    neg = _int(sentiment.get("negative"))
    total = sum(
        _int(sentiment.get(k)) or 0
        for k in ("negative", "neutral", "positive", "unknown")
    )
    if total:
        metrics.append(
            {
                "label": "舆情统计总量",
                "value": str(total),
                "hint": "接口情感分类合计，不是竞争分",
            }
        )
    if neg is not None:
        metrics.append(
            {
                "label": "负面舆情统计",
                "value": str(neg),
                "hint": "需人工复核样本，不作法律定性",
            }
        )
    if pt is not None and tmn is not None:
        insights.append(
            {
                "feature": "专利与商标并存事实",
                "evidence": f"专利类型统计合计 {pt}，商标 {tmn}（其中有效 {valid_tm if valid_tm is not None else '未知'}）。",
                "interpretation": "说明知识产权两类公开记录均存在；未提供同业分母、专利质量和权利人逐项核验，不能称领先或形成排名。",
            }
        )
    if pt is not None and bid_total is not None:
        insights.append(
            {
                "feature": "创新记录与市场活动并存",
                "evidence": f"专利类型统计合计 {pt}，招投标记录 {bid_total}。",
                "interpretation": "两个独立域均有公开活动；不能据此归因商业化收入、履约质量或市场份额。",
            }
        )
    if neg is not None and neg > 0:
        insights.append(
            {
                "feature": "负面舆情提示",
                "evidence": f"情感统计中负面 {neg} 条，总量 {total} 条。",
                "interpretation": "竞争基准必须保留该风险线索；需复核时间、样本相关性，不能用正面声量抵消。",
            }
        )
    for m in metrics[:8]:
        records.append({"维度": m["label"], "关键记录": f"{m['value']}（{m['hint']}）"})
    missing = [
        title
        for key, title in DOMAINS
        if not _effective(_base(data) if key == "enterprise" else data.get(key))
    ]
    if not confirmed:
        missing.insert(0, "主体工商确认")
    verdict = {
        "level": "单企业基准事实可用" if confirmed else "数据不足",
        "recommendation": "用于人工对标准备" if confirmed else "先确认主体",
        "summary": (
            "本报告只给出单企业客观基准事实，不生成竞争总分、域分、领先性、排名或市场份额结论。"
            if confirmed
            else "主体未通过工商名称和统一社会信用代码确认，不形成竞争判断。"
        ),
        "blockers": [],
        "key_concerns": ([f"负面舆情统计 {neg} 条"] if neg else [])
        + [f"缺口：{x}" for x in missing],
        "specialty_average": None,
    }
    total_sections = len(DOMAINS)
    populated = len(sections)
    abstract = f"本报告整理「{canon}」的单企业竞争基准事实。" + str(verdict["summary"])
    report = {
        "report_type": REPORT_TYPE,
        "title": f"{canon} 企业竞争基准画像",
        "banner": BANNER,
        "subject": {
            "enterprise": canon,
            "match_raw": enterprise,
            "keywordType": keyword_type,
            "resolved": confirmed,
            "resolve_reason": reason,
        },
        "abstract": abstract,
        "summary": abstract,
        "executive_summary": [verdict["summary"]]
        + [x["interpretation"] for x in insights[:4]],
        "verdict": verdict,
        "specialty_scores": {"items": [], "average": None, "rating_eligible": False},
        "metrics": metrics,
        "caliber": {
            "match_target": canon,
            "match_type": "单企业竞争基准（非多企业横向对比）",
            "data_scope": f"有效覆盖 {populated}/{total_sections} 个主题域；生成时间 {dt.datetime.now().astimezone().isoformat(timespec='seconds')}",
            "products": PRODUCTS,
            "limit": "无可比企业和行业分母，不作排名、领先性、市场份额、收入归因或履约质量结论。缺口："
            + "；".join(missing),
        },
        "core_analysis": {**core, "sections": sections},
        "representative_records": records,
        "insights": insights,
        "data_source": {
            "mcp_server": f"{len(SERVERS)} MCP",
            "mcp_servers": SERVERS,
            "mode": "live_mcp" if meta.get("source") == "live" else "cached_reports",
            "dry_run": dry_run,
            "generated_at": dt.datetime.now()
            .astimezone()
            .isoformat(timespec="seconds"),
            "quality_report": {
                "total_sections": total_sections,
                "populated_sections": populated,
                "empty_sections": total_sections - populated,
                "coverage_pct": round(populated / total_sections * 100),
            },
            "tool_errors": list(errors),
            "products": [{"name": p} for p in PRODUCTS],
        },
    }
    if meta.get("source") == "live":
        from common import attach_pagination

        report = attach_pagination(report, meta.get("pagination_payloads") or {})
        call_usage = meta.get("call_usage")
        if isinstance(call_usage, dict) and call_usage:
            report["data_source"]["call_usage"] = call_usage
        if max_pages is None:
            budget_note = (
                "明细接口默认按单页预算采集（每接口仅请求第 1 页，该页同时用于分析与上游 total 发现，不重复计费）；"
                "如需更多明细页，请先规划所需结论与数据维度，再用 --max-pages N 明确页数预算；"
                "若预算不足以支撑关键结论，必须说明证据缺口与预计所需额外页数，不得悄悄降级结论或扩大计费范围。"
            )
            report["abstract"] += budget_note
            report["summary"] += budget_note
            report["caliber"]["limit"] += budget_note
        for note in (meta.get("schema_limited") or {}).values():
            report["abstract"] += note
            report["summary"] += note
            report["caliber"]["limit"] += note
    return apply_content_review(report, evidence)
