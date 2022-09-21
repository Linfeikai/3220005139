import sys
import jieba
import gensim
import re
from datetime import datetime
import argparse
import os

#检测文件路径是否正确以及是否非空
def testFilePath(path,num):
    if(num == 0):
        if(os.path.isfile(path)):
            if(os.path.getsize(path) != 0):
                return path
            else:
                print('你输入的第一个文件是空的，请重新输入。感谢您的使用！')
                sys.exit()
        else:
            print('你输入的第一个文件路径不存在。请重新输入。感谢您的使用！')
            sys.exit()
    elif(num == 1):
        if(os.path.isfile(path)):
            if(os.path.getsize(path) != 0):
                return path
            else:
                print('你输入的第二个文件是空的，请重新输入。感谢您的使用！')
                sys.exit()
        else:
            print('你输入的第二个文件路径不存在。请重新输入。感谢您的使用！')
            sys.exit()
    elif(num == 2):
        if(os.path.isfile(path)):
            return path
        else:
            workingPath = os.getcwd()
            filePath = workingPath + "\\" + "save.txt"
            file = open("save.txt", "w", encoding="utf8")  # 指定文件名和保存路径、文件操作类型、编码
            file.write("文章查重检测记录")  # 写入内容
            file.close()  # 关闭操作对象
            print('结果输出路径不存在。将把结果储存在当前工作目录下的”save.txt“的文件。')
            return filePath








# 获取论文内的文件内容


def getFileContents(path):
    str = ''
    with open(path, mode='r', encoding='UTF-8') as f:
        line = f.readline()
        # 读出来的是以行为元素的一个list 这个while循环把所有的行的内容都放在一个str里面
        while line:
            str = str + line
            line = f.readline()

    return str


# 把论文的内容进行分词，过滤特殊符号
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        # 只有属于26个字母和/或汉字的才属于要识别的内容，利用正则表达式去除其它引号/分号/换行字符等
        if (re.match(u"[a-zA-Z\d\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result


# 计算相似度的第一种方法（词袋模型）
def calculateSimilarty(text1, text2):
    texts = [text1, text2]
    # 通过输入文本生成语料库
    dictionary = gensim.corpora.Dictionary(texts)
    # 得到语料中每一篇文档对应的稀疏向量（这里是bow向量）;向量的每一个元素代表了一个word在这篇文档中出现的次数
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 用待检索的文档向量初始化一个相似度计算的对象
    index = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    # 计算余弦相似度
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = index[test_corpus_1][1]
    return cosine_sim


# 计算相似度的第二种方法(Word2Vec) 这个方法暂时未实现 因为我的电脑下载不了word2vec这个库
# def calculate_similarity(text1,text2):


if __name__ == '__main__':
    #测试时为固定路径
    # path1 = r'C:\Users\林霏开\Downloads\测试文本\orig.txt'
    # path2 = r'C:\Users\林霏开\Downloads\测试文本\orig_0.8_add.txt'
    # save_path = r'C:\Users\林霏开\Desktop\save.txt'
    #命令行输入
    # path1 = sys.argv[1]
    # path2 = sys.argv[2]
    # save_path = sys.argv[3]
    #换了一种命令行输入的方法
    parser = argparse.ArgumentParser(description='请依次传入要查重的第一份文件路径、第二份文件路径、结果保存路径（以空格隔开）')
    parser.add_argument('param', type=str, nargs='+', help='参数')
    args = parser.parse_args()
    path1 = args.param[0]
    path2 = args.param[1]
    save_path = args.param[2]

    path1 = testFilePath(path1,0)
    path2 = testFilePath(path2,1)
    save_path = testFilePath(save_path,2)

    #这里的前提是 两个文件都要能打开，而且有内容
    str1 = getFileContents(path1)
    str2 = getFileContents(path2)
    # str1和str2是字符串数据类型
    text1 = filter(str1)
    text2 = filter(str2)
    # text1和text2是两个列表，每个列表里的元素都是划分出来的词
    similarity = calculateSimilarty(text1, text2)
    # print("The simimarity between the articles you have given is %.4f" % similarity)
    NowOnTxt = datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S')
    time = str(NowOnTxt)
    f = open(save_path, 'a', encoding='utf-8')
    f.write("\n检测时间：%s\n文章一来源：%s\n文章二来源：%s\n 相似度：%.4f\n\n\n" % (time, path1, path2, similarity))
    f.close()
