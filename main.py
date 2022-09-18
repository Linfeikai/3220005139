import jieba
import gensim
import re


# 获取论文内的文件内容
def getFileContents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    # 读出来的是以行为元素的一个list 这个while循环把所有的行的内容都放在一个str里面
    while line:
        str = str + line
        line = f.readline()


# 把论文的内容进行分词，过滤特殊符号
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result


# 计算相似度
def calculateSimilarty(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


# def print_hi(name):
#     seg_list = jieba.lcut("我是一个坏人!?")
#     path = r'C:\Users\林霏开\Desktop\readme.txt'
#     f = open(path,'r',encoding='UTF-8')
#     line = f.readlines()
#     print(line)


if __name__ == '__main__':
    path1 = r'C:\Users\林霏开\Downloads\测试文本\orig.txt'
    path2 = r'C:\Users\林霏开\Downloads\测试文本\orig_0.8_add.txt'
    save_path = r'C:\Users\林霏开\Desktop\readme.txt'
    str1 = getFileContents(path1)
    str2 = getFileContents(path2)
    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calculateSimilarty(text1, text2)
    print("The simimarity between the articles you have given is %.4f" % similarity)
    f = open(save_path, 'w', encoding='utf-8')
    f.write("文章相似度：%.4f" % similarity)
    f.close()
