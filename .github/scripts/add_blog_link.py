from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
needle = '<a href="#localisation">Notre localisation</a>'
replacement = needle + '\n        <a href="/blog/">Blog</a>'
count = text.count(needle)
if count < 2:
    raise SystemExit(f'Expected at least 2 navigation occurrences, found {count}')
text = text.replace(needle, replacement)
path.write_text(text, encoding='utf-8')
print(f'Added Blog link after {count} navigation occurrences')
