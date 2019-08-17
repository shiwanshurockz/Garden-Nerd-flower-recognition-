# Garden Nerd (Flower recognition Challenge)
This repository contains the training code to build a CNN classifier to classify between 102 classes of images

### Dataset given:
below is the image of the given dataset to build the classifier
![actual dataset](readme_images/orig0.jpg)
![actual dataset](readme_images/orig1.jpg)
![actual dataset](readme_images/orig2.jpg)

### Segmentation model:
First trained a segmentation model to produce the mask of flowers, after the mask is generated we applied the mask to generate a segmented image on which we are going to train our model.
Below is the Image of generated mask :
![mask](readme_images/mask0.jpg)
![mask](readme_images/mask1.jpg)
![mask](readme_images/mask2.jpg)

### Final generated data:
The above generated mask is applied to the actual dataset, this will generate the segmentation of the image, and help our model to learn only necessary details of the flowers such as Shape, Design, Colour etc.
Below is the finally segmented image:
![final segmentation](readme_images/Final0.jpg)
![final segmentation](readme_images/Final1.jpg)
![final segmentation](readme_images/Final2.jpg)
