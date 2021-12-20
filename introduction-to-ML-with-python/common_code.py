# 基础库导入
from io import SEEK_CUR
from operator import ipow
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn # 一个集成上述库及额外参数设置，主要用于画图

# 数据集分割
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons
from sklearn.datasets import make_blobs
from sklearn.datasets import make_f
from sklearn.datasets import make_wave
from mglearn.datasets import make_forge
from mglearn.datasets import make_wave

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LogisticRegression
mglearn.plots.plot_2d_separator
mglearn.plots.plot_ridge_n_samples
from sklearn.svm import LinearSVC
mglearn.discrete_scatter()
mglearn.plots.plot_linear_svc_regularization()
mglearn.plots.plot_2d_classification()
mglearn.plots.plot_animal_tree()
from sklearn.tree import DecisionTreeClassifier
mglearn.plots.plot_tree_not_monotone()