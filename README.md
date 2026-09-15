# 产教决策报告 SKILL

面向院校管理者、政府部门和产业园区，提供两版有证据的产教决策报告模板、广东新能源汽车历史样板与自动检查工具。模板根据教育部就业质量报告框架、专业教学标准和发改委可研框架研究改编，不是官方统一报送模板。

## 内容

- [技能入口](skills/industry-education-report/SKILL.md)
- [院校版样板](skills/industry-education-report/assets/examples/college/report.md)
- [政府与园区版样板](skills/industry-education-report/assets/examples/government/report.md)
- [模板原始来源及映射](skills/industry-education-report/references/template-provenance.md)
- [广东证据检索记录](skills/industry-education-report/references/guangdong-evidence.md)
- [数据结构契约](skills/industry-education-report/references/data-contract.md)
- [语义审核](review.md)

两套样板覆盖区域产业、岗位人才、重点企业、就业去向、专业课程、招商。采用2024产业基线与2025教学标准，不是2026最新态势。没有指定院校/园区，因此就业微观数据、真实岗位缺口和园区承载条件作为有责任方的缺口，未伪造实际结论。

## 安装与使用

将 `skills/industry-education-report` 整个目录复制到 `~/.codex/skills/`。调用：

> 使用 $industry-education-report，根据我提供的院校模板，为广东新能源汽车产业链生成院校版决策报告，逐条核对证据，输出报告和验收结果。

Python 3 标准库，无额外包依赖。以技能目录为工作目录：

```bash
python3 scripts/report.py validate assets/examples/college/report.json
python3 scripts/report.py render assets/examples/college/report.json --output /tmp/college-report.md
python3 scripts/report.py verify assets/examples/college/report.json /tmp/college-report.md
python3 scripts/test_report.py
```

输出文件默认独占创建，防止覆盖已有材料。JSON 是可复核的报告底稿；Markdown 自动附来源和图表底表。已有 Word/PDF 模板需先建立逐项映射，导出后另作版面验收。

## 验收边界

自动检查：章节顺序与覆盖、必填字段、证据ID、有限数值、日期、派生算式与口径、循环推导、图表注释、缺口登记和正文一致性。十项回归测试覆盖关键失败路径。

**结构通过不等于数据充分或审批合格。** 脚本不会因缺口列表为空就宣称数据齐备；引用是否支持结论、用户实际模板适用性仍需语义审核。两份样板的结构与正文一致性均通过，决策所需微观数据尚不完备。

仓库不含院校个人数据、内部台账或第三方全文附件。公开来源只保留必要释义与链接。
