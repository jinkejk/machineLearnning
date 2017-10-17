'''
    author : jinke
    github: https://github.com/jinkejk
    NB测试,垃圾邮件分类
'''
import random

from src.algorithm.NaiveBayes.Naivebayes import *
import os
basePath = os.path.abspath('.')
#从邮件中提取单词
def textParse(bigString):
    import re
    #使用非单词字符分割
    listOfTokens = re.split(r'\W*', bigString)
    #转化成小写,且屏蔽空格和标点
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

#测试代码
def spamTest():
    #读取文件
    docList=[]; classList = []; fullText =[]
    for i in range(1,22):
        spam = open(basePath + '/email/spam/%d.txt' % i, encoding='GBK')
        wordList = textParse(spam.read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        ham = open(basePath +'/email/ham/%d.txt' % i,encoding='GBK')
        wordList = textParse(ham.read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    #创建字典
    vocabList = createVocabList(docList)
    #创建测试数据
    trainingSet = list(range(40)); testSet=[]
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]; trainClasses = []

    #训练数据
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print ("classification error",docList[docIndex])
    print ('the error rate is: ',float(errorCount)/len(testSet))
    #return vocabList,fullText

spamTest()