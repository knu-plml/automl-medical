from autogluon.tabular import TabularDataset, TabularPredictor

import joblib
import os
import models.metric_utils
import pandas as pd
from sklearn.model_selection import train_test_split


def train(X_train, y_train, data_flag, output_root):
    label = X_train.columns[-1]

    # Split the training data into a training set and a validation set
    X_train, X_vali, y_train, y_vali = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    train_data = pd.concat([X_train, y_train], axis=1)
    val_data = pd.concat([X_vali, y_vali] , axis=1)
    
    # Initialize Autogluon tabularpredictor with specified parameters
    model = TabularPredictor(label=label)

    # Fit the model on the training data
    model.fit(train_data=train_data, tuning_data=val_data, time_limit=3600*2)

    # Save the trained model to a file
    joblib.dump(model, os.path.join(output_root, '%s_autogluon.m' % (data_flag)))
    

def test(X_test, y_test, data_flag, output_root):
    test_data = pd.concat([X_test, y_test], axis=1)

    # Load the trained model from the file
    model = joblib.load(os.path.join(output_root, '%s_autogluon.m' % (data_flag)))
    
    # Make predictions with the loaded model and Evaluate the model's performance
    try:
        y_pred = model.predict(test_data)
        y_pred_proba = model.predict_proba(test_data)

        models.metric_utils.clf_eval(y_test, y_pred, y_pred_proba.values[:,1])
    except:
        print('Not supported regression')
    


def main(data_flag, output_root, train_flag, X_data, y_data):
    # Main function to handle training and testing based on the train_flag
    if train_flag:
        # If training flag is True, train the model
        train(X_data, y_data, data_flag, output_root)
    else:
        # Otherwise, test the model
        test(X_data, y_data, data_flag, output_root)
    