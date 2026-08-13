---
name: competitive-analysis-report
description: Use for generating a 竞争分析报告 (竞争分析, 竞品对比, 技术对比, 市场竞争, 竞品分析). Directly connects to 7 MCP servers (enterprise / operation / patent / trademark / bidding / news / qualification), pulls raw data, and runs cross-domain analysis — innovation commercialization, market positioning, brand-patent synergy — producing a scored competitive positioning report. Trigger when users ask for "竞争分析", "竞品对比", "技术对比", "市场竞争", "竞品分析". Infer the enterprise name, connect MCPs, cross-analyze, and produce a radar + gauge + verdict report.
---

# 竞争分析报告

## 定位

竞品技术对比 skill。**直接连接 7 个 MCP server**（工商 / 经营 / 专利 / 商标 / 标讯 / 舆情 / 资质），获取多源原始数据，运行**跨维度交叉分析**。

- MCP 返回的嵌套 JSON 字符串（如金额 `{"coinType":"人民币","value":430000000.0}`、地址 `{"city":"杭州市",...}`）必须解析为可读文本（如"4.30 亿 人民币"、"浙江省杭州市"），绝不在报告正文、表格或指标中输出原始 JSON 字符串。
- 报告所有章节标题、指标卡标签必须用中文；`core_analysis.sections` 的 `title` 字段必须中文，不可显示英文 key（如 `holders`、`investments`）。
- 指标值必须可读化：金额格式为"X 亿/万 + 币种"，地址拼接省市区，比率显示百分号。详见 `references/report-output.md` 的「数据格式约束」。

## 直连的 7 个 MCP

| MCP server | 工具 | 数据用途 |
| --- | --- | --- |
| enterprise-mcp-server | base_info / holders / invest / main_person | 工商基础、股权 |
| enterprise-operation-mcp-server | business_scale / financing / trends / rankings | 经营规模、资本运作 |
| patent-mcp-server | patent_stats | 专利储备、申请授权趋势 |
| trademark-mcp-server | trademark_profile / trademark_stats | 商标布局、类别覆盖 |
| bidding-mcp-server | bid_win_stats / bidding_info | 中标能力、招投标参与 |
| news-mcp-server | news_stats | 舆情健康、情感分布 |
| qualification-mcp-server | qualification_stats | 荣誉资质、高新认证 |

## 交叉分析产出

| 产出 | 说明 |
| --- | --- |
| 专项评分 | 创新实力 / 市场活跃度 / 经营规模 / 资质完备度（0-100） |
| 竞争定位 | 技术领先型 / 市场活跃型 / 稳健经营型 / 需提升 |
| 跨维度洞察 | 创新商业化 / 市场地位 / 商标专利协同 / 创新经营匹配 |

## 脚本速查

```bash
# 默认：直连多 MCP
python scripts/compose_fusion_report.py --enterprise "某公司" --output output/竞争.json --report-output output/竞争.html
# dry-run
python scripts/compose_fusion_report.py --enterprise "某公司" --dry-run --output output/竞争.json --report-output output/竞争.html
```
