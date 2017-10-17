'''
    author : jinke
    github: https://github.com/jinkejk
    #使用lenses.txt预测
'''

from src.algorithm.DecisionTree.id3 import *

fr = open(basePath + '/lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
print('前5个数据: ', lenses[1:5])
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = createTree(lenses, lensesLabels)
storeTree(lensesTree, basePath + '/tree2.model')
print(lensesTree)



# #测试数据集的熵
# dataSet, labels = createDataSet()
# storeTree(createTree(dataSet, labels), basePath + '/tree.model')
# #labels是list变量,传地址,会变
# print(classify(readTree(basePath + '/tree.model'), createDataSet()[1], [0, 0]))
