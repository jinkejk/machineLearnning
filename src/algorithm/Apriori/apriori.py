'''
    author : jinke
    github: https://github.com/jinkejk
    apriori:算法
'''
import os
basePath = os.path.abspath('.')


#简单数据集
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

# 将数据集中的数据提取
# 返回frozenset的一个列表
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()
    # 创建不可变的set, 存在hash值, python2 不用list函数
    return list(map(frozenset, C1))

# print(createC1(loadDataSet()))

# 计算关联集的支持度,如果它不满足支持度,那么它的超集必定不满足
# minupport: 最小支持度
# Ck: 候选项集列表
# D; 数据集 set 的一个列表
def scanD(dataset, Ck, minSupport):
    # 保存元素出现次数
    ssCnt = {}
    for tid in dataset:
        for can in Ck:
            # 如果是子集
            if can.issubset(tid):
                # 保存单个元素出现次数
                if can not in ssCnt: ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(dataset))
    # 保存满足支持度的元素
    retList = []
    # 保存元素的支持度
    supportData = {}
    for key in ssCnt:
        # 计算支持度
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support

    return retList, supportData

# 这个算法貌似有问题,有缺失
# 将候选集的维数变成k
# k: 需要输出的候选项的长度
# Lk: 候选项集
# 输入{0,1},{0,2},{1,2} 输出{1,2,3}
# 输入{0},{1},{2} 输出{0,1},{0,2},{1,2}
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    # 遍历候选集
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            #分别提取前k - 2 个数
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    # 删除单个不符合支持度的元素
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    # 当候选集中还有对象时
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        #按支持度删选
        Lk, supK = scanD(D, Ck, minSupport)
        # 合并支持度
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


#测试
dataset = loadDataSet()
C1 = createC1(dataset)
C3 = aprioriGen([frozenset({0,1}),frozenset({0,2}),frozenset({1,2}),frozenset({1,3})], 3)
# D = list(map(set, dataset))
# retList, supportData = scanD(D, C1, 0.5)
print(apriori(dataset, 0.5))
