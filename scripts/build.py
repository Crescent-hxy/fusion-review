"""Build compact Markdown tables, CSV and a standalone searchable index."""
import json,csv,pathlib,collections,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
PAPERS=json.loads((ROOT/'data/papers.json').read_text())
TASKS={'ivif':'红外与可见光','medical':'医学图像','general':'通用融合','focus':'多聚焦','exposure':'多曝光','remote':'遥感与高光谱','polar':'光谱与偏振','video':'视频融合','assessment':'融合质量评价','related':'相关工作（非双源像素融合）'}
def a(url,label):return f'[{label}]({url})' if url else '待补全'
def table(papers):
 lines=['| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题标签 | 链接 | 状态 |','| :-- | :-- | :-- | :-- | :-- | :-- |']
 for p in papers:
  status='预印本' if p['publication_status']=='预印本' else ('待核对' if p['publication_status']!='正式发表' else '已核对')
  if '尚未' in p['code_status'] or '仅公告' in p['code_status']:status+='；代码待发布/核实'
  lines.append(f"| **{p['name']}** | {p['year']} · {p['venue']} | {p['title']} | {' / '.join(p['tags']) or '待核对'} | {a(p['paper'],'Paper')} · {a(p['code'],'Code')} | {status} |")
 return '\n'.join(lines)
counts=collections.Counter(t for p in PAPERS for t in p['tasks'])
intro=f'''<div align="center">

# Fusion Review

### 图像融合文献索引

**{len(PAPERS)} 个去重条目 · 检索截至 2026-10-09 · 中文分类导航**

[可搜索表格](index.html) · [CSV](data/papers.csv) · [JSON](data/papers.json) · [核对规则](docs/methodology.md) · [更新记录](CHANGELOG.md)

</div>

以像素级图像融合为主，仅收录本次范围内已核对发表信息的工作。按**应用任务**分表，使用**研究问题与技术标签**交叉索引。配准、任务驱动、退化鲁棒、文本控制、扩散与 Mamba 等均作为标签，不与应用任务混为同一级分类。

下载后直接打开 `index.html` 即可搜索、筛选与导出；GitHub 文件页展示 HTML 源码，本次未启用网页托管。表格中的“已核对”指作者来源或出版平台的发表元数据已检查，**不代表已复现**。不在本次范围内的文献及未确认发表的预印本移入 archive，保留原始收藏。

## 分类导航

| 分类 | 条目数 | 入口 |
| :-- | --: | :-- |
'''
for t,n in TASKS.items():intro+=f'| {n} | {counts[t]} | [跳转](#{t}) |\n'
intro+='\n通用方法可以出现在多个应用表中，分类数之和不等于去重总数。语义先验与任务监督分别标注；相关特征融合、单图知识迁移与评价方法单列。\n'
sections=[]
for t,n in TASKS.items():sections.extend([f'<a id="{t}"></a>',f'## {n}','',table([p for p in PAPERS if t in p['tasks']]),''])
end='''## 维护与来源

数据源为 `data/papers.json`，每条记录含来源、核对日期及备注。运行 `python scripts/build.py` 更新表格与页面，运行 `python scripts/validate.py` 做结构校验。

原始收藏保存在 [archive/README-original.md](archive/README-original.md)。本次范围：CVPR / ICCV / ECCV / NeurIPS / ICML / AAAI / MICCAI / ACM MM；TPAMI / TIP / IJCV / TMM / TCSVT / Information Fusion / Pattern Recognition / TGRS。按固定白名单收录，不代表统一或官方的期刊等级排名。尚未覆盖全部相关文献；不提供方法性能排名。
'''
(ROOT/'README.md').write_text(intro+'\n'+'\n'.join(sections)+end)
(ROOT/'docs/catalog.md').write_text('# 文献表格\n\n'+'\n'.join(sections))
with (ROOT/'data/papers.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(PAPERS[0]));w.writeheader()
 for p in PAPERS:w.writerow({k:'; '.join(v) if isinstance(v,list) else v for k,v in p.items()})
template=(ROOT/'index.template.html').read_text()
(ROOT/'index.html').write_text(template.replace('__PAPERS__',json.dumps(PAPERS,ensure_ascii=False).replace('<','\\u003c')).replace('__TASKS__',json.dumps(TASKS,ensure_ascii=False)))
print(f'Built {len(PAPERS)} records; {sum(p["publication_status"]=="正式发表" for p in PAPERS)} publication metadata checked.')
