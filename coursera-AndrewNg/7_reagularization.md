# Regularization

### 1 The problem of overfitting

- **examples**: linear regression
  - **underfit**: high bias (say linear hypothesis)
  - **just** **right** (say a quadratic function)
  - **overfit**: high variance (say higher order polynomial)

- **example**: logistic regression
- definition (**overfitting**): too many features, the learned hypothesis may *fit the training set very well*(cost function is so close to zero), but *fail to generalize to new examples* 
- addressing overfitting
  - options 0: 
    - visualization (hard to plot with many features)
  - options 1: reduce number of features
    - manually select
    - model selection algorithm
  - options 2: regularization
    - keep all the features, but reduce magnitude of parameters
    - therefore, each of features contribute to predicting, though only a bit

---



### 2 Cost function

- **Idea**: small values for parameters to gain a simpler hypothesis

- **regularization**: 

  - add parameters to cost function (regularization term)

  $$
  J(\theta)=\frac{1}{2m}[\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})+\lambda\sum_{j=1}^n\theta_j^2]
  $$

  - regard as a punishment to large parameters
  - no need to deal with $\theta_0$, it's a parameter to a constant variable
  - the choice for regularization parameter $\lambda$ is important, elsewhere it would turn to be underfitting

---



### 3 Regularized linear regression

- **Cost function**:
  $$
  J(\theta)=\frac{1}{2m}[\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})+\lambda\sum_{j=1}^n\theta_j^2]
  $$
   

- **Gradient descent**:
  
  - basically slightly differences
    $$
    \theta_0:=\theta_0 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_0^{(i)}\\
    \theta_j:=\theta_j(1-\alpha\frac{\lambda}{m}) - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}\\
    \text{for every j in 1,2,3,...,n}
    $$
  
- **normal equation**:
  $$
  \theta=
  \left(
  X^TX+\lambda\
  \begin{bmatrix}
   0 	& 	&	&\\
   	& 1 &	&\\
  	& 	&\ddots &\\
   	& 	&	&	1
   \end{bmatrix}
   \right)^{-1}X^Ty
  $$

  - always invertible as long as $\lambda>0$

---



### 4 Regularized logistic regression

- **Cost function**:
  $$
  J(\theta) = -[\frac{1}{m}\sum_{i=1}^my^{(i)}log(h_\theta(x^{(i)}))+(1-y^{(i)})log(1-h_\theta(x^{(i)}))]+\frac{\lambda}{2m}\sum_{j=1}^n\theta_j^2
  $$
  

- **Gradient descent**:
  $$
  \theta_0:=\theta_0 - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_0^{(i)}\\
  \theta_j:=\theta_j - \alpha[\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}+\frac{\lambda}{m}\theta_j]\\
  \text{for every j in 1,2,3,...,n}
  $$
  

- **Advanced optimization**
