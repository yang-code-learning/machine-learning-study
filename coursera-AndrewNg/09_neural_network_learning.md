# Neural Network: Learning

### 1 Cost function

- **Classification**

  - Binary classification: **1 output unit**
    $$
    y=0\ or\ 1
    $$

  - Multi-class classification (K classes): **K output units**
    $$
    y\in\mathbb{R}^K\\
    $$

- **Cost function**
  $$
  J(\theta) = -\frac{1}{m}[\sum_{i=1}^m\sum_{k=1}^Ky_k^{i}log(h_\theta(x^{(i)}))_k+(1-y_k^{(i)})log(1-h_\theta(x^{(i)}))_k)]\\
  +\frac{\lambda}{2m}\sum_{l=1}^{L-1}\sum_{i=1}^{S_l}\sum_{j=1}^{S_{l+1}}(\theta_{ji}^{(l)})^2
  $$
  
  - $h_\theta(x)\in\mathbb{R}^K$ 表示结果是一个K维向量，加上下标表示第几个结果（第几个分类），第一项就是对单条数据的所有结果求和（代价）然后对所有数据的代价求和，第二项就是正则项，下标ji表示目标层和来源层，先对单个来源层神经元影响的所有目标层结点的权重求和，在对所有来源层结点这权重求和，这个就是层与层之间所有权重的和，最后把所有层之间的权重矩阵求和。

---



### 2 Backpropagation algorithm

- **Gradient computation**: Forward propagation

  ![image-9-1](.\img\9-1.png)

- **Gradient computation**: Backpropagation algorithm 

  - Intuition: $\delta_j^{(l)}=\text{"error" of node }j\text{ in layer }l$s 

    ![image-9-2](.\img\9-2.png)

  - The process

    ![image-9-3](.\img\9-3.png)


---



### 3 Backpropagation intuition



---



### 4 Implementation note: Unrolling parameters

- reshape()

---



### 5 Gradient checking

- **Numerical estimation of gradients**
- **Parameter vector $\theta$**

---



### 6 Random initialization

-  **Zero initialization**: parameters of two hidden units are identical after each update
- **Symmetry breaking**: initialize each parameter to a random value

---



### 7 Putting it together

- **Training a neural network**: usually the more of hidden layer, the better

![image-9-4](.\img\9-4.png)

---



### 8 Autonomous driving example

- just an video
