'''
    author : jinke
    github: https://github.com/jinkejk
'''
from matplotlib import pyplot
from numpy import *
from numpy.ma import *
import operator
#简单的测试数据
def creatDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# inX 输入样本
def classify0(inX, dataSet, labels, k):
    # shape 显示维数
    dataSetSize = dataSet.shape[0]
    # tile函数 将inX 按行列复制
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # ** 是指数操作
    sqDiffMat = diffMat ** 2
    # 参数1表示按照行求和,0是按列求和
    sqDistance = sqDiffMat.sum(axis=1)
    # 根号
    distance = sqDistance ** 0.5

    # 将元素转换成它在这一行的大小排序索引(从小道大)
    sortedDistanceIndicies = distance.argsort()
    classCount = {}
    # 找出最近的k个样本
    for i in range(k):
        voteILable = labels[sortedDistanceIndicies[i]]
        # 对于该标签样本数 +1
        classCount[voteILable] = classCount.get(voteILable, 0) + 1
    # operator.itemgetter(1): 获取map中的值(第二维数据),它是一个函数
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 读取文件数据
def file2Matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    # 文件行数
    arrayOfLines = len(arrayOLines)
    # arrayOfLines = 1000
    # 特征矩阵
    returnMat = zeros((arrayOfLines, 3))
    classLabelVector = []
    index = 0
    # 解析文件数据
    for line in arrayOLines:
        line = line.strip()  # 去掉末尾换行
        listFromLine = line.split('\t')
        returnMat[index, 0:2] = listFromLine[0:2]
        returnMat[index, 2] = listFromLine[3]
        # 最后一列是label
        classLabelVector.append(int(listFromLine[2]))
        index += 1

    fig = pyplot.figure()
    # 参数控制xyz比例
    ax = fig.add_subplot(111)
    # 10控制点大小
    ax.scatter(returnMat[:, 1], returnMat[:, 2],
               6 * array(classLabelVector), 6 * array(classLabelVector))
    pyplot.show()

    return returnMat, classLabelVector


# 归一化
def autoNorm(dataSet):
    # 0按列
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue
    normalDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normalDataSet = (dataSet - tile(minValue, (m, 1))) / tile(ranges, (m, 1))

    return normalDataSet, ranges, minValue


# 测试
def dataTest():
    returnMat, classLabelVector = file2Matrix('../../data/u.data')
    normMatTrain, rangesTrain, minValsTrain = autoNorm(returnMat)
    datingDataMat, datingLabels = file2Matrix('../../data/u.data.test')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    errorCount = 0.0
    for i in range(m):
        classifierResult = classify0(normMat[i, :], normMatTrain,
                                     classLabelVector, 10)
        print('classifier: %d, the real answer is: %d' % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1
    print('accuracy: %f' % (1 - errorCount / float(m)))

# group, labels = creatDataSet()
# print(classify0([0, 0], group, labels, 3))

# returnMat, classLabelVector = file2Matrix('../../data/u.data')
# print(returnMat)
#
# normalDataSet = autoNorm(returnMat)[0]
# print(len(normalDataSet))
# print(classLabelVector)

# dataTest()
