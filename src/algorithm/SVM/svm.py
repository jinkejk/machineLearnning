'''
    author : jinke
    github: https://github.com/jinkejk
    SMO优化算法
    数据集是手写数字数据集
'''

import random
import numpy as np
import os
basePath = os.path.abspath('.')

#加载数据,这里加载的是二维数据testSet.txt
def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

# 在区间0-m内随机选取一个数,且这个数不等于i
def selectJrand(i,m):
    j = i
    while (j == i):
        j = int(random.uniform(0,m))
    return j

# 当数值过大时进行调整
# H: 上界
# L: 下界
def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

# SMO优化算法
# 第一步选取一对alpha_i和alpha_j，选取方法使用启发式方法。
# 第二步，固定除alpha_i和alpha_j之外的其他参数，确定W极值条件下的alpha_i，
# alpha_j可以由alpha_i表示。满足约束条件
# C: 松弛参数
# toler: 容错率,间隔
# maxIter: 最大迭代次数
# 参考公式:http://www.cnblogs.com/jerrylead/archive/2011/03/18/1988419.html
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = np.mat(dataMatIn); labelMat = np.mat(classLabels).transpose()
    b = 0; m,n = np.shape(dataMatrix)
    alphas = np.mat(np.zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        #记录alpha是否已经优化
        alphaPairsChanged = 0
        #对于所有数据向量遍历:选择该向量后,随机选择另外一个向量,组成优化的alpha对
        for i in range(m):
            # fXi是预测的类别(第i个样本): 对应u_i
            fXi = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            # 误差
            Ei = fXi - float(labelMat[i])
            #查看alpha是否满足KKT条件(正间隔和负间隔)
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                #随机算则alpha_j
                j = selectJrand(i,m)
                #第j个样本的预测
                fXj = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                #保存副本
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
                #保障alpha在0-C之间:参考公式
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print ("L==H"); continue
                # eta是alpha_j的最优修改量
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print ("eta>=0"); continue
                # alpha_j的优化公式
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                # alpha_j必须在HL之间
                alphas[j] = clipAlpha(alphas[j],H,L)
                # 改变太小则忽略
                if (abs(alphas[j] - alphaJold) < 0.00001): print ("j not moving enough"); continue
                # 对i修改,修改量和j 相同
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])
                #常数项设置b1和b2
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                #b的更新规则,见博客
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
                print ("iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged))
        #当遍历样本集合之后所有alpha都没变时,才停止循环
        if (alphaPairsChanged == 0): iter += 1
        else: iter = 0
        print ("iteration number: %d" % iter)
    return b,alphas

#分类:计算权值w
def calcWs(alphas,dataArr,classLabels):
    X = np.mat(dataArr); labelMat = np.mat(classLabels).transpose()
    m,n = np.shape(X)
    w = np.zeros((n,1))
    for i in range(m):
        w += np.multiply(alphas[i]*labelMat[i],X[i,:].T)
    return w


#测试
dataArr,labelMat = loadDataSet(basePath + '/testSet.txt')
b, alphas = smoSimple(dataArr, labelMat, 0.6, 0.001, 40)
print(alphas[alphas > 0])

#查看支持向量
for i in range(100):
    if alphas[i] > 0:
        print(dataArr[i], labelMat[i])

#计算w
ws = calcWs(alphas, dataArr, labelMat)

#对第一个点测试一下
dataMat = np.mat(dataArr)
dataMat[0] * np.mat(ws) + b