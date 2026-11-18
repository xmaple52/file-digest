# file-digest

Compute and verify SHA-256 hashes without loading entire files into memory.

Python 3.10+ · standard library only.

## Quick start

```sh
python file_digest.py README.md
```

Use `--expect HASH` to compare a known checksum. Exit codes: 0 success/match, 1 mismatch, 2 input error. Reads in 1 MiB chunks. A checksum detects differences; it does not prove a file is trustworthy. Read-only: the input file is never changed.

## Tests

```sh
python -m unittest discover -s tests -v
```
