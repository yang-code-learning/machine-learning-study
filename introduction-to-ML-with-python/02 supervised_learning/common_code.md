#### 基础库导入

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn # 一个集成上述库及额外参数设置，主要用于画图
```

#### 数据集分割

```python
from sklearn.model_selection import train_test_split
'''
train_test_split: (*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None) -> list[Sequence | Any | list]
'''
```

array就是数据集，如 X, y，可以有多个；

会被以同样的方式分割，即对应关系保持不变；

stratify 就是参考哪个列表分割，一般对于 X, y 就是 y

#### 数据集加载

```python
from sklearn.datasets import load_boston
from sklearn.datasets import load_extend_boston # 通过特征工程拓展
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris
from sklearn.datasets import make_blobs # 多分类（聚簇）
from sklearn.datasets import make_circles # 二分类（环形）
from sklearn.datasets import make_wave # 二分类（月牙型）
from mglearn.datasets import make_forge # 分类
from mglearn.datasets import make_wave # 回归
```

#### 模型

```python
from sklearn.neighbors import KNeighborsClassifier # K近邻分类
from sklearn.neighbors import KNeighborsRegressor # K近邻回归
from sklearn.linear_model import LinearRegression # 线性回归
from sklearn.linear_model import Ridge # L2 正则化
from sklearn.linear_model import Lasso # L1 正则化
from sklearn.linear_model import LogisticRegression # 逻辑回归（线性分类）
from sklearn.svm import LinearSVC # 线性支持向量机
from sklearn.tree import DecisionTreeClassifier # j


# 拟合
model.fit(X_train, y_train)
# 预测
model.predit(X_test)
# 评测
model.score(X_test, y_test)
# 属性
model.__class__.__name__ # 模型名称
lr.coef_ # “斜率参数”，权重或系数，行-类别，列-特征
lr.intercept_ # 偏移或截距
tree.feature_importances_ # 行-特征，列-重要程度

```

#### pyplot 相关

```python
# 一般
plt.plot(x, y, 'o' label="") # label 这里是图例，x 省略则按照顺序计数
plt.xlabel("") # x轴标签，y轴同理
plt.hline(0,0,length) # 在水平方向从0，0位置画一条length长度的线，垂直方向同理
plt.ylim(down, up) # 设置y轴数值范围，x轴同理
plt.xtick(range(), feature_name, rotation=90) # x轴标签不是数组而是特征名字，且名字显示逆时针90度摆放
plt.legend(['Class 0', 'Class 1' ....], loc=(x, y)) # 标签（按序）和设置位置
plt.barh(range(),feature_importance_, align='center') # 未知

# subplot
fig, axes = plt.subplots(rows, colomns, figsize)
ax.set_title("") # 子图表标签
ax.set_xlabel("") # 设置x轴信息,y轴同理
ax.legeng(loc=3) # 指定图表显示图例，loc指定位置，除了1234还有‘best’和(x,y)坐标
```

fig 大概就是整个图像

axes 就是各个子 plot 构成的 np 列表，可通过 toLis() 变成普通列表

#### mglearn 相关

```python
# 示例
mglearn.plots.plot_knn_classification(n_eighbors=n) # knn分类
mglearn.plots.plot_knn_regression(n_eighbors=n) # knn回归
mglearn.plots.plot_linear_regression_wave() # 线性回归
mglearn.plots.plot_ridge_n_samples() # 岭回归
mglearn.plots.plot_linear_svc_regularization() # 正则化的线性SVM
mglearn.plots.plot_animal_tree() # 决策树示例
mglearn.plots.plot_tree_not_monotone() # 未知

```



```python
mglearn.plots.plot_2d_classification(model, X, fill=True, alpha=0.7)
mglearn.plots.plot_2d_separator(model, X, fill=True, eps=0.5, ax=ax, alpha=0.4)
'''
(function) plot_2d_separator: (classifier, X, fill=False, ax=None, eps=None, alpha=1, cm=cm2, linewidth=None, threshold=None, linestyle="solid") -> Any
'''
```

两个好像差不多，效果就是查看该分类器的决策边界

classifier 就是分类器，fill 即设置是否用颜色填充，

ax 指定在哪个图表显示（常用于subplots）

eps 未知，alpha 即显示的透明度

```python
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
'''
(x1, x2, y=None, markers=None, s=10, ax=None, labels=None, padding=0.2, alpha=1, c=None, markeredgewidth=None) -> Any
'''
```

效果就是散点图，能自动检测标签分配不同图标
