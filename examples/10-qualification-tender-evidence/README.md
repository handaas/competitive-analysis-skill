# 工程资质与公开标讯证据清单

- 用户需求：核对中国建筑第八工程局有限公司的资质证书统计、公开标讯总量和当前页代表记录，分别说明统计总量与样本边界；不要估算全部订单、收入或中标率。
- 决策用途：为工程企业初步尽调提供资质与公开市场活动的可核对事实清单。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：100%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 工商主体必须确认
- 资质证书统计至少一个实际字段非空
- 标讯统计总量和当前页代表记录均真实非空
- 总量与样本数分开呈现
- 不得推断全部订单、收入、中标率或市场份额

## 本轮自动检查发现


## 使用局限

- 公开标讯不覆盖全部商业合同
- 报告不执行证书现行有效性和投标资格审查
- 当前页样本不能重建上游完整去重统计

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '中国建筑第八工程局有限公司' --keyword-type name --output competitive-analysis-skill/output/10-qualification-tender-evidence/report.json --report-output competitive-analysis-skill/output/10-qualification-tender-evidence/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 工商主体必须确认：工商=中国建筑第八工程局有限公司/9131000063126503X1
- **pass** 资质证书统计至少一个实际字段非空：资质实际值样本=[451, 29]
- **pass** 标讯统计总量和当前页代表记录均真实非空：标讯总量=1000、当前页记录=20
- **pass** 总量与样本数分开呈现：报告分别呈现总量=1000与样本=20
- **pass** 不得推断全部订单、收入、中标率或市场份额：qualification=data、bidding=data；洞察明确“不能据此归因商业化收入、履约质量或市场份额”

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)