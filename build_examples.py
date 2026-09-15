"""Rebuild historical sample JSON from reviewed public evidence; never fetches live data."""
import json
from pathlib import Path
P=Path(__file__).parent/'skills/industry-education-report/assets'
sources=[]
def source(id,title,publisher,url,published,locator,scope,excerpt):
 sources.append(dict(id=id,title=title,publisher=publisher,url=url,published=published,accessed='2026-09-15',locator=locator,scope=scope,excerpt=excerpt))
source('S1','2024年广东省国民经济和社会发展统计公报','广东省统计局、国家统计局广东调查总队','https://stats.gd.gov.cn/attachment/0/576/576336/4686764.pdf','2025-03-28','第4页；第8页表4；第9页表5；公报注释','广东省2024年工业统计，初步统计数','释义：新能源汽车产量增长；汽车制造业利润下降，二者统计对象不同。')
source('S2','新能源汽车技术专业教学标准（高等职业教育专科）','教育部','https://www.moe.gov.cn/s78/A07/zcs_ztzl/2017_zt06/17zt06_bznr/bznr_zyjyzyjxbz/gdzyjy_zk/zk_zbzzdl/zbzzdl_qczzl/202502/P020250207528684826334.pdf','2025-02-11（新版标准发布说明日期）','专业名称、职业面向、培养目标','全国高职专科，2025版专业代码460702','释义：培养面向制造装调、质量检验、试制试验和维修服务等方向的人才。')
source('S3','2024年广东省政府工作报告','广东省人民政府','https://www.gd.gov.cn/gdywdt/zwzt/xsdzgts/ywsd/content/post_4354856.html','2024-01-23（报告日期）','2023年工作回顾','广东省历史投产项目','释义：报告回顾深汕比亚迪汽车工业园、小鹏汽车广州工厂全面投产。')
source('S4','教育部办公厅关于编制发布高校毕业生就业质量年度报告的通知','教育部','https://www.moe.gov.cn/srcsite/A15/s3265/201311/t20131105_159491.html','2013-11-15','第二、三条','高校就业质量报告历史框架','释义：就业质量分析用于招生、专业设置与教学反馈。')
source('S5','投资项目可行性研究报告编写大纲及说明','国家发展改革委','https://www.ndrc.gov.cn/xxgk/zcfb/ghxwj/202304/t20230407_1353356.html','2023-04-07','通知附件政府投资项目大纲，章节通过施甸县发改局官方全文核验','2023版投资项目可研框架，专题报告仅作改编','释义：需求、方案、要素、投融资、效果与风险共同支撑决策。')
source('S6','广东省2024年重点建设项目计划表','广东省发展和改革委员会','https://drc.gd.gov.cn/attachment/0/546/546348/4401875.pdf','未标注','印刷页91，广州小鹏新能源汽车零部件产业园项目','2024年项目计划；不代表实际完成','释义：项目建设内容列有压铸车间、电池线及配套。')
source('S7','政府投资项目可行性研究报告编写通用大纲（2023年版）','施甸县发展和改革局（官方转载）','https://www.shidian.gov.cn/info/2588/3304973.htm','2023-06-26','选址要素、投融资、风险管控及结论章节','国家发改委2023版大纲官方全文转载','释义：项目需评估要素保障、财务可持续性和风险管控。')
metrics=[]
def metric(id,label,value,unit,population,definition):
 metrics.append(dict(id=id,label=label,value=value,unit=unit,period='2024自然年',region='广东省',population=population,definition=definition,source_ids=['S1']))
metric('M1','新能源汽车产量',361.78,'万辆','公报工业产品产量统计范围','新能源汽车工业产品产量，非销量或保有量；规上工业范围见公报注释')
metric('M2','新能源汽车产量同比',43.0,'%','公报工业产品产量统计范围','较上年增长率，直接引用公报，不由四舍五入产量反推')
metric('M3','汽车制造业利润总额',318.06,'亿元','规模以上汽车制造业','年主营业务收入2000万元及以上工业企业；涵盖传统动力汽车，非新能源汽车单独利润')
metric('M4','汽车制造业利润同比',-40.4,'%','规模以上汽车制造业','利润总额同比变化；非新能源汽车专属口径')
claims=[]
def claim(id,kind,text,ss=[],ms=[],limit='历史样板，不代表2026年最新情况。'):
 claims.append(dict(id=id,kind=kind,text=text,source_ids=ss,metric_ids=ms,limitation=limit))
