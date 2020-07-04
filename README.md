# Acceptance-Prediction-for-Conference-Paper

This project is instructed by AI605, NLP in GSAI, KAIST

We make experiment on prediction for conference paper, more clearly by using ICLR (2018~2020)
Through this model, we can predict a given data (title, abstract, ...) whether it can be accepted or not, especially in ICLR.
As a baseline experiment, we used sentiment classification about IMDB and Yelp dataset.

BERT is used as baseline model. From this, we make variation with LSTM as a classification head network.

In this project, the descriptiond about components are as follows.

(dir) data-processing : files to crawl ICLR paper data from openreview (https://openreview.net/) and generate meta-data from crawled data
(dir) hedwig-master/hedwig-baseline : used BERT model for the experiments
(dir) hedwig-master/hedwig-LSTM : used BERT + LSTM layers
(dir) hedwig-master/hedwig-data : Dataset used for the experiments. To run this project, you have to download IMDB, Yelp dataset and bert-pretrained mdoel in this directory

Experimental results in detail
