from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Canonical + crawl directives
if '<link rel="canonical" href="https://centredentairevenezuela.com/">' not in s:
    anchor = '<meta name="description" content="Centre Dentaire Venezuela à Tanger : implantologie, orthodontie, esthétique dentaire et soins conservateurs par Dr Majda Laasraoui. Une approche douce, précise et personnalisée.">'
    replacement = anchor + '\n<link rel="canonical" href="https://centredentairevenezuela.com/">\n<meta name="robots" content="index, follow, max-image-preview:large">'
    if anchor not in s:
        raise SystemExit('Meta description anchor not found')
    s = s.replace(anchor, replacement, 1)

if '<meta property="og:url" content="https://centredentairevenezuela.com/">' not in s:
    anchor = '<meta property="og:description" content="Une approche douce, précise et personnalisée pour des soins dentaires d’exception, à Tanger.">'
    replacement = anchor + '\n<meta property="og:url" content="https://centredentairevenezuela.com/">'
    if anchor not in s:
        raise SystemExit('OG description anchor not found')
    s = s.replace(anchor, replacement, 1)

schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "@id": "https://centredentairevenezuela.com/#dentist",
  "url": "https://centredentairevenezuela.com/",
  "name": "Centre Dentaire Venezuela",
  "alternateName": "Cabinet dentaire Dr Majda Laasraoui",
  "description": "Cabinet dentaire à Tanger proposant des soins dentaires généraux, chirurgie dentaire, dentisterie esthétique, implantologie, endodontie et parodontologie.",
  "image": "https://centredentairevenezuela.com/assets/images/hero-poster-cabinet-dentaire-venezuela-tanger.webp",
  "logo": "https://centredentairevenezuela.com/assets/images/logo-centre-dentaire-venezuela.webp",
  "telephone": "+212531112127",
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+212531112127",
      "contactType": "Cabinet dentaire"
    },
    {
      "@type": "ContactPoint",
      "telephone": "+212771158018",
      "contactType": "WhatsApp",
      "url": "https://wa.me/212771158018"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "4ème étage n°74, Immeuble Venezuela, 89 Rue Moussa Ben Noussair",
    "addressLocality": "Tanger",
    "postalCode": "90000",
    "addressCountry": "MA"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 35.7781833,
    "longitude": -5.8165155
  },
  "areaServed": {
    "@type": "City",
    "name": "Tanger"
  },
  "hasMap": "https://share.google/NQdfjEYv9MC4431Lz",
  "medicalSpecialty": "Dentistry",
  "employee": {
    "@type": "Person",
    "name": "Dr Majda Laasraoui",
    "jobTitle": "Chirurgienne-dentiste",
    "alumniOf": {
      "@type": "CollegeOrUniversity",
      "name": "CEU Cardinal Herrera University"
    }
  },
  "sameAs": [
    "https://www.instagram.com/centre.dentaire.venezuela/",
    "https://share.google/NQdfjEYv9MC4431Lz"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Soins dentaires",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Soins dentaires généraux et détartrage"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Chirurgie dentaire et extractions"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dentisterie esthétique : blanchiment et facettes"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Implants dentaires et implantologie"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Endodontie et traitement de canal"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Parodontologie et soins des gencives"}}
    ]
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Wednesday", "Friday"], "opens": "09:30", "closes": "17:30"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday", "Thursday"], "opens": "09:30", "closes": "13:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday", "Thursday"], "opens": "15:00", "closes": "18:30"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "14:00"}
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "bestRating": "5",
    "reviewCount": "50"
  }
}
</script>'''

pattern = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)
s, count = pattern.subn(schema, s, count=1)
if count != 1:
    raise SystemExit(f'Expected exactly one JSON-LD block, found {count}')

path.write_text(s, encoding='utf-8')
