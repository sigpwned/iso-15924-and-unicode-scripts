all: scripts.jsonl scripts.json scripts.min.json scripts.csv

ISO_15924.html:
	curl -o ISO_15924.html 'https://en.wikipedia.org/w/index.php?title=ISO_15924&oldid=1127582355'

scripts.jsonl: ISO_15924.html
	python3 build.py ISO_15924.html > scripts.jsonl

scripts.json: scripts.jsonl
	cat scripts.jsonl | jq -s . > scripts.json

scripts.csv: scripts.json
	echo 'iso_id,iso_number,iso_name,iso_notes,unicode_name,unicode_version,unicode_historic,unicode_notes' > scripts.csv
	cat scripts.jsonl | jq -r '[.iso.id,.iso.number,.iso.name,.iso.notes,.unicode.name,.unicode.version,.unicode.historic,.unicode.notes]|@csv' >> scripts.csv

%.min.json: %.json
	cat $< | jq -c . > $@

clean:
	rm -f *.html *.jsonl *.json *.csv
