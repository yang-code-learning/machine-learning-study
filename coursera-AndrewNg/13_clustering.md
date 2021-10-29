# Clustering

### 1 Unsupervised learning introduction

- **Supervised learning**
- **Unsupervised learning**
- **Application of clustering**

---



### 2 K-means algorithm

- **Input**

  - K (number of clusters)
  - Training set

- **Algorithm**: cluster assignment & move centroid

  ![image-13-1](.\img\13-1.png)

---



### 3 Optimization objective

- **Optimization objective**: distortion cost function

  ![image-13-2](.\img\13-2.png)

---



### 4 Random initialization

- **Method one:** randomly pick K training examples
  - causing local optima
  - try many time, pick one the gave lowest cost J

---



### 5 Choosing the number of cluster

- **Elbow method**
  - the point (number of clusters) where Cost function drop rapid before but slow after
  - if no clear "elbow", might be a problem
- Later/downstream purpose
  - based on a metric for how well it performs for a later purpose

