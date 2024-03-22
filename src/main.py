import pandas as pd
import numpy as np

import models.autokeras_utils as aku
import models.autosklearn_utils as asu
import models.autogluon_utils as agu
import models.tpot_utils as tpu

import os
import argparse

# models = ['autosklearn', 'tpot', 'autokeras', 'autogluon']
def main(data_flag, output_root, train_flag, model):
    models = {
        'autosklearn': asu,
        'autokeras': aku,
        'autogluon': agu,
        'tpot': tpu
        }
    
    X_data, y_data = data_load(data_flag, train_flag)
    models[model].main(data_flag, output_root, train_flag, X_data, y_data)


def data_load(data_flag, train_flag):
    # Data categories
    data_3d = ['organ', 'nodule', 'fracture', 'adrenal', 'vessel', 'synapse']
    data_2d = ['pathmnist', 'chestmnist', 'dermamnist', 'breastmnist', 'bloodmnist', 'tissuemnist', 
            'octmnist', 'pneumoniamnist', 'retinamnist', 'organamnist', 'organcmnist', 'organsmnist']
    data_table = ['cardio', 'nhb']
    data_signal = ['mitbih', 'cinc']
    data_mela = ['melanoma']

    # data_2d = ['pathmnist', 'chestmnist', 'dermamnist', 'breastmnist', 'bloodmnist', 'tissuemnist', 
    #        'octmnist', 'pneumoniamnist', 'retinamnist', 'organamnist', 'organcmnist', 'organsmnist']
    if data_flag in data_2d:
        if train_flag:
            pass
        else:
            pass

    # data_3d = ['organ', 'nodule', 'fracture', 'adrenal', 'vessel', 'synapse']
    elif data_flag in data_3d:
        if train_flag:
            pass
        else:
            pass

    # data_table = ['cardio', 'nhb']
    elif data_flag in data_table:
        if data_flag == 'cardio':
            X_data, y_data = load_cardio(train_flag)
        else:
            X_data, y_data = load_nhb(train_flag)

    # data_signal = ['mitbih', 'cinc']
    elif data_flag in data_signal:
        if data_flag == 'mitbih':
            X_data, y_data = load_mitbih(train_flag)
        else:
            X_data, y_data = load_cinc(train_flag)

    # data_mela = ['melanoma']
    elif data_flag in data_mela:
        if train_flag:
            pass
        else:
            pass

    else:
        print("Error")

    return X_data, y_data


def load_cardio(train_flag):
    if train_flag:
        df = pd.read_csv('../dataset/tabular/cardio_train.csv')
    else:
        df = pd.read_csv('../dataset/tabular/cardio_test.csv')
    
    X_data, y_data = df.iloc[:, :-1], df.iloc[:, -1]
    
    return X_data, y_data


def load_nhb(train_flag):
    if train_flag:
        df = pd.read_csv('../dataset/tabular/nh_blood_train.csv')
    else:
        df = pd.read_csv('../dataset/tabular/nh_blood_test.csv')
    
    X_data, y_data = df.iloc[:, :-1], df.iloc[:, -1]
    
    return X_data, y_data


def load_mitbih(train_flag):
    if train_flag:
        df = pd.read_csv('../dataset/signals/mitbih_train.csv', header=None)
    else:
        df = pd.read_csv('../dataset/signals/mitbih_test.csv', header=None)
    
    X_data, y_data = df.iloc[:, :-1], df.iloc[:, -1]
    
    return X_data, y_data


def load_cinc(train_flag):
    if train_flag:
        df = pd.read_csv('../dataset/signals/cinc_train.csv')
    else:
        df = pd.read_csv('../dataset/signals/cinc_test.csv')
    
    X_data, y_data = df.iloc[:, :-1], df.iloc[:, -1]
    
    return X_data, y_data
    

# data_3d = ['organ', 'nodule', 'fracture', 'adrenal', 'vessel', 'synapse']
# data_2d = ['pathmnist', 'chestmnist', 'dermamnist', 'breastmnist', 'bloodmnist', 'tissuemnist', 
#            'octmnist', 'pneumoniamnist', 'retinamnist', 'organamnist', 'organcmnist', 'organsmnist', 
#            'melanoma']
# data_table = ['cardio', 'nheb']
# data_signal = ['mitbih', 'cinc']

# models = ['autosklearn', 'tpot', 'autokeras', 'autogluon']

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--data',
                        default='pathmnist',
                        type=str)
    parser.add_argument('--output_root',
                        default='../bestmodel/',
                        type=str)
    parser.add_argument('--train_flag',
                        default=1,
                        type=int)
    parser.add_argument('--model',
                        default='autokeras',
                        type=str)
    
    args = parser.parse_args()
    data = args.data
    output_root = args.output_root
    train_flag = args.train_flag
    model = args.model
    print(model)
    
    main(data, output_root, train_flag, model)
    