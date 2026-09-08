from pathlib import Path
import re

files = [Path('index.html'), Path('blog/index.html')]
files += list(Path('.').glob('*-tanger/index.html'))

for path in files:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    # Homepage section titles
    text = text.replace('font-weight:300;\n  line-height:1.14;', 'font-weight:600;\n  line-height:1.14;')

    # Service/blog page H2 rules
    text = re.sub(r'(\.content h2\{[^}]*?font-weight:)350([;}])', r'\g<1>600\2', text)
    text = re.sub(r'(h2\{[^}]*?font-weight:)400([;}])', r'\g<1>600\2', text)
    text = re.sub(r'(h2\{[^}]*?font-weight:)500([;}])', r'\g<1>600\2', text)

    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'Updated {path}')
