<div align="center">
  <center><h1>Python / ML bootcamp by 42AI pt1 📈</h1></center>
  </div>

<div id="user-content-toc">
  <ul>
    <summary><h2 style="display: inline-block;">Topics:</h2></summary>
  </ul>
</div>


-   Object-Oriented Programming

-   Linear Algebra

-   Numpy arrays and Pandas dataframes manipulation

-   Image Processing with numpy

-   Generators

-   Decorators

-   How to publish packages on PyPi

-   K-Means algorithm from scratch

#

<div id="user-content-toc">
  <ul>
    <summary><h2 style="display: inline-block;">Highlights:</h2></summary>
  </ul>
</div>


### <u>Image processing with numpy</u>

Applying color filters to images using numpy arrays.
Images are loaded as numpy arrays, each pixel is represented by a 3-tuple of RGB values. We can apply filters to the image by modifying the RGB values of each pixel.

<p float="left">
<img src="https://user-images.githubusercontent.com/91064070/218063205-899eef39-b3dc-49db-9467-2be7149eab1e.jpg" width="250" height="150">
<img src="https://user-images.githubusercontent.com/91064070/218063346-350e66ae-c539-4b2e-ab18-eec930d225ee.PNG" width="250" height="150">
</p>

<p float="left">
<img src="https://user-images.githubusercontent.com/91064070/218063263-3057c018-9385-4282-817f-d96dc8f31eed.PNG" width="250" height="150">
<img src="https://user-images.githubusercontent.com/91064070/218063164-266d1760-32e6-44cd-897a-78011a922091.PNG" width="250" height="150">
</p>

<p float="left">
<img src="https://user-images.githubusercontent.com/91064070/218063471-8db2e144-fc1a-410b-b593-0ac73122c62b.PNG" width="250" height="150">
<img src="https://user-images.githubusercontent.com/91064070/218063362-8b1d78d1-aaca-48e2-aff5-db86a74fe0ce.PNG" width="250" height="150">
</p>

<br />

### <u>K-Means from scratch</u>

K-Means is an unsupervised learning algorithm that groups data points into k clusters. The algorithm is iterative and starts by randomly assigning each data point to a cluster. Then, the algorithm iterates between two steps:

-   The centroid of each cluster is computed.
-   Each data point is assigned to the cluster whose centroid is the closest.

The algorithm stops when the data points no longer change cluster.

3d plot of the K-Means algorithm on a dataset of 4 clusters and 3 features:

![K-Means](https://user-images.githubusercontent.com/91064070/218058393-38f82f1a-88d0-4d0c-940c-1e076763fdd6.png)
