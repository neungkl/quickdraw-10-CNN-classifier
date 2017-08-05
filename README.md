Quickdraw 10 CNN Classifier
===

Demo project.

This is machine learning project to classify [Google Quickdraw image](https://github.com/googlecreativelab/quickdraw-dataset) just only 10 classes with convolutional neural networks using [Keras](https://keras.io/) and [Tensorflow](https://www.tensorflow.org).<br>
And also serve hand-writting website with [Flask](http://flask.pocoo.org/)

![Quickdraw Preview](docs/quickdraw-preview.jpg)

## Training Data Preparation

Enter these command to automatic download training dataset

```
chmod +x ./data-download.sh
./data-download.sh

# Or
docker-compose exec quickdraw ./data-download.sh
```