# This program scrapes data from the Wikipedia page https://en.wikipedia.org/wiki/Script_(Unicode)
# It was built and tested against version https://en.wikipedia.org/w/index.php?title=Script_(Unicode)&oldid=1110671885

from bs4 import BeautifulSoup
from json import dumps
from re import compile
from sys import argv

REFERENCES = compile(r"\[[iv]*\]")
PROLOG = compile(r"ZZ[\u2014]")

def sanitize(s):
    for regex in [ PROLOG, REFERENCES ]:
        s = regex.sub("", s)
    s = s.strip()
    return s

wikipage = argv[1]

soup = None
with open(wikipage, "rb") as file:
    soup = BeautifulSoup(file, "html.parser")

header = soup.find(id="List_of_codes").parent
table = header.find_next("table")
for row in table.select("tr[id]"):
    cells = row.find_all("td", recursive=False)
    iso_id = cells[0].text.strip()
    iso_number = cells[1].text.strip()
    iso_formal_name = cells[2].text.strip()

    unicode = None
    iso_notes = None
    has_unicode = "colspan" not in cells[4].attrs
    if has_unicode:
        unicode_alias = cells[4].text.strip()
        unicode_version = cells[5].text.strip()
        unicode_notes = sanitize(cells[7].text)
        unicode_historic = "Ancient/historic" in unicode_notes
        if unicode_notes == "":
            unicode_notes = None
        unicode = { "name": unicode_alias, "version": unicode_version, "notes": unicode_notes, "historic": unicode_historic }
    else:
        unicode = None
        iso_notes = sanitize(cells[4].text)
        if iso_notes == "":
            iso_notes = None
        
    iso = { "id": iso_id, "number": iso_number, "name": iso_formal_name, "notes": iso_notes }
    
    print(dumps({"iso":iso, "unicode":unicode}))
