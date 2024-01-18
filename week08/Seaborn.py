#pandas是Python语言的一个扩展程序库，用于数据分析
#可以从各种文件格式比如csv,json,sql,microsoft excel导入数据
# 还可以对各种数据进行运算操作，比如归并，成形，选择，还有数据清洗和加工等
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 
iris = load_iris()
#数据集
iris_data = iris.data
#数据集的标签
iris_labels = iris.target
iris_feature_names = iris.feature_names


iris_df = pd.DataFrame(data=iris_data,columns=iris_feature_names)
iris_df['Species'] = iris_labels
#设置图形主题风格
sns.set(style='whitegrid')


#散点图
sns.pairplot(iris_df,hue="Species",markers=["o","s","D"])
plt.suptitle("Pairplot of Iris Dataset",y=1.02)
plt.show()


#箱线图 Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(x="Species",y="sepal length(cm)",data=iris_df)
plt.title("Boxplot of Sepal Length by Species")
plt.show()


#直方图Histogram
plt.figure(figsize=(10,6))
sns.hisplot(iris_df,x="petal length(cm)",hue="Species",element="step",stat="density",common_norm="False")
plt.title("Histogram of Petal Length by Species")
plt.show()