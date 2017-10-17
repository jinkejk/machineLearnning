'''
    author : jinke
    github: https://github.com/jinkejk
    朴素贝叶斯分析文档
'''
from math import *
#创建简单测试数据
from numpy import ones, zeros, array


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    label = [0,1,0,1,0,1]
    return postingList, label

#创建这些文档中不重复出现的词
def createVocabList(dataSet):
    vocabSet = set([])  #创建set
    for document in dataSet:
        #求集合的并集
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

#提取特征向量(0-1特征)
#vocabList : 词汇表
#inputSet : 某个输入的特征
def setOfWords2Vec(vocabList, inputSet):
    #创建一个0向量
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            #在词汇表中出现的单词置为1
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

#训练朴素贝叶斯其实是计算各个属性出现的概率
#二分类
#trainCategory: 类别标签
def trainNB(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    #防止出现次数为0, 相乘的时候乘积会变0
    p0Num = ones(numWords); p1Num = ones(numWords)
    #总单词数
    p0Denom = 2; p1Denom = 2
    for i in range(numTrainDocs):
        #这里是二分类
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    #防止下溢,因为乘数太小(这里相当于ln)
    #这里概率相乘可以变成相加, ln(a*b) = ln(a) + ln(b)
    p1Vect = [log(x) for x in p1Num/p1Denom]
    p0Vect = [log(x) for x in p0Num/p0Denom]
    return p0Vect, p1Vect, pAbusive

#二分类
#vec2Classify: 要分类的向量
#p0Vec: 第0类的属性在其类别下的概率(p(i/c))
#pClass1 : 第1类的概率(p(c1))
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    #计算属于各个类别的概率(p(w)是相同的,不用除)
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

#对单词计数,生成新的特征不是0-1特征
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

#对测试的一个分装
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

#测试
# postingList, label = loadDataSet()
# myVocabList = createVocabList(postingList)
# trainMat = []
# for postingDoc in postingList:
#     trainMat.append(setOfWords2Vec(myVocabList, postingDoc))
#
# print(trainNB(trainMat, label))

# testingNB()
