import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA 

#读取数据（）
df_wine = pd.read_csv('Python\data\wine.data',header=None)

#设置列索引
df_wine.columns=['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue',
                   'OD280/OD315 of diluted wines', 'Proline']

#数据维度
#df_wine.shape()

#每一类数据包含的样本个数
df_wine['Class label'].value_counts()

#打印输出前五行
df_wine.head()

#数据集设置：X为样本特征数据，y为目标数据，即标注结果(iloc通过行号来读取数据)
X,y = df_wine.iloc[:,1:],df_wine.iloc[:,0]

#数据集划分：将数据集分为训练集和测试集（训练集是0.7，测试集是0.3）
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,stratify=y,random_state=0)

#实例化，右边本身是一个对象，左侧创建一个实例
sc = StandardScaler()

#对数据集进行标准化（一般情况下我们在训练集中进行均值和方差的计算，直接在测试集中使用）
X_train_std = sc.fit_transform(X_train)
X_test_std =sc.transform(X_test)

#使用sklearn实现PCA
#pca实例化,保留所有特征
pca = PCA()

#特征提取
X_train_pca = pca.fit_transform(X_train_std)
#特征值结果
pca.explained_variance_ratio_

#特征值绘制
#绘制图像
'''plt.figure()
plt.bar(range(1,14),pca.explained_variance_ratio_,alpha=0.5,
        label='Eigenvalue distribution') #特征值分布
plt.step(range(1,14),np.cumsum(pca.explained_variance_ratio_),where='mid',
         label='Cumulative eigenvalues') #累计特征值分布
plt.ylabel('Eigenvalue ratio') #特征值比例
plt.xlabel('Feature index') #特征值索引
plt.legend(loc='best')  '''

#压缩到二维特征
pca=PCA(n_components=2)

#对训练数据进行处理
X_train_pca = pca.fit_transform(X_train_std)

#特征值结果(只保留两个特征)
print(pca.explained_variance_ratio_)

#对测试集数据进行处理
X_test_pca = pca.transform(X_test_std)

#特征降维结果后结果展示
colors = ['r','b','g']
markers = ['s','x','o']
for l,c,m in zip(np.unique(y_train),colors,markers):
  #按照样本的真实值进行展示
  plt.scatter(X_train_pca[y_train==1,0],
              X_train_pca[y_train==1,1],
              c=c,label=1,marker=m)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()