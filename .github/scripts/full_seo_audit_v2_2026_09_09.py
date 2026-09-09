from pathlib import Path

src_path = Path('.github/scripts/full_seo_audit_2026_09_09.py')
src = src_path.read_text(encoding='utf-8')
src = src.replace("m.group(3) or m.group(4) or m.group(5) or ''", "m.group(2) or m.group(3) or m.group(4) or ''")
src = src.replace("for tag in re.findall(r'<img\\b[^>]*>', raw, re.I):", "for tag in re.findall(r'<img\\b[^>]*>', re.sub(r'<!--.*?-->', '', raw, flags=re.S), re.I):")
exec(compile(src, str(src_path), 'exec'))
