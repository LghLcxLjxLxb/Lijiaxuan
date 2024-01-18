from pylab import *
import matplotlib.pyplot as plt
#是python中的机器学习库，建立在numpy、scipy、matplotlib等数据科学包的基础之上，
#涵盖了机器学习中的样例数据、数据预处理、模型验证、特征选择、分类、回归、聚类、降维等几乎所有环节
#load_iris是鸢尾花数据集
from sklearn.datasets import load_iris
iris=load_iris()
data=iris.data
#目标集
target=iris.target 
feature_names=iris.feature_names



#散点图
# 设置图形大小，分别是宽和高
plt.figure(figsize=(12,6))
for i in range(3):
  plt.scatter(data[target==i,0],data[target==i,1],label=f"Class {i}")
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('Scatter Plot of Iris Dataset')
#给图像加图例
plt.legend()
plt.show() 



#箱线图
plt.figure(figsize=(8,6))
plt.boxplot([data[target==i,2] for i in range(3)],
            labels=[f'Class{i}' for i in range(3)])
plt.xlabel('Classes')
plt.ylabel(feature_names[2])
plt.title('Box Plot of Sepal Length by Class')
plt.show()



#直方图
plt.figure(figsize=(8,6))
for i in range(3):
  plt.hist(data[target==i,3],bins=20,alpha=0.5,label=f'Class{i}')
plt.xlabel(feature_names[3])
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width by Class')
plt.legend()
plt.show()