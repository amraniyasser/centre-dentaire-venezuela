from pathlib import Path

src_path = Path('.github/scripts/full_seo_audit_2026_09_09.py')
src = src_path.read_text(encoding='utf-8')
src = src.replace("m.group(3) or m.group(4) or m.group(5) or ''", "m.group(2) or m.group(3) or m.group(4) or ''")
src = src.replace("raw = p.read_text(encoding='utf-8')", "raw = re.sub(r'<!--.*?-->', '', p.read_text(encoding='utf-8'), flags=re.S)")
src = src.replace("    # images alt + assets\n    for tag in re.findall(r'<img\\b[^>]*>', raw, re.I):", "    # images alt + assets\n    raw_markup = re.sub(r'<style\\b.*?</style>|<script\\b.*?</script>', '', raw, flags=re.I|re.S)\n    for tag in re.findall(r'<img\\b[^>]*>', raw_markup, re.I):")
exec(compile(src, str(src_path), 'exec'))
