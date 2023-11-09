# ISO 15924 and Unicode Script Dataset

[ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) is an international standard for the various and sundry [writing systems](https://en.wikipedia.org/wiki/Writing_system) of Earth and their associated [Unicode](https://en.wikipedia.org/wiki/Unicode) [scripts](https://en.wikipedia.org/wiki/Script_%28Unicode%29).

## The Need

I needed a trustworthy dataset in machine-readable format(s) with the following data attributes:

1. Script ID (e.g., `Latn`)
2. Unicode Script name, if exists (e.g., `Latin`)
3. Whether or not each script is ancient/historical (e.g., Bassah Vah)

## The Dataset

There were many good options, like [wooorm/iso-15924](https://github.com/wooorm/iso-15924), but none that matched all my needs. (Or at least none that I could find.) So [I made one myself](https://xkcd.com/927/). It attempts to address the following needs:

* Free -- This dataset is released under the Creative Commons CC0 license.
* All ISO 15924 codes -- All ISO codes in the standard are in this document, and vice-versa.
* All Unicode scripts -- All Unicode scripts in the standard are in this document, and vice-versa.
*  Clear provenance -- Data is pulled from [`https://en.wikipedia.org/wiki/ISO_15924`](https://en.wikipedia.org/wiki/ISO_15924)
* Easy-to-use -- Data is available in simple JSON and CSV formats.

These data should help users to plan, build, and implement support for Unicode scripts quickly and easily.

## The Data

The dataset is comprised of the following data files:

* `scripts.jsonl` -- This is the "master" file. All other files are generated from this file, either directly or indirectly. It contains data parsed from  `https://en.wikipedia.org/wiki/ISO_15924`. There is [one JSON record per line](https://jsonlines.org/).
* `scripts.json` -- This is the same as `scripts.jsonl`, but all values are wrapped in one top-level array.
* `scripts.min.json` -- This is the same as `scripts.json`, but minified.
* `scripts.csv` This is the same as `scripts.jsonl`, but the file format in CSV as opposed to JSON.

### Downloading

You can get the data a few different ways:

* Download the CSV files from this repo
* Download the CSV, JSON, and JSONL files from [the releases on this repo](https://github.com/sigpwned/names-by-country-dataset/releases)
* Clone this repo and run `make`

## The License

The data is available under the Creative Commons CC0 license. This places the data into the public domain, so you can do whatever you'd like with it, but I'd appreciate a note if you find it useful! You can open a ticket to say hello 👋 if nothing else.

## Maintenance

I watch the source Wikipedia page and will update this project when there is a relevant change. Release versioning will follow [semver](https://semver.org/). Because this project straddles two different standards, both with their own different versioning schemes, the version format (`YYYYMMDD.PATCH`) is based on release dates as opposed to versions from either standard. Updates to either standard will trigger a release, and release notes will indicate this.

For example, a (hypothetical) update to ISO 15924 on July 26, 2023 would trigger a major release versioned `20230726.0`. A non-breaking minor release (e.g., to fix a typo) on July 28, 2023 would be versioned `20230726.1`, indicating that users currently on `20230726.0` may safely update to `20230726.1`. A new (hypothetical) update to Unicode on July 29, 2023 would trigger a new major release versioned `20230729.0`. And so on.

It's worth nothing that both ISO 15924 and Unicode scripts are fairly stable at this point. 
