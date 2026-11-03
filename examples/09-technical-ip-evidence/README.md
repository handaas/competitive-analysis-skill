# 技术知识产权事实基线

- 用户需求：整理华为技术有限公司的专利类型累计量、申请或公开趋势以及法律状态分布，形成技术知识产权事实基线；不评分、不排名，也不判断专利质量或行业领先。
- 决策用途：验证竞争分析 skill 能否提供可追溯的技术知识产权事实，而不把数量升级为竞争结论。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：100%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 工商主体必须确认
- 专利类型累计量至少一个字段为真实非空值
- 申请趋势或公开趋势至少一个序列含真实非空数据
- 法律状态分布保留上游口径
- 不得输出专利质量、商业价值、总分、排名或领先结论

## 本轮自动检查发现


## 使用局限

- 单企业事实基线不是完整竞品评估
- 累计申请和授权不能计算同批申请成功率
- 专利质量需结合权利要求、同族、引用和稳定性另行分析

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '华为技术有限公司' --keyword-type name --output competitive-analysis-skill/output/09-technical-ip-evidence/report.json --report-output competitive-analysis-skill/output/09-technical-ip-evidence/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 工商主体必须确认：工商=华为技术有限公司/914403001922038216
- **pass** 专利类型累计量至少一个字段为真实非空值：类型值=[133237, 59570, 66820, 3440, 3407]
- **pass** 申请趋势或公开趋势至少一个序列含真实非空数据：申请/公开时间序列=10项
- **pass** 法律状态分布保留上游口径：法律状态=[{'patentCount': 1429, 'patentDivAppLegal': '专利实施许可合同备案的生效、变更及注销'}, {'patentCount': 217, 'patentDivAppLegal': '著录事项变更'}, {'patentCount': 13, 'patentDivAppLegal': '专利权的终止专利权有效期届满'}, {'patentCount': 2, 'patentDivAppLegal': '专利权的终止专利权的主动放弃'}]
- **pass** 不得输出专利质量、商业价值、总分、排名或领先结论：patent调用=data；摘要明确“不生成竞争总分、领先性、排名”，洞察明确“不能称领先或形成排名”

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)
[页面截图](browser.png)