from unittest import TestCase
from main import calculateSimilarty,getFileContents,filter,testFilePath


'''
    白盒测试法检查程序内部逻辑结构，对所有的逻辑路径进行测试，是一种穷举路径的测试方法
     1. 保证一个模块中的所有独立路径至少被测试一次；
     2. 所有逻辑值均需要测试真（true）和假（false）；两种情况；
     3. 检查程序的内部数据结构，保证其结构的有效性；
     4. 在上下边界及可操作范围内运行所有循环。
'''

class Test(TestCase):
    # def test_calculateSimilarty(self):
    #     text1 = "今天周三，啥时候才能到周五啊？"
    #     text2 = "今天是礼拜三，什么时候周五呢？"
    #     answer = calculateSimilarty(text1,text2)
    #     self.assertEqual(answer,)

    def test_getFileContents_existed(self):
        path = r'C:\Users\林霏开\Downloads\测试文本\ori1.txt'
        contents = getFileContents(path)

        self.assertEqual(contents,'今天周一，周一我觉得我快要死掉了。')
    # def test_getFileContents_notexisted(self):

    def test_filter(self):
        answer = ['今天','我','周三','开心']
        self.assertEqual(answer,filter('今天，我周三开心。'))

    #这是一个测试测试函数的函数，由于时间缘故暂不实现了，逻辑比较简单。
    # def test_testFilePath(self):
if __name__ == '__main__':
    Test.main()