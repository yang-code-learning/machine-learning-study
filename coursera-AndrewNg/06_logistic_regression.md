# Logistic regression

## 1 Classification

- **example**:
  - Email: spam / not spam
  - Online Transactions: Fraudulent (Yes / No)?
  - Tumor: Malignant / Benign
- start form binary classification: positive or negative
- **logistic regression algorithm**: the output are always between 0 and 1

---



## 2 Hypothesis representation

- **Logistic function** (Sigmoid function)
  $$
  g(x) = \frac{1}{1+e^{-x}}
  $$

  - the **Hypothesis** would be $h_\theta = g(\theta^TX)$

- **Interpretation of Hypothesis output**

  - $h_\theta(x)$=estimated probability that y=1 on input x
  - $P(y=0|x;\theta)$ = probability that y = 1, given x, parameterized by $\theta$
  - $P(y=0|x;\theta)+P(y=1|x;\theta)=1$

---



## 3 Decision boundary

- a threshold (like $y=1\ if\ h_\theta(x)\geq0.5(x\geq0)\ else\ y=0$)
- a line separate two region (not just line, but circle and so on)
- not a property of dataset, the hypothesis and parameters determined the boundary, the boundary helps fit the parameters

---



## 4 Cost function

- **Hypothesis**
  $$
  h_\theta = \frac{1}{z+e^{-\theta^Tx}}
  $$
  
-  **Cost function**
  $$
  J(\theta)=\frac{1}{m}Cost(h_\theta(x),y)
  \\
  Cost(h_\theta(x),y) = \begin{cases}
  -log(h_\theta(x))& if\ y=1\\
  -log(1-h_\theta(x))& if\ y=0\end{cases}
  $$

  - $cost = 0\ if\ y=1,h_\theta(x)=1$ and $cost=0\ if\ y=0,h_\theta(x)=0$
  - which means the lower the cost is, more correct the Hypothesis will be
    - (不行用中文好说点)  对于x特征，真实情况是恶性肿瘤（y=1），但是假设的出来是良性（h=0），说明误差很大（代价很大）放到上面的函数就是这样一个过程，接下来就要降低代价，代价如果为0，此时假设的结果1，事实上y确实1，说明假设正确。【线性回归也可以这么理解，代价就是假设的线到各点均距离，代价越小，说明这条线贴合曲线，拟合的越好】
    - 为什么不直接按照线性回归类似求均差呢？因为设置了逻辑函数，这样代价函数是非凸函数，没法求极值；为什么要设逻辑函数呢？因为要把假设（预测）的结果限制在0-1；为什么限制在0和1，因为是二分类问题，即0和1，将假设结果通过逻辑函数映射到概率（0~1），用概率去解释0和1的倾向性，设置阈值后进行分类【还是有点没解释清楚，可能是log函数的原因，也感觉有Scaling的意味，总之逻辑回归就是得应用逻辑函数】

---



## 5 Simplified cost function and gradient descent

- **simplified version**
  $$
  J(\theta)=\frac{1}{m}Cost(h_\theta(x),y)\\
  Cost(h_\theta(x),y) = 
  -ylog(h_\theta(x))-(1-y)log(1-h_\theta(x))
  $$

- to fit parameters $\theta:\ \underset{\theta}{min}\ J(\theta)$, and to make a prediction give new x with an output $h_\theta(x)$

- **gradient descent**
  $$
  \theta_j:=\theta_j-\alpha\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}\\
  (\text{for every j in 0 to n})
  $$

  - look same as linear regression, the hypothesis is totally different

---



## 6 Advanced optimization

- two compute term: cost function and derivative terms
- **optimization algorithms:** conjugate gradient, BFGS, L-BFGS
  - no need to manually pick learning rate; faster; but more complex 

- **example on Octave**

  ![image-6-1](.\img\6-1.png)

---



## 7 Multi-classification one-vs-all

- one-vs-all
  - Train a logistic regression classifier $h_\theta^{(i)}(x)$ for each class $i$ to predict the probability that $y=i$
  - On a new input $x$, to make a prediction, pick the class $i$ that maximizes $\underset{i}{max}h_\theta^{(i)}(x)$