#!/usr/bin/env python
import unittest
from emojiscript import emojify

class EmojiTest(unittest.TestCase):
    def test(self):
        # Should contain all the input words
        emojified = emojify('this is totally lit')
        self.assertIn('this', emojified)
        self.assertIn('is', emojified)
        self.assertIn('totally', emojified)
        self.assertIn('lit', emojified)

if __name__ == '__main__':
    unittest.main()

