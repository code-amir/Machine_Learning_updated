**Anomaly detection with autoencoder neural network applied on detecting malicious URLs**

##  Training/testing data
The dataset we are going to use is retrieved from Kaggle. It contains a list of 420465 URLs with good/bad labels to mention if the concerned URL is malicious or not. We will use only the ‘good’ URLs to train the autoencoder. And since it will be exciting to check if our model is working we will use both good and bad URLs for testing. 80% of data will be used for training the model after keeping only the normal cases and 20% will be used for testing.

## Implementation
The implementation is coded in Python using Keras for building and training the model and Pandas for data manipulation.
