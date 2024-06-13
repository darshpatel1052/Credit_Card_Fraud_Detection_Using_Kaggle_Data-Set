# Credit Card Fraud Detection

This project aims to build a robust and efficient model for detecting credit card fraud using the Random Forest algorithm, which is known for its high accuracy and versatility. The model is trained and validated using multiple cross-validation techniques to ensure its reliability. The project also includes a feature reduction step to improve the model's efficiency. The final model is integrated with a Flask backend and a simple HTML frontend to provide a user-friendly interface for fraud detection.

## Table of Contents

- [Project Explanation](#project-explanation)
- [Installation](#installation)
- [Usage](#usage)
- [Suggestions](#suggestions)

## Project Explanation

The project is divided into several parts:

1. **Data Preprocessing:** The first step in any machine learning project, where we clean and transform raw data into a format that can be fed into our model.

2. **Model Training:** We use the Random Forest algorithm to train our model. The model is trained using multiple cross-validation techniques to ensure its reliability.

3. **Feature Reduction:** We reduce the number of features in our model to improve its efficiency and prevent overfitting.

4. **Model Integration:** The final model is integrated with a Flask backend and a simple HTML frontend. This allows users to interact with the model through a simple web interface.

## Installation

1. Clone the repository:
https://github.com/darshpatel1052/Credit_Card_Fraud_Detection_Using_Kaggle_Data-Set

2. Navigate to the project directory:
cd Credit_Card_Fraud_Detection_Using_Kaggle_Data-Set

3. Install the required Python packages:
pip install -r requirements.txt

4. Fetching Dataset:
I have added a text file Named (data_set.txt) which contains a kaggle dataset link just simply click on it and download the dataset it might take
a few minutes as the file is large.

## Usage

1. Run the Flask server:
ccd_Flask.py

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter the query points in the provided form and click 'Submit' to get the prediction.

## Suggestions

Your suggestions and feedback are appreciated. Feel free to open an issue or submit a pull request if you have something to contribute. You can also contact me directly at daksh4765@gmail.com.
