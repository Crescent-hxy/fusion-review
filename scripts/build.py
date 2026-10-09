"""Build compact Markdown tables, CSV and a standalone searchable index."""
import json,csv,pathlib,collections,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
PAPERS=json.loads((ROOT/'data/papers.json').read_text())
TASKS={'ivif':'红外与可见光','medical':'医学图像','general':'通用融合','focus':'多聚焦','exposure':'多曝光','remote':'遥感与高光谱','polar':'光谱与偏振','video':'视频融合','assessment':'融合质量评价','related':'相关工作（非双源像素融合）'}
def a(url,label):return f'[{label}]({url})' if url else '—'
def table(papers):
 lines=['| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |','| :-- | :-- | :-- | :-- | :-- |']
 for p in papers:
  links=f"{a(p['paper'],'Paper')} · {a(p['code'],'Code')}"
  if '尚未' in p['code_status'] or '仅公告' in p['code_status']:links+='（代码待发布）'
  lines.append(f"| **{p['name']}** | {p['year']} · {p['venue']} | {p['title']} | {' / '.join(p['tags']) or '—'} | {links} |")
 return '\n'.join(lines)
counts=collections.Counter(t for p in PAPERS for t in p['tasks'])
TASKS={t:n for t,n in TASKS.items() if counts[t]}
intro=f'''# Image Fusion Review | 图像融合论文与代码

图像融合论文与开源代码整理，涵盖红外与可见光、医学图像、多聚焦、多曝光、遥感和视频融合。按应用任务分类，并标注配准、任务驱动、扩散模型、文本控制等研究方向，方便查找论文和实现。

A collection of image fusion papers and code: infrared and visible image fusion, multimodal medical image fusion, multi-focus fusion, multi-exposure fusion, remote sensing, and video fusion.

**{len(PAPERS)} 篇论文 · 更新于 2026-10-09**

[搜索与筛选](index.html) · [下载 CSV](data/papers.csv) · [收录范围](docs/methodology.md) · [更新记录](CHANGELOG.md)

下载仓库后，用浏览器打开 `index.html`，可按关键词、任务、年份和技术标签筛选，并导出结果。

## 目录

| 任务 | 论文数 | 入口 |
| :-- | --: | :-- |
'''
for t,n in TASKS.items():intro+=f'| {n} | {counts[t]} | [查看](#{t}) |\n'
intro+='\n各表按年份倒序排列。同一方法涉及多个任务时，会出现在对应表中。\n'
sections=[]
for t,n in TASKS.items():sections.extend([f'<a id="{t}"></a>',f'## {n}','',table([p for p in PAPERS if t in p['tasks']]),''])
end='''## 收录与贡献

重点收录 CVPR、ICCV、ECCV、NeurIPS、ICML、AAAI、MICCAI、ACM MM，以及 TPAMI、TIP、IJCV、TMM、TCSVT、Information Fusion、Pattern Recognition、TGRS 的相关论文。

欢迎通过 Issue 或 PR 补充遗漏论文、修正分类或更新代码链接。请附上论文标题、发表渠道、年份和原文或作者代码链接。

数据保存在 [data/papers.json](data/papers.json)。修改后运行 `python scripts/build.py` 生成表格与页面，再运行 `python scripts/validate.py` 检查。原有收藏保留在 [archive](archive/README-original.md)。
'''
(ROOT/'README.md').write_text(intro+'\n'+'\n'.join(sections)+end)
with (ROOT/'data/papers.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(PAPERS[0]));w.writeheader()
 for p in PAPERS:w.writerow({k:'; '.join(v) if isinstance(v,list) else v for k,v in p.items()})
template=(ROOT/'index.template.html').read_text()
(ROOT/'index.html').write_text(template.replace('__PAPERS__',json.dumps(PAPERS,ensure_ascii=False).replace('<','\\u003c')).replace('__TASKS__',json.dumps(TASKS,ensure_ascii=False)))
print(f'Built {len(PAPERS)} records; {sum(p["publication_status"]=="正式发表" for p in PAPERS)} publication metadata checked.')
