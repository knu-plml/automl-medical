from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import label_binarize
import numpy as np


def clf_eval(y_test, y_pred, y_pred_proba):
    print('accuracy : ', accuracy_score(y_test, y_pred))
    try:
        print('precision : ', precision_score(y_test, y_pred))
        print('recall_score : ', recall_score(y_test, y_pred))
        print('f1_score :', f1_score(y_test, y_pred))
        print('roc_auc_score : ', roc_auc_score(y_test, y_pred_proba))
    except Exception as e:
        print('precision : ', precision_score(y_test, y_pred, average="weighted"))
        print('recall_score : ', recall_score(y_test, y_pred, average="weighted"))
        print('f1_score :', f1_score(y_test, y_pred, average="weighted"))
        try:
            print('roc_auc_score : ', roc_auc_score(y_test, y_pred_proba, average="weighted"))
        except Exception as e:
            n_classes = len(np.unique(y_test)) 
            y_test_binarized = label_binarize(y_test, classes=np.arange(n_classes))
            
            print('roc_auc_score : ', roc_auc_score(y_test_binarized[:,1], y_pred_proba, average="weighted", multi_class='ovr'))