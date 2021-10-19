# Neural networks: representation

### 1 Non-linear hypotheses

- Non-linear Classification:  tons of polynomial features 
- Example: computer vision in cars detection

---



### 2 Neurons and the brain

- **Overview** 
- **The "one learning algorithm" hypothesis**
- **Sensor representation in the brain**

---



### 3  Model representation

- **Neuron in the brain**

- **Neuron model: Logistic unit**

  - Sigmoid (logistic) activation function

- **Neural Network**

  ![image-8-2](.\img\8-2.png)

  ![image-8-3](.\img\8-3.png)

  - 权重在这里是一个存在于不同层之间的一个$S_{j+1}\times(s_j+1)$矩阵，$S_{j+1}$ 代表输出的结点个数，$(s_j+1)$ 代表输入结点个数加一个$x_0$，反正看上面的公式

- **Forward propagation: Vectorized implemetation**

  ![image-8-4](.\img\8-4.png)

- **Neural network learning its own features**

  - essentially a logistic regresssion
  - but feature are its own (hidden layer)

- **Other network architecture**

  - examples

---



### 4 Examples and intuitions

- **Non-linear classification example: XOR/XNOR**

  - Simple example: AND
  - Example: OR function
  - Negation

- **Putting it together**

  ![image-8-5](.\img\8-5.png)

- **Handwritten digit classification**

---



### 5 Multi-class classification

- **Multiple output uints: One-vs-all**

  ![image-8-6](.\img\8-6.png)