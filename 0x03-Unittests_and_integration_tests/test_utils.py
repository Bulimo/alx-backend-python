#!/usr/bin/env python3
"""
Module test_utils
Module that implements class TestAccessNestedMap, TestGetJson, and TestMemoize
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Class TestAccessNestedMap that inherits from unittest.TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected):
        """Test for access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """Test for access nested map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class TestGetJson that inherits from unittest.TestCase"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_payload):
        """Test for get json"""
        config = {'return_value.json.return_value': expected_payload}
        with patch('requests.get', **config) as mock_get:
            result = get_json(url)
            self.assertEqual(result, expected_payload)
            mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class TestMemoize that inherits from unittest.TestCase"""

    def test_memoize(self):
        """Method to test memoizing a function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
