'''
    author : jinke
    github: https://github.com/jinkejk
    KNN进行手写数字识别, 特征为像素点输入
'''

from os import listdir
from src.algorithm.KNN.KNN import *
import os
basePath = os.path.abspath('.')
#图像转向量
def image2Vector(fileName):
    returnVector = zeros((1, 1024))
    fr = open(fileName)
    for i in range(32):
        #自动换到下一行
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0, i * 32 + j] = int(lineStr[j])
    return returnVector

def handWritingClassTest():
    hwlabels = []
    trainingFileList = listdir(basePath + '/KNN/trainingDigits/')
    m = len(trainingFileList)

    #获取trainingMat
    trainMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwlabels.append(classNumStr)
        trainMat[i, :] = image2Vector(basePath + '/KNN/trainingDigits/%s' % fileNameStr)

    testFileList = listdir(basePath + '/KNN/testDigits/')
    erroCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorTest = image2Vector(basePath + '/KNN/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorTest, trainMat, hwlabels, 3)
        print('classifier: %d, the real answer: %d' % (classifierResult, classNumStr))
        if classifierResult != classNumStr: erroCount += 1

    print('accuracy: %f' % (1 - erroCount/mTest))

#测试
handWritingClassTest()