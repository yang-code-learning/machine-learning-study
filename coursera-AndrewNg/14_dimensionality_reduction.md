# Dimensionality Reduction

### 1 Motivation

- **Data Compression**
  - **Dimension reduction**: project
- **Data Visualization**

---



### 2 Principal component analysis problem formulation

- **PCA is not linear regression**

  ![image-14-1](.\img\14-1.png)

---



### 3 Principal component analysis algorithm

- **Data preprocessing**: mean normalization / feature scaling

  ![image-14-2](.\img\14-2.png)

- **Principal Component Analysis (PCA) algorithm**: covariance matrix & eigenvectors

  - 奇异值分解

  ![14-3](.\img\14-3.png)

- **Dimension reduction**

  ![14-4](.\img\14-4.png)

---



### 4 Choosing the number of principal components

- **Principle**: say choose a k allows keeping 99% of variance

  ![14-5](.\img\14-5.png)

- **Algorithms**

  - Method one

    ![14-6](.\img\14-6.png)

  - Method two: SVD function

    ![14-7](.\img\14-7.png)

---



### 5 Reconstruction from compressed representation

- k => n (from lower dimensional representation map to an **approximation** of origin dimensional data)

![14-8](.\img\14-8.png)

---



### 6 Advice for applying PCA

- **Supervised learning speedup**

  ![14-9](.\img\14-9.png)

- **Application of PCA**

  - Compression and visualization

- **Bad use of PCA: to prevent overfitting**

  - fewer features is like to overfit
  - instead using regularization

- **PCA is sometimes used where it shouldn’t be**

  - like designing of ML system 
  - first try running with the original/raw data
  - only if that doesn’t do what you want, then implement PCA

