#导入必要的库
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#font = FontProperties(frame='/System/Library/Fonts/STHeiti Light.ttc',size=14)

#读取数据
data = pd.read_csv('Python\data\github_bot_processed_data.csv')

#去除数据“created_at” and "updated_at"
data = data.drop(['created_at','updated_at','bio'],axis=1)

#将文本型数据转化为数值型数据
data['label']=data['label'].apply(lambda x:1 if x=='Human' else 0)
data['site_admin']=data['site_admin'].apply(lambda x:1 if x else 0)
data['company']=data['company'].apply(lambda x:1 if x else 0)
data['blog']=data['blog'].apply(lambda x:1 if x else 0)
data['location']=data['location'].apply(lambda x:1 if x else 0)
data['hireable']=data['hireable'].apply(lambda x:1 if x else 0)
data['site_admin']=data['site_admin'].apply(lambda x:1 if x else 0)

#标准化处理
data['public_repos']=(data['public_repos']-np.mean(data['public_repos']))/np.std(data['public_repos'])
data['public_gists']=(data['public_gists']-np.mean(data['public_gists']))/np.std(data['public_gists'])
data['followers']=(data['followers']-np.mean(data['followers']))/np.std(data['followers'])
data['following']=(data['following']-np.mean(data['following']))/np.std(data['following'])

#计算相关系数
corr = data.corr()
corr = corr[['label']]
corr = corr.drop('label')

#取绝对值排序
corr = corr.apply(lambda x:abs(x))
corr = corr.sort_values('label',ascending=False)

#输出结果
print('采用的特征提取法：相关系数法\n')
print('label最相关的几个特征：\n',corr.head())

#绘制特征关系图
sns.heatmap(data.corr(),cmap='coolwarm',annot=True,fmt='.2f',xticklabels=1,yticklabels=1,linewidths=0.5)
plt.xticks(rotation=90,fontsize=12)
plt.yticks(rotation=0,fontsize=12)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()