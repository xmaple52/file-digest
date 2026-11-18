import argparse
import hashlib
import hmac
from pathlib import Path


def digest(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def main():
    parser = argparse.ArgumentParser(description='SHA-256 checksum utility.')
    parser.add_argument('file')
    parser.add_argument('--expect', help='Expected 64-character hexadecimal SHA-256')
    args = parser.parse_args()
    if args.expect and (len(args.expect) != 64 or any(c not in '0123456789abcdefABCDEF' for c in args.expect)):
        parser.error('--expect must be a 64-character hexadecimal hash')
    try:
        actual = digest(args.file)
    except OSError as error:
        parser.exit(2, f'Error: {error}\n')
    print(actual)
    if args.expect:
        match = hmac.compare_digest(actual, args.expect.lower())
        print('MATCH' if match else 'MISMATCH')
        return 0 if match else 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
