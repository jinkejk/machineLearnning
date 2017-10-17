'''
    author : jinke
    github: https://github.com/jinkejk
'''
import math

import operator
import os
basePath = os.path.abspath('.')

#创建简单的测试数据
def createDataSet():
    dataSet = [[0,0,'maybe'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing', 'plippers']
    return dataSet, labels

#计算整个数据集香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    #保存个各类样本数量
    labelCounts = {}
    for featVec in dataSet:
        #最后一个变量是标签
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        #计算熵
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * math.log(prob, 2)

    return shannonEnt

#划分数据集
#axis: 划分数据集的特征索引
#value: 划分特征值
#函数返回的是,在dataSet中特征等于value的数据集(去除了axis特征)
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            #axis索引的元素删了
            reduceFeatVec = featVec[:axis]
            # 获取后半部分,extend和append差别:append保留自己的格式(数组)
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

#选择信息增益最大的特征为分割特征
def chooseBestFeatureToSplit(dataSet):
    #特征维数,最后一位是标签
    numFeatures = len(dataSet[0]) - 1
    #数据集信息熵
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        #获取列的所有元素
        featList = [example[i] for example in dataSet]
        #去重
        uniqueVals = set(featList)
        newEntropy = 0.0
        #对每个值求信息熵增益
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            #该属性出现的概率,乘该属性feature(除去了这个属性)的熵
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#当数据集处理完所有的属性后,依旧没能分开该节点的类
#则采用多少表决的方式: 使用该类中最多的类为该节点的类别
def majorityCnt(classList):
    #一个map
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

#labels: 属性的描述不是分类标签
#使用map保存
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    #类别完全相同时,返回
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #所有属性都分割完成了
    if len(dataSet[0]) == 1:
        #取出现最多的那个为标签
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    #使用map保存tree
    myTree = {bestFeatLabel:{}}
    #删掉选中的属性
    del(labels[bestFeat])
    #获取该属性的值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    #递归划分数据集
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),
                                                  subLabels)
    return myTree

#使用决策树分类
#模型都是dict类
def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    #获取根节点的子树
    secondDict = inputTree[firstStr]
    #第一个节点的属性索引值(也就是划分特征的索引值)
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        #若划分特征相等
        if testVec[featIndex] == key:
            #若含有子树
            if type(secondDict[key]).__name__=='dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else: classLabel = secondDict[key]
    return classLabel

#存储模型
def storeTree(inputTree, fileName):
    #序列化工具pickle,默认是二进制存储
    import pickle
    fw = open(fileName, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

#读取模型
def readTree(fileName):
    import pickle
    fr = open(fileName, 'rb')
    return pickle.load(fr)

