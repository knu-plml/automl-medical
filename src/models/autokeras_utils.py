from autokeras.utils.io_utils import image_dataset_from_directory
from autokeras import ImageClassifier
import autokeras as ak
import kerastuner
import os


import joblib
import os
import models.metric_utils
from sklearn.model_selection import train_test_split


def train(X_train, y_train, data_flag, output_root):
    time = 2 * 60 * 60

    # Split the training data into a training set and a validation set
    X_train, X_vali, y_train, y_vali = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

    # Initialize Autokeras classifier with specified parameters
    model = ak.StructuredDataClassifier(overwrite=True, max_trials=1,
                                        metrics=['accuracy','Precision', 'Recall'],
                                        objective="val_loss")
    
    # Fit the model on the training data
    model.fit(X_train, y_train, validation_data=(X_vali, y_vali), epochs=1)
    
    # Save the trained model to a file
    joblib.dump(model, os.path.join(output_root, '%s_autokeras.m' % (data_flag)))


def test(X_test, y_test, data_flag, output_root):
    # Load the trained model from the file
    model = joblib.load(os.path.join(output_root, '%s_autokeras.m' % (data_flag)))
    
    # Make predictions with the loaded model
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)
    
    # Evaluate the model's performance
    models.metric_utils.clf_eval(y_test, y_pred, y_pred_proba[:,1])


def main(data_flag, output_root, train_flag, X_data, y_data):
    # Main function to handle training and testing based on the train_flag
    if train_flag:
        # If training flag is True, train the model
        train(X_data, y_data, data_flag, output_root)
    else:
        # Otherwise, test the model
        test(X_data, y_data, data_flag, output_root)
    