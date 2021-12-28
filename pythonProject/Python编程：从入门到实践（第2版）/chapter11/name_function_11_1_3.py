# Author:D.辉
# Place：哈工深
# Time：2021/08/19 21:02
# 11.1.3 未通过的测试


import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像janis joplin 这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
