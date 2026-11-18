import hashlib
import tempfile
import unittest
from pathlib import Path
from file_digest import digest

class DigestTest(unittest.TestCase):
    def test_empty_and_binary(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)/'data'
            for data in [b'', b'hello', bytes(range(256))*10000]:
                p.write_bytes(data)
                self.assertEqual(digest(p), hashlib.sha256(data).hexdigest())
