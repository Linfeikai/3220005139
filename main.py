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
    return str

# 把论文的内容进行分词，过滤特殊符号
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        # 只有属于26个字母和/或汉字的才属于要识别的内容，去除其它引号/分号/换行字符等
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result


# 计算相似度的第一种方法（词袋法）
def calculateSimilarty(text1, text2):
    texts = [text1, text2]
    #为语料库中出现的所有单词分配了唯一的一个整数id
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

#计算相似度的第二种方法(Word2Vec) 这个方法暂时未实现 因为我的电脑下载不了word2vec这个库
#def calculate_similarity(text1,text2):


if __name__ == '__main__':
    path1 = r'C:\Users\林霏开\Downloads\测试文本\ori1.txt'
    path2 = r'C:\Users\林霏开\Downloads\测试文本\ori2.txt'
    save_path = r'C:\Users\林霏开\Desktop\readme.txt'
    str1 = getFileContents(path1)
    str2 = getFileContents(path2)
    #str1和str2是字符串数据类型
    text1 = filter(str1)
    text2 = filter(str2)
    #text1和text2是两个列表，每个列表里的元素都是划分出来的词
    similarity = calculateSimilarty(text1, text2)
    print("The simimarity between the articles you have given is %.4f" % similarity)
    f = open(save_path, 'w', encoding='utf-8')
    f.write("文章相似度：%.4f" % similarity)
    f.close()
