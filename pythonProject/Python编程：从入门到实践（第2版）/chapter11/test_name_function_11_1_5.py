# Author:D.辉
# Place：哈工深
# Time：2021/08/19 22:02
# 11.1.5 添加新测试

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像janis joplin 这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
