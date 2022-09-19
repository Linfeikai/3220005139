from unittest import TestCase
from main import getFileContents

class Test(TestCase):
    def test_get_file_contents(self):
        path1 = r'C:\Users\林霏开\Downloads\测试文本\orig.txt'
        str1 = getFileContents(path1)
        self.fail()

if __name__ == '__main__'
    Test.main()