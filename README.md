# Contour-Shape-Finder-OpenCV

## Contour_Centroid.ipynb
* Pre-Processing the image
  - Converting RGB to grayscale
  - Blurring the image to reduce noise
  - Applying binarization using threshold
* Grabbing the contours from the image 
* Using moments to find the centroid.
* Adding text and drawing contours in the image
![alt text](https://github.com/vermavinay982/Contour-Shape-Finder-OpenCV/blob/master/assets/contour.png)

## Shape_of_Contour.ipynb
* Pre-Processing the image
* Grabbing the contours from the image 
* Reducing the number of points in curve by assuming them as line segments
* The number of line segments will give the shape of polygon
  - if the line segments are too much - Assume it as circle
  - if the aspect ratio of bounding box is 1 - then square else rectangle
* Using moments to find the centroid.
* Adding text and drawing contours in the image
![alt text](https://github.com/vermavinay982/Contour-Shape-Finder-OpenCV/blob/master/assets/shapes.png)
