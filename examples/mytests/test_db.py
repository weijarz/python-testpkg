import unittest

from . import db


class TestDB(unittest.TestCase):

    def test_in_db(self):
        self.assertIn(3, db)

    def test_index(self):
        self.assertEqual(db.index(2), 1)
