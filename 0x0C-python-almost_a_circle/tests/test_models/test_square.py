#!/usr/bin/python3

"""This module contains `TestSquare` class."""


import contextlib
from io import StringIO
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for `Square` class"""

    def test_sqauer(self):
        """It should create a `Square`"""

        s = Square(3)
        self.assertIsInstance(s, Square)

    def test_id(self):
        """It should create a `Square` with id == 5"""

        s = Square(3, id=5)
        self.assertEqual(s.id, 5)

    def test_properties(self):
        """It should have all properties set on creation"""

        s = Square(10, 5, 5, id=2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

    def test_no_args(self):
        """It should fail when no argument is passed during creation"""

        with self.assertRaises(TypeError):
            Square()

    def test_zero_size(self):

