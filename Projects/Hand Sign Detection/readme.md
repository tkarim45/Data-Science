# Sign Language Detection Project #

![alt text](https://www.mdpi.com/jimaging/jimaging-06-00073/article_deploy/html/images/jimaging-06-00073-g009.png)

This project is aimed at developing an AI-based system that can detect sign languages in real-time.

## Introduction ##

Sign language is a visual language that is used by deaf and hard-of-hearing people to communicate with each other. While it is a very effective means of communication, it can be difficult for people who do not know the language to understand. This is where our project comes in. 

Our project aims to develop a system that can detect sign languages and translate them into text or speech. This will enable people who do not know sign language to communicate with people who do.

## Approach ##

![alt text](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41598-022-08133-z/MediaObjects/41598_2022_8133_Fig1_HTML.png)

Our approach to building this system involves training a deep learning model on a large dataset of sign language videos. We will be using a combination of computer vision and natural language processing techniques to detect the signs and translate them.

The dataset we will be using is our own image dataset, which contains over 500 images of each class of the American Sign Language alphabet. We will use support vector machine to train the model tp predict the sign languages and apply the model to the real time video to predict the sign language.

We will also use natural language processing techniques to convert the detected signs into text or speech. For this, we will use use the trained model and predict the signs in real time.

## Creating Images ##

The collect_images.py file is used to make 3 classes of any 3 alphabet hand sign and take 500 images of that hand sign and store it in the images directory as specified.

## Creating Dataset ##

After taking the images, the next step is creating the data set. The create_dataset.py file reads all the images and assign them label. Afterwards using mediapipe library the hand landmarks are made and drawn on the frame and store the axis of those landmarks and store it in a data dict. 

Now, we have labels and hand landmarks data. Finally, we create the final dataset containing labels and hand landmarks.

## Classifier ##

The classifier.py is used to train the model to predict the hand signs. Firstly, we would read the dataset file that we created then apply a classificaton model such as support vector machine to train the model.

Afterwards, the dataset is split into train and test. Model is trained of train data and then accuracy is check on the test data. The model is then stored in a model.p file to be later used for real time prediction.

## Technologies Used ##

The following technologies will be used in this project:

* Python
* Mediapipe
* Support Vector Machine
* OpenCV
* Project Goals

## The goals of this project are as follows: ##

* Develop an AI-based system that can detect sign languages in real-time
* Translate the detected signs into text or speech
* Achieve high accuracy in sign detection
* Provide a user-friendly interface for the system

## Conclusion ##

The Sign Language Detection Project is an important project that has the potential to help deaf and hard-of-hearing people communicate with the hearing community. Our goal is to develop a system that can accurately detect signs in real-time and translate them into text or speech. With this system, we hope to bridge the communication gap between deaf and hearing communities.
