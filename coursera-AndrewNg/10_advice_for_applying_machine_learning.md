# Advice for applying machine learning

### 1 Decide what to try next

- **Debugging a learning algorithm**
  - Get more training examples
  - additional features
  - ...
- **Machine learning diagnostic**

---



### 2 Evaluating a hypothesis

- **Dataset**: training set and test set (usually 7 : 3), shuffle
- **Training/testing procedure for linear regression**
- **Training/testing procedure for logistic regression**
  - misclassification error

---



### 3 Model selection and training/validation/test sets

- **Model selection**
  - problem: overfitting
- **Dataset**: Training set and Cross validation set and Testing set4 
- **Train/validation/test error**
  - 简单来说，测试集是用来初步拟合数据，训练集是用来挑选模型（最佳拟合的多项式模型），测试集是检验模型成效的。
  - 相当于训练集是教科书[分别使用不同的学习方法]，验证集是平时作业[自己对答案看那种学习方法最好]，测试集是大考[用分数评估这种学习方法的质量]

---



### 4 Diagnosing bias vs. variance

- **Bias / variance**

  - Training error / Cross validation error

- **Diagnosing bias vs. variance**

  ![image-10-1](.\img\10-1.png)

  - **Bias (underfit)**: high training error and high cross validation error
  - **Variance (overfit)**: low training error and high cross validation error 

---



### 5 Regularization and bias/variance

- **Linear regression with regularization**
  - large regularization parameter => high bias (underfit)
  - small regularization parameter => high variance (overfit)
- **Choosing the regularization parameter**
  - try different $\lambda$

- **Bias/variance as a function of the regularization parameter**

  ![image-10-2](.\img\10-2.png)

---



### 6 Learning curve

- **The train set size** (normally)

  - the bigger, the larger of training error, the smaller of validation error

  ![image-10-3](.\img\10-3.png)

- **High bias**

  - the more data will not help much

  ![image-10-4](.\img\10-4.png)

- **High variance**

  - more data is likely to help (but slowly)

  ![image-10-5](.\img\10-5.png)

---



### 7 Deciding what to try next (revisited)

- **Debugging a learning algorithm**

  - Get more training examples => fixes high variance
  - Try smaller sets of features => fixes high variance
  - Try additional features => fixes high bias
  - Try adding polynomial features => fixes high bias
  - Try decreasing $\lambda$ => fixes high bias
  - Try increasing $\lambda$ => fixes high variance

- **Neural networks and overfitting**

  ![image-10-6](.\img\10-6.png)
