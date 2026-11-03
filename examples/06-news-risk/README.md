# 舆情压力下的竞争画像

- 用户需求：分析特斯拉（上海）有限公司的创新、市场和舆情组合，检查负面舆情是否影响综合判断。
- 决策用途：检验声誉风险在竞争评价中的体现。
- 本轮结果：**本轮检查通过**
- 实际工具调用：15；失败 0
- 章节覆盖率：100%（不代表证据质量）

## 预期业务检查（不自动宣称通过）

- 情感分布有具体统计依据
- 新闻数量与风险严重性不混淆
- 创新和市场维度独立展示
- 综合结论说明数据不足项

## 本轮自动检查发现


## 使用局限

- 舆情情感分类可能存在误判
- 单企业画像不能替代与指定竞品的对比

## 证据与复现

- [审计结果](result.json)
- [工具调用、结果形态与响应摘要哈希](calls.json)
- [JSON](report.json) / [HTML](report.html) / [Markdown](report.md)

```bash
python3 competitive-analysis-skill/scripts/compose_fusion_report.py --enterprise '特斯拉（上海）有限公司' --keyword-type name --output competitive-analysis-skill/output/06-news-risk/report.json --report-output competitive-analysis-skill/output/06-news-risk/report.html
```

## 逐场景业务复核

当前冻结产物逐项满足场景契约；结论仅限本轮公开数据和报告口径。

- **pass** 情感分布有具体统计依据：metrics给舆情总量721、负面121，保留具体情感统计。；本轮当前产物：technical=passed，successful_data_calls=13；subject.enterprise=特斯拉（上海）有限公司，resolved=False；metrics[专利类型统计合计=2；商标总数=18；有效商标数=0；资质证书数=81；近一年获证数=22；招投标记录总量=28；舆情统计总量=721；负面舆情统计=121]；quality={'total_sections': 7, 'populated_sections': 7, 'empty_sections': 0, 'coverage_pct': 100}；非空章节=['主体与工商基础', '专利事实', '商标事实', '招投标公开活动', '经营公开线索', '资质证书事实', '舆情情感统计']；代表记录=8；calls[patent:patent_bigdata_patent_stats=data；qualification:qualification_bigdata_qualification_certificate_profile=data；news:news_bigdata_news_stats=data；bidding:bid_bigdata_bid_win_stats=data；bidding:bid_bigdata_bidding_info=data(20/28)；trademark:trademark_bigdata_trademark_profile=data；trademark:trademark_bigdata_trademark_stats=data；operation:operation_insight_business_scale=data；operation:operation_insight_financing_info=data；operation:operation_insight_company_trends=data；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=data；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=data(7/7)]
- **pass** 新闻数量与风险严重性不混淆：洞察要求复核时间与样本相关性，不用正面声量抵消负面或推断法律风险。；本轮当前产物：technical=passed，successful_data_calls=13；subject.enterprise=特斯拉（上海）有限公司，resolved=False；metrics[专利类型统计合计=2；商标总数=18；有效商标数=0；资质证书数=81；近一年获证数=22；招投标记录总量=28；舆情统计总量=721；负面舆情统计=121]；quality={'total_sections': 7, 'populated_sections': 7, 'empty_sections': 0, 'coverage_pct': 100}；非空章节=['主体与工商基础', '专利事实', '商标事实', '招投标公开活动', '经营公开线索', '资质证书事实', '舆情情感统计']；代表记录=8；calls[patent:patent_bigdata_patent_stats=data；qualification:qualification_bigdata_qualification_certificate_profile=data；news:news_bigdata_news_stats=data；bidding:bid_bigdata_bid_win_stats=data；bidding:bid_bigdata_bidding_info=data(20/28)；trademark:trademark_bigdata_trademark_profile=data；trademark:trademark_bigdata_trademark_stats=data；operation:operation_insight_business_scale=data；operation:operation_insight_financing_info=data；operation:operation_insight_company_trends=data；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=data；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=data(7/7)]
- **pass** 创新和市场维度独立展示：专利2与招投标28独立展示。；本轮当前产物：technical=passed，successful_data_calls=13；subject.enterprise=特斯拉（上海）有限公司，resolved=False；metrics[专利类型统计合计=2；商标总数=18；有效商标数=0；资质证书数=81；近一年获证数=22；招投标记录总量=28；舆情统计总量=721；负面舆情统计=121]；quality={'total_sections': 7, 'populated_sections': 7, 'empty_sections': 0, 'coverage_pct': 100}；非空章节=['主体与工商基础', '专利事实', '商标事实', '招投标公开活动', '经营公开线索', '资质证书事实', '舆情情感统计']；代表记录=8；calls[patent:patent_bigdata_patent_stats=data；qualification:qualification_bigdata_qualification_certificate_profile=data；news:news_bigdata_news_stats=data；bidding:bid_bigdata_bid_win_stats=data；bidding:bid_bigdata_bidding_info=data(20/28)；trademark:trademark_bigdata_trademark_profile=data；trademark:trademark_bigdata_trademark_stats=data；operation:operation_insight_business_scale=data；operation:operation_insight_financing_info=data；operation:operation_insight_company_trends=data；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=data；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=data(7/7)]
- **pass** 综合结论说明数据不足项：summary说明主体未确认，caliber明确主体工商确认缺口。；本轮当前产物：technical=passed，successful_data_calls=13；subject.enterprise=特斯拉（上海）有限公司，resolved=False；metrics[专利类型统计合计=2；商标总数=18；有效商标数=0；资质证书数=81；近一年获证数=22；招投标记录总量=28；舆情统计总量=721；负面舆情统计=121]；quality={'total_sections': 7, 'populated_sections': 7, 'empty_sections': 0, 'coverage_pct': 100}；非空章节=['主体与工商基础', '专利事实', '商标事实', '招投标公开活动', '经营公开线索', '资质证书事实', '舆情情感统计']；代表记录=8；calls[patent:patent_bigdata_patent_stats=data；qualification:qualification_bigdata_qualification_certificate_profile=data；news:news_bigdata_news_stats=data；bidding:bid_bigdata_bid_win_stats=data；bidding:bid_bigdata_bidding_info=data(20/28)；trademark:trademark_bigdata_trademark_profile=data；trademark:trademark_bigdata_trademark_stats=data；operation:operation_insight_business_scale=data；operation:operation_insight_financing_info=data；operation:operation_insight_company_trends=data；operation:operation_insight_enterprise_rankings=empty；enterprise:enterprise_get_enterprise_base_info=data；enterprise:enterprise_get_enterprise_holder_info=data；enterprise:enterprise_get_enterprise_invest_info=empty；enterprise:enterprise_get_enterprise_main_person_info=data(7/7)]

## 离线浏览器检查

[Ego Lite 离线图表、页面溢出和脚本检查](browser-check.json)