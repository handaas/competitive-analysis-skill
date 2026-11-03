# 消费品牌商标保护事实清单

- 用户需求：整理贵州茅台酒股份有限公司的商标总量、有效状态分布、类别分布和申请/注册时间序列，形成品牌保护事实清单；不要估算品牌价值、销量、市场份额或整体竞争力。
- 决策用途：验证商标保护数据的状态、类别和时间口径能否被独立呈现。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：100%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 工商主体必须确认
- 商标总量或有效商标字段至少一项真实非空
- 商标状态分布至少一个非空项
- 商标类别分布至少一个实际项非空
- 商标申请或注册时间序列至少一个系列含真实非空数据
- 不得用商标数量推断品牌价值、销量、份额或排名

## 本轮自动检查发现


## 使用局限

- 商标数量不等于品牌价值或实际使用强度
- 类别与状态需以商标主管机关记录复核
- 不覆盖关联公司或许可使用的完整品牌资产

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '贵州茅台酒股份有限公司' --keyword-type name --output competitive-analysis-skill/output/11-brand-protection-evidence/report.json --report-output competitive-analysis-skill/output/11-brand-protection-evidence/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 工商主体必须确认：工商=贵州茅台酒股份有限公司/9152000071430580XT
- **pass** 商标总量或有效商标字段至少一项真实非空：tmCount=89、tmValidNumber=33
- **pass** 商标状态分布至少一个非空项：状态项=[25, 14, 1, 35]
- **pass** 商标类别分布至少一个实际项非空：类别项=[{'count': 46, 'tmName': '33-酒'}, {'count': 20, 'tmName': '35-广告销售'}, {'count': 10, 'tmName': '32-啤酒饮料'}, {'count': 6, 'tmName': '16-办公用品'}]
- **pass** 商标申请或注册时间序列至少一个系列含真实非空数据：申请/注册时间序列=10项
- **pass** 不得用商标数量推断品牌价值、销量、份额或排名：trademark=data，未检出品牌价值/销量/份额/排名外推

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)