'''
    author : jinke
    github: https://github.com/jinkejk
    k-means
'''
from numpy import *
import os

#加载数据
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataMat.append(fltLine)
    return array(dataMat)

#计算欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

#随机初始化聚类中心,  k个
def randCent(dataSet, k):
    #特征维数
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    # 随机初始化中心, 但是这个中心的元素值,必须要在最大和最小值之间
    for j in range(n):
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        # 一次创建k个值
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

#distMeas: 距离函数
#createCent: 初始化中心函数
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    #这里第一列保存类的索引,第二列保存到中心的误差
    clusterAssment = mat(zeros((m,2)))
    #初始化中心
    centroids = createCent(dataSet, k)
    #结束循环的条件
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        #遍历所有点,重新分配类别
        for i in range(m):
            # 初始化为无穷大
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            #若类别变了
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            #保存一下类别和距离的平方
            clusterAssment[i,:] = minIndex,minDist**2
        print (centroids)
        #更新聚类中心
        for cent in range(k):
            #nonzero: 返回非0样本的索引
            #找到该类的样本
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

#测试
dataset = loadDataSet(os.path.abspath('.') + '/testSet.txt')
kMeans(dataset, 5)