claim('K1','fact','广东2024年新能源汽车产量361.78万辆，同比增长43.0%。',ms=['M1','M2'])
claim('K2','inference','省级产品产量增长与汽车制造业利润承压并存：汽车制造业利润318.06亿元，同比下降40.4%。因此产量信号不足以单独支持扩招或投资判断。',ms=['M1','M2','M3','M4'],limit='汽车制造业包含传统动力汽车，不能据此断言新能源汽车利润下降40.4%；不存在从产量到岗位的直接换算。')
claim('K3','recommendation','建议先验证制造装调、质量检验、试制试验和维修服务岗位能力，再设计课程和实训模块。由专业负责人组织企业访谈，访谈样本、岗位地点和日期逐项登记。',['S2'],limit='专业标准提供职业面向，不证明广东岗位需求人数。')
claim('K4','fact','2024年政府工作报告回顾深汕比亚迪汽车工业园、小鹏汽车广州工厂全面投产，可作为历史企业布局线索。',['S3'],limit='事实对应2023年回顾；须核验具体法人及当前运营，不代表与目标院校已合作。')
claim('K5','recommendation','建议将制造装调岗位映射为电池/电驱装调检测实训，将检验岗位映射为质量记录与检测任务，将维修方向映射为故障诊断项目；分别用操作规程、检测记录和诊断报告评价。',['S2'],limit='这是课程模块设计建议，不冒称标准中的逐字课程名；校内师资设备与学分待论证。')
claim('K6','recommendation','建议将毕业去向、就业地域、行业流向和专业相关度分别取数，再用于专业调整和招生反馈；校方确认统计届别、截止日期和分母。',['S4'],limit='未取得目标院校台账，不能计算该校落实率、留粤率或对口就业率。')
claim('K7','recommendation','建议把零部件装调检测服务和电池线配套列为招商访谈主题，并邀请院校论证培训能力；依据2024重点项目计划中的压铸车间、电池线及配套建设内容开展尽调。',['S6','S2'],limit='项目计划不代表实际落地状态或当前招商意向；主题待企业需求、园区资源和环境条件核验。')
claim('K8','recommendation','建议院校先做课程试点评审：教务处负责岗位—课程—考核映射，就业部门补采本校去向数据，资产部门核查实训条件；在企业能力需求和校内资源审核完成后再决定是否扩招。',['S2','S4'],limit='实施节点为建议流程；预算、人数和完成期限须校方确认，未设定虚构量化承诺。')
claim('K9','recommendation','建议政府/园区比较维持现有服务、共建培训检测服务、引进配套项目三种方案。招商主管部门核实企业意向，园区管理方核实空间与要素，财政部门核实资金边界；形成需求和资源台账后再进入项目评审。',['S5','S6'],limit='不构成正式投资可研；无土地、能耗、预算、收益与就业数据，不作财政投入额度或收益率结论。')
claim('K10','recommendation','数据附录应保留产品产量与行业利润的不同统计对象，并按2024自然年呈现；2025专业标准仅作课程规范依据，不与2024产业数合成同年成效。',['S1','S2'],limit='学年、自然年和毕业届别需要独立记录。')
claim('K11','recommendation','建议设置项目评审条件：土地和能耗可用性未核实前不确定建设规模；资金来源和运营成本未核实前不建议财政投入额度；企业需求与院校能力未匹配前不启动订单培养。若尽调显示条件无法满足，应暂缓或转为小规模培训服务方案。',['S7'],limit='这些为拟议风险控制条件，不代表已发现当地土地不足、财政风险或企业承诺违约。')
gaps=[dict(id='D1',description='缺少目标院校毕业去向与专业容量数据',owner='院校就业部门、教务处',required_data='学校名称、毕业届别、毕业人数、分类型去向人数、就业地区行业、专业相关度调查、师资设备与预算',impact='无法评价本校培养成效、留粤率、对口就业和扩招规模'),dict(id='D2',description='缺少地区岗位需求与人才供给的可比台账',owner='人社部门及企业人力资源部门',required_data='地域边界、岗位去重清单、需求人数与时点、技能与学历、实际录用及流失、当地毕业供给',impact='无法测算真实人才缺口或订单班人数'),dict(id='D3',description='缺少目标园区和拟引进项目尽调',owner='园区管理方、招商及项目单位',required_data='园区边界、企业法人和信用代码、意向确认、厂房土地能耗、环境条件、投资预算与绩效基线',impact='无法判断承载能力、财政投入和招商项目可行性')]
gaps.append(dict(id='D4',description='缺少目标地区现行产业政策与行业分类映射',owner='当地发展改革、工业和信息化主管部门',required_data='现行政策原文及有效期、产业链环节与统计行业代码映射、目标地区产业定位及适用条件',impact='无法判断当前政策匹配性和申报资格；历史产业数据不能替代现行政策依据'))
charts=[dict(id='T1',title='广东新能源汽车产量与汽车制造业经营信号（不同统计对象）',metric_ids=['M1','M2','M3','M4'],type='table',note='直接列示公报数据，无派生计算。各行单位不同不相加。产量与行业利润口径不同；2024初步统计数。不能由产量增长推断岗位缺口或新能源汽车利润。')]
templates=json.loads((P/'templates.json').read_text())
for audience in ['college','government']:
 mapping=([(['K2','K8'],[]),(['K1'],[]),(['K3'],['D2']),(['K4'],[]),(['K6'],['D1']),(['K5'],[]),(['K7'],['D3']),(['K8'],[]),(['K10'],[])] if audience=='college' else [(['K2','K9'],[]),(['K1'],['D4']),(['K3','K6'],['D1','D2']),(['K4','K7'],[]),(['K5'],[]),(['K9'],['D3']),(['K2','K11'],[]),(['K10'],[])])
 used={k for cs,gs in mapping for k in cs}
 d=dict(title=f'广东新能源汽车产业链产教决策报告·{ "院校版" if audience=="college" else "政府与园区版"}历史证据样板',audience=audience,region='广东省（未指定具体院校或园区）',chain='新能源汽车',period='2024年产业基线；2025年教学标准',as_of='2026-09-15',status='sample',sources=sources,metrics=metrics,claims=[c for c in claims if c['id'] in used],gaps=[g for g in gaps if g['id'] in {gid for cs,gs in mapping for gid in gs}],charts=charts,sections=[dict(id=spec['id'],claim_ids=cs,gap_ids=gs) for spec,(cs,gs) in zip(templates[audience]['sections'],mapping)])
 out=P/'examples'/audience
 out.mkdir(parents=True,exist_ok=True)
 (out/'report.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
