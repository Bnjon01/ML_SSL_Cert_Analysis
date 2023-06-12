# Machine Learning solution to SSL Cert Analysis
Machine Learning models predicting malicious SSL certificates

## Project Description
This project takes the data from a given website's SSL certificate and predicts using one of three Machine Learning classification models whether or not the website harbours malicious content.
The model correctly predicts up to almost 98% of the SSL certificates as belonging to either malicious or benign websites.

## Method
### Preprocessing
The preprocessing involves splitting the following SSL certificate features into a csv file:
- Issuer's organisation name (ASCII string)
- Issuer's common name (ASCII string)
- Issuer's country (ASCII string)
- Subject's country (ASCII string)
- Subject's (number of) details (Integer)
- Subject's alternate names (Integer)
- Subject's days of validity (Integer)

A Sample of data using this format is provided in the "FullCertList.csv" file and includes an extra column contianing the classification of malicious or benign website.

### Model
This project contains three classifiers, Decision Tree, Random Forests, and Gradient Boosting. The project is written in Python 3 and use Pandas, Numpy, and SciKit for modules.

## Usage
The program contains three classifications, comment/uncomment each block of code as they are marked with a commented header for each classifier to be tested.
To run this program, simply place the "cert_analysis.py" file in the same location as the "FullCertList.py" file and enter the following into a terminal:

`python3 cert_analysis.py`

The result will be the accuracy values for the prediction, as well as the 5-fold Cross Validation score.
