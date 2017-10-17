'''
    author : jinke
    github: https://github.com/jinkejk
    使用梯度上升法,求表达式的最大值
'''

#加载数据,二维特征
import random

from numpy import mat, shape, ones, exp, array, arange, ndarray


def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        #1.0 是x0, 对应w0
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

#sigmod 函数
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

#梯度上升
#alpha: 学习率
#maxCycle: 迭代次数
def gradAscent(dataMatIn, classLabels, alpha, maxCycle):
    dataMatrix = mat(dataMatIn)
    #标签转置一下 n*1
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    weights = ones((n, 1))
    for k in range(maxCycle):
        #m个样本的预测值error
        h = sigmoid(dataMatrix * weights)
        error = h - labelMat
        print('%d iteration error: %f' % (k, sum(abs(error))))
        #梯度公式(这里的代价函数是误差平方)
        weights = weights - alpha * dataMatrix.transpose() * error / m

    print('weights: ', weights)
    return weights

#随机梯度下降法
#随机选取一个样本计算梯度,更新w
def stocGradAscent1(dataMatrix, classLabels, numIter):
    m,n = shape(dataMatrix)
    weights = ones((n, 1))
    for j in range(numIter):
        dataIndex = list(range(m))
        #对于随机样本更新w, alpha不断减小
        for i in range(m):
            alpha = 4 / (1.0+j+i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            temp = dataIndex[randIndex]
            tt = dataMatrix[temp]
            h = sigmoid(mat(tt) * mat(weights))
            error = h - classLabels[dataIndex[randIndex]]
            #使用一个随机样本更新w
            weights = weights - array(alpha * error * dataMatrix[dataIndex[randIndex]]).transpose()
            del(dataIndex[randIndex])
        print('%d iteration error: %f' % (j, sum(abs(error))))
    return weights

#分类
def classifyVector(inX, weights):
    b = [weight[0] for weight in weights]
    a = array(inX) * array(b)
    prob = sigmoid(sum(a))
    if prob > 0.5: return 1.0
    else: return 0.0
#测试
dataMat,labelMat = loadDataSet()
weights = stocGradAscent1(dataMat, labelMat, 100)

print(classifyVector([1, -1.395634,	4.662541], weights))