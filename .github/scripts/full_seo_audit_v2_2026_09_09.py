from pathlib import Path

src_path = Path('.github/scripts/full_seo_audit_2026_09_09.py')
src = src_path.read_text(encoding='utf-8')
src = src.replace("m.group(3) or m.group(4) or m.group(5) or ''", "m.group(2) or m.group(3) or m.group(4) or ''")
exec(compile(src, str(src_path), 'exec'))
