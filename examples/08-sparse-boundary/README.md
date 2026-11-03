# 不存在企业竞争边界测试

- 用户需求：分析深圳市不存在的星河量子商业有限公司，验证无数据时不会输出虚假竞争定位。
- 决策用途：测试评分门禁和空报告渲染。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：29%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 主体无法确认时明确提示
- 空维度不获得正向评分
- 不生成虚构专利商标或标讯
- 数据源模式不从失败静默降级为已验证结论

## 本轮自动检查发现


## 使用局限

- 该名称为边界测试输入
- 无结果不是行业竞争力低的证据

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '深圳市不存在的星河量子商业有限公司' --keyword-type name --output competitive-analysis-skill/output/08-sparse-boundary/report.json --report-output competitive-analysis-skill/output/08-sparse-boundary/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 主体无法确认时明确提示：subject.resolved=false并明确缺少工商名称和统一社会信用代码。；本轮当前产物：technical=passed，successful_data_calls=1；subject.enterprise=深圳市不存在的星河量子商业有限公司，resolved=False；metrics[招投标记录总量=0]；quality={'total_sections': 7, 'populated_sections': 2, 'empty_sections': 5, 'coverage_pct': 29}；非空章节=['招投标公开活动', '经营公开线索']；代表记录=1；calls[patent:patent_bigdata_patent_stats=empty；qualification:qualification_bigdata_qualification_certificate_profile=empty；news:news_bigdata_news_stats=empty；bidding:bid_bigdata_bid_win_stats=empty；bidding:bid_bigdata_bidding_info=empty；trademark:trademark_bigdata_trademark_profile=empty；trademark:trademark_bigdata_trademark_stats=empty；operation:operation_insight_business_scale=empty；operation:operation_insight_financing_info=empty；operation:operation_insight_company_trends=empty；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=empty；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=empty]
- **pass** 空维度不获得正向评分：无竞争域分；标讯总量0为客观空记录，不是正向评分。；本轮当前产物：technical=passed，successful_data_calls=1；subject.enterprise=深圳市不存在的星河量子商业有限公司，resolved=False；metrics[招投标记录总量=0]；quality={'total_sections': 7, 'populated_sections': 2, 'empty_sections': 5, 'coverage_pct': 29}；非空章节=['招投标公开活动', '经营公开线索']；代表记录=1；calls[patent:patent_bigdata_patent_stats=empty；qualification:qualification_bigdata_qualification_certificate_profile=empty；news:news_bigdata_news_stats=empty；bidding:bid_bigdata_bid_win_stats=empty；bidding:bid_bigdata_bidding_info=empty；trademark:trademark_bigdata_trademark_profile=empty；trademark:trademark_bigdata_trademark_stats=empty；operation:operation_insight_business_scale=empty；operation:operation_insight_financing_info=empty；operation:operation_insight_company_trends=empty；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=empty；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=empty]
- **pass** 不生成虚构专利商标或标讯：专利、商标、标讯调用均为空，core_analysis未生成虚构明细。；本轮当前产物：technical=passed，successful_data_calls=1；subject.enterprise=深圳市不存在的星河量子商业有限公司，resolved=False；metrics[招投标记录总量=0]；quality={'total_sections': 7, 'populated_sections': 2, 'empty_sections': 5, 'coverage_pct': 29}；非空章节=['招投标公开活动', '经营公开线索']；代表记录=1；calls[patent:patent_bigdata_patent_stats=empty；qualification:qualification_bigdata_qualification_certificate_profile=empty；news:news_bigdata_news_stats=empty；bidding:bid_bigdata_bid_win_stats=empty；bidding:bid_bigdata_bidding_info=empty；trademark:trademark_bigdata_trademark_profile=empty；trademark:trademark_bigdata_trademark_stats=empty；operation:operation_insight_business_scale=empty；operation:operation_insight_financing_info=empty；operation:operation_insight_company_trends=empty；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=empty；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=empty]
- **pass** 数据源模式不从失败静默降级为已验证结论：mode为live_mcp，summary明确主体未确认而非把失败降级为已验证结论。；本轮当前产物：technical=passed，successful_data_calls=1；subject.enterprise=深圳市不存在的星河量子商业有限公司，resolved=False；metrics[招投标记录总量=0]；quality={'total_sections': 7, 'populated_sections': 2, 'empty_sections': 5, 'coverage_pct': 29}；非空章节=['招投标公开活动', '经营公开线索']；代表记录=1；calls[patent:patent_bigdata_patent_stats=empty；qualification:qualification_bigdata_qualification_certificate_profile=empty；news:news_bigdata_news_stats=empty；bidding:bid_bigdata_bid_win_stats=empty；bidding:bid_bigdata_bidding_info=empty；trademark:trademark_bigdata_trademark_profile=empty；trademark:trademark_bigdata_trademark_stats=empty；operation:operation_insight_business_scale=empty；operation:operation_insight_financing_info=empty；operation:operation_insight_company_trends=empty；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=empty；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=empty]

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)