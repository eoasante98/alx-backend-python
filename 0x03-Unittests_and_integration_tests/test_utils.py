#!/usr/bin/env python3
'''
A Unittest class for utils.py
'''


import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''
    Test Case class for access_nested_map
    '''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        function to test access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
        function to test access_nested_map (exception)
        '''
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    '''
    Test cases
    '''

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_class):
        '''
        testing the get_json function
        '''
        mock_class.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''
    Test cases for TestMemoize class
    '''

    def test_memoize(self):
        '''
        testing the memoize function
        '''
        class TestClass:
            '''
            test class
            '''

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                '''
                a_property function
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
