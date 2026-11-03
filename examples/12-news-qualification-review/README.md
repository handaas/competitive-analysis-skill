# 新闻分类与资质事实复核清单

- 用户需求：整理宁德时代新能源科技股份有限公司的新闻情感统计、新闻趋势和资质证书统计，形成需要人工复核的公开事实清单；不要把负面标签直接解释为违法、重大合规风险或竞争劣势。
- 决策用途：验证新闻分类线索能否与资质事实分开呈现并保持人工复核边界。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：100%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 工商主体必须确认
- 新闻情感统计至少一个分类为真实非空值
- 新闻趋势至少一个时间点含真实数据
- 资质证书或许可统计至少一个实际字段非空
- 负面标签不得直接定性为违法或合规结论

## 本轮自动检查发现


## 使用局限

- 自动情感分类可能误判
- 资质数量不证明所有证书当前有效
- 报告不替代监管、处罚或新闻事实核验

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '宁德时代新能源科技股份有限公司' --keyword-type name --output competitive-analysis-skill/output/12-news-qualification-review/report.json --report-output competitive-analysis-skill/output/12-news-qualification-review/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 工商主体必须确认：工商=宁德时代新能源科技股份有限公司/91350900587527783P
- **pass** 新闻情感统计至少一个分类为真实非空值：情感分类=[184, 3006, 2362, 20]
- **pass** 新闻趋势至少一个时间点含真实数据：新闻趋势=[{'month': '2025-09', 'stats': {'negative': 0, 'positive': 6}}, {'month': '2025-10', 'stats': {'negative': 0, 'positive': 1}}, {'month': '2025-11', 'stats': {'negative': 0, 'positive': 4}}, {'month': '2025-12', 'stats': {'negative': 0, 'positive': 10}}]
- **pass** 资质证书或许可统计至少一个实际字段非空：资质实际值样本=[196, 25]
- **pass** 负面标签不得直接定性为违法或合规结论：news=data、qualification=data，负面项仅作线索且未检出违法/合规定性

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)