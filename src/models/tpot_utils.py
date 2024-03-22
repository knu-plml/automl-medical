from tpot import TPOTClassifier

import joblib
import os
import models.metric_utils
from sklearn.model_selection import train_test_split

def train(X_train, y_train, data_flag, output_root):
    # Define the scoring method and training time
    time = 2

    # Initialize TPOT classifier with specified parameters
    model = TPOTClassifier(
        early_stop=1,
        max_time_mins=int(time),
        verbosity=2,
        memory='auto'
    )

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model.fitted_pipeline_, os.path.join(output_root, '%s_tpot.m' % (data_flag)))


def test(X_test, y_test, data_flag, output_root):
    # Load the trained model from the file
    model = joblib.load(os.path.join(output_root, '%s_tpot.m' % (data_flag)))
    
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
    