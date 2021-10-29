# Anomaly detection

### 1 Problem motivation

- **Example**: Aircraft engine
  - two features: heat generated, vibration intensity
  - given dataset, for a new engine, to detect whether it's anomalous
- **Density estimation**
  - 数据是怎么分布的[如以一个为中心，分布密度向外减小]
- **Other examples**
  - Fraud detection
  - Manufacturing
  - Monitoring computer in a data center

---



### 2 Gaussian distribution

- **Gaussian (Normal ) distribution**

  - example for different $\mu\text{ and }\sigma$

  ![15-1](.\img\15-1.png)

- **parameter estimation**

  - $\mu=\frac{1}{m}\sum_{i=1}^mx^{(i)}$
  - $\sigma^2=\frac{1}{m}\sum_{i=1}^m(x^{(i)}-\mu)^2$

---



### 3 Algorithm

- **Density estimation**

  - $p(x)=\prod_{j=1}^np(x_j;\mu_j,\sigma_j^2)$ 

- **Anomaly detection algorithm**

  ![15-2](.\img\15-2.png)

---



### 4 Developing and evaluating an anomaly detection system

![15-3](.\img\15-3.png)

---



### 5 Anomaly detection vs. supervised learning

![15-4](.\img\15-4.png)

- 异常检测：鸡蛋里挑石头；分类监督问题：哪些是石头那些是鸡蛋

---



### 6 Choosing what features to use

- **Non-gaussian features**: use many methods to transform into gaussian

- **Error analysis for anomaly detection**
  - want normal data x' p(x) to be large, and anomalous data x's p(x) to be small
  - sometime, it make error resulting wrong prediction, can **try adding/creating new feature to solve**

---



### 7 Multivariate Gaussian distribution

- don't model separately, but model all in one go

- **Example**

  ![15-5](.\img\15-5.png)

----



### 8 Anomaly detection using the multivariate Gaussian distribution

- **Multivariate Gaussian distribution**

  - Parameter: $\mu\in\mathbb{R}^n,\ \sigma\in\mathbb{R}^{n\times n}$
  - Parameter fitting:
    - $\mu=\frac{1}{m}\sum_{i=1}^mx^{(i)}$
    - $\sum=\frac{1}{m}(x^{(i)}-\mu)(x^{(i)}-\mu)^T$

- **Anomaly detection with the multivariate gaussian**

  ![15-6](.\img\15-6.png)

- **Relationship to original model**

  ![15-7](.\img\15-7.png)

