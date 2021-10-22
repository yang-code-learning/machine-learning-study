# Machine learning system design

### 1 Prioritizing what to work on: Spam classification example

- **Building a spam classifier**
  - Honeypot project
  - email routing information
  - message body, punctuation
  - misspelling

---



### 2 Error analysis

- **Recommended approach**
- **Manually select**
- **The importance of numerical evaluation**
  - "stemming" software

---



### 3 Error metrics for skewed classes

- **Cancer classification example**

  - only 0.5% of patients have cancer (skewed classes)

- **Precision/Recall**

  - Precision: $\frac{\text{true positive}}{\text{no. of predicted positive}}$（预测准确率[预测为真就是真，不会误诊]）
  - Recall: $\frac{\text{true positive}}{\text{no. of actual positive}}$（预测命中率[所有为真都猜出来]）

  ![image-11-1](.\img\11-1.png)

---



### 4 Trading off precision and recall

- **The curve**

  ![image-11-2](.\img\11-2.png)

- **F score**
  - $Average:\ \frac{P+R}{2}$, if predict y =1 all the time, the result might be high
  - $F_1\ Score:\ 2\frac{PR}{P+R}$

---



### 5 Data for machine learning

- Designing a high accuracy learning system`
  - Perceptron
  - Winnow
  - Memory-based
  - Naïve Bayes
- Large data rationale
  - assume feature has sufficient information to predict y accurately