from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

if 'Consultations en français, arabe, anglais et espagnol' not in s:
    anchor = '''          <li>\n            <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>\n            Un suivi personnalisé, du premier rendez-vous au contrôle\n          </li>'''
    insert = anchor + '''\n          <li>\n            <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>\n            Consultations en français, arabe, anglais et espagnol\n          </li>'''
    if anchor not in s:
        raise SystemExit('Practitioner facts anchor not found')
    s = s.replace(anchor, insert, 1)

if '"knowsLanguage": ["français", "arabe", "anglais", "espagnol"]' not in s:
    anchor = '    "jobTitle": "Chirurgienne-dentiste",\n'
    if anchor not in s:
        raise SystemExit('Practitioner schema anchor not found')
    s = s.replace(anchor, anchor + '    "knowsLanguage": ["français", "arabe", "anglais", "espagnol"],\n', 1)

path.write_text(s, encoding='utf-8')
