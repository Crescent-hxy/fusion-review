"""Validate index integrity and local document targets without network access."""
import json,pathlib,re,csv
from urllib.parse import urlparse
root=pathlib.Path(__file__).resolve().parents[1]
papers=json.loads((root/'data/papers.json').read_text())
ids=set();repos=set()
tasks={'ivif','medical','general','focus','exposure','remote','polar','video','assessment','related'}
for p in papers:
 assert p['id'] not in ids,('duplicate id',p['id']);ids.add(p['id'])
 assert p['name'] not in ('-','新方法X')
 assert p['tasks'] and set(p['tasks'])<=tasks
 assert isinstance(p['year'],int) and 1900<=p['year']<=2026
 assert p['verification'] and p['checked_at']=='2026-10-09'
 if p['publication_status']!='待核对':assert p['sources'],p['name']
 if p['repo']:
  key=p['repo'].lower();assert key not in repos,('duplicate repository',key);repos.add(key)
 for url in [p['paper'],p['code'],*p['sources']]:
  if url:assert urlparse(url).scheme in ('http','https') and urlparse(url).netloc and not re.search(r'[\s<>]',url),(p['name'],url)
for path in [root/'README.md',root/'docs/methodology.md',root/'CHANGELOG.md']:
 for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
  if not target.startswith(('http:','https:','#')):assert (path.parent/target.split('#')[0]).exists(),(path,target)
page=(root/'index.html').read_text()
assert '__PAPERS__' not in page and '__TASKS__' not in page
assert json.loads(re.search(r'const papers=(.*?),tasks=',page).group(1))==papers
with (root/'data/papers.csv').open(encoding='utf-8-sig') as f:assert len(list(csv.DictReader(f)))==len(papers)
print(f'OK: {len(papers)} unique records; URLs, classification, local links and generated data are consistent.')
