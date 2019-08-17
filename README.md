# Garden Nerd (Flower recognition Challenge)
This repository contains the training code to build a CNN classifier to classify between 102 classes of images, It also contains how to build a segmentation model.

### Dataset given:
Below is the image of the given dataset to build the classifier
![actual dataset](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/orig0.jpg)
![actual dataset](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/orig1.jpg)
![actual dataset](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/orig2.jpg)

### Segmentation model:
First trained a segmentation model to produce the mask of flowers, after the mask is generated we applied the mask to generate a segmented image on which we are going to train our model.
Below is the Image of generated mask :
![mask](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/mask0.jpg)
![mask](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/mask1.jpg)
![mask](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/mask2.jpg)

### Final generated data:
The above generated mask is applied to the actual dataset, this will generate the segmentation of the image, and help our model to learn only necessary details of the flowers such as Shape, Design, Colour etc.
Below is the final segmentation :
![final segmentation](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/Final0.jpg)
![final segmentation](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/Final1.jpg)
![final segmentation](https://github.com/shiwanshurockz/Garden-Nerd-flower-recognition-/blob/master/readme_img/Final2.jpg)
