# competitive-analysis-skill：已验收示例

本目录只展示 **6 个完全通过的真实正向场景**（最低要求4例）。

每例均为真实、非空、非缓存调用；技术检查、独立业务检查和离线浏览器检查全部通过。不把空数据、报错处理或仅生成页面计作通过。历史验收记录保留在本地 test-records/；本目录的 HTML/Markdown 由原 JSON 重渲染，不代表重新查询或重新验收。

| 场景 | 真实使用需求 | 报告 |
|---|---|---|
| [技术知识产权事实基线](09-technical-ip-evidence/README.md) | 整理华为技术有限公司的专利类型累计量、申请或公开趋势以及法律状态分布，形成技术知识产权事实基线；不评分、不排名，也不判断专利质量或行业领先。 | [HTML](09-technical-ip-evidence/report.html) / [MD](09-technical-ip-evidence/report.md) / [JSON](09-technical-ip-evidence/report.json) |
| [工程资质与公开标讯证据清单](10-qualification-tender-evidence/README.md) | 核对中国建筑第八工程局有限公司的资质证书统计、公开标讯总量和当前页代表记录，分别说明统计总量与样本边界；不要估算全部订单、收入或中标率。 | [HTML](10-qualification-tender-evidence/report.html) / [MD](10-qualification-tender-evidence/report.md) / [JSON](10-qualification-tender-evidence/report.json) |
| [消费品牌商标保护事实清单](11-brand-protection-evidence/README.md) | 整理贵州茅台酒股份有限公司的商标总量、有效状态分布、类别分布和申请/注册时间序列，形成品牌保护事实清单；不要估算品牌价值、销量、市场份额或整体竞争力。 | [HTML](11-brand-protection-evidence/report.html) / [MD](11-brand-protection-evidence/report.md) / [JSON](11-brand-protection-evidence/report.json) |
| [新闻分类与资质事实复核清单](12-news-qualification-review/README.md) | 整理宁德时代新能源科技股份有限公司的新闻情感统计、新闻趋势和资质证书统计，形成需要人工复核的公开事实清单；不要把负面标签直接解释为违法、重大合规风险或竞争劣势。 | [HTML](12-news-qualification-review/report.html) / [MD](12-news-qualification-review/report.md) / [JSON](12-news-qualification-review/report.json) |
| [舆情压力下的竞争画像](06-news-risk/README.md) | 分析特斯拉（上海）有限公司的创新、市场和舆情组合，检查负面舆情是否影响综合判断。 | [HTML](06-news-risk/report.html) / [MD](06-news-risk/report.md) / [JSON](06-news-risk/report.json) |
| [不存在企业竞争边界测试](08-sparse-boundary/README.md) | 分析深圳市不存在的星河量子商业有限公司，验证无数据时不会输出虚假竞争定位。 | [HTML](08-sparse-boundary/report.html) / [MD](08-sparse-boundary/report.md) / [JSON](08-sparse-boundary/report.json) |

- [逐例验收结果](results.json) · [业务复核](review.json) · [证据摘要](evidence-index.json)
- 完整测试记录仅存于本地 test-records/live-replaced-20261027/（仅本地审计用，不随本目录发布），不属于可展示示例。
- 当前数据与结论限于原查询时点及公开样本；覆盖率不代表准确率或低风险。
