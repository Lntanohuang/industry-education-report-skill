# industry-education-report · 产业人才需求观察报告技能

基于公开招聘数据的离线快照,按 12 章模板生成《区域×产业人才需求观察报告》:观点式导语 → 图N → 数据解读 → 结论框,逐图核对数据口径与缺口,输出报告 Markdown、结构化 report.json 与验收结果。**模板与数据全部内置,运行时不联网检索、不连接数据库。**

- 模板:`assets/02-报告模板.md`(12 章 + 附录,章节→所需数据映射表)
- 数据:`references/05-数据库字段摸底与口径.md`(广东在招岗位离线快照,含口径定义与质量清单;不含任何数据库连接信息)
- 契约:`references/data-contract.md`(report.json 结构、章节→数据映射、口径红线)
- 示例:`assets/examples/observation/`(结构合格、含登记缺口的完整样板)

## 与 Skill 广场的关系(父子仓库模式)

本仓库是此技能的**权威源头(父仓库)**:技能的一切修改在本仓库进行、在本仓库发布版本。

[skill-plaza-foru](https://github.com/Lntanohuang/skill-plaza-foru)(Skill 广场)不保存本技能的副本,而是通过 git submodule 将本仓库挂载为其 `.agents/skills/industry-education-report`(子引用):

```bash
# 广场侧初始挂载
git submodule add https://github.com/Lntanohuang/industry-education-report-skill.git .agents/skills/industry-education-report

# 本仓库更新后,广场侧同步
git submodule update --remote .agents/skills/industry-education-report && git commit -am "Bump industry-education-report submodule"
```

## 安装与使用(独立使用)

```bash
git clone https://github.com/Lntanohuang/industry-education-report-skill.git
cp -R industry-education-report-skill ~/.agents/skills/industry-education-report   # 或各引擎的技能目录
```

Python 3 标准库,无额外依赖。以技能目录为工作目录:

```bash
python3 scripts/report.py validate assets/examples/observation/report.json
python3 scripts/report.py render  assets/examples/observation/report.json --output /tmp/report.md
python3 scripts/report.py verify  assets/examples/observation/report.json /tmp/report.md
python3 scripts/test_report.py   # 11 项回归测试
```

## 数据边界

- 一切数字出自 05 快照的既算统计,引用必须带节号;快照未提供的交叉统计登记为缺口,不编造。
- 快照不含岗位真实发布时间与职位链接;时间口径为导入批次(2026-06~07)。
- 逐词命中数互有重叠,不能相加为分布;无互斥分类时只能按"含关键词岗位数(非互斥)"降级呈现。
