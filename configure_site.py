from pathlib import Path
import sys
from urllib.parse import urlparse
p = Path(__file__).parent
old = 'https://YOUR-USERNAME.github.io/GEO_iPhone17/'
if len(sys.argv) != 2:
    raise SystemExit('Cách dùng: python configure_site.py https://USERNAME.github.io/REPOSITORY/')
new = sys.argv[1].strip().rstrip('/') + '/'
u = urlparse(new)
if u.scheme != 'https' or not u.netloc.endswith('.github.io') or not u.path.strip('/'):
    raise SystemExit('Hãy nhập URL GitHub Pages hợp lệ: https://USERNAME.github.io/REPOSITORY/')
for f in list(p.glob('*.html')) + [p / 'sitemap.xml', p / 'robots.txt']:
    s = f.read_text(encoding='utf-8')
    if old in s:
        f.write_text(s.replace(old, new), encoding='utf-8')
        print('Đã cập nhật:', f.name)
print('URL website:', new)
