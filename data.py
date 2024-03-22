import os
import csv
import glob
import medmnist
import numpy as np
import pandas as pd
import scipy.io, scipy.signal
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

DATA_PATH='./dataset/'

## EMRs.
os.makedirs(DATA_PATH + 'tabular/', exist_ok=True)
# 1. Cardiovascular Disease Diagnosis Dataset. -Table 1 *XGBoost
# Download a data file on 'https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/download?datasetVersionNumber=1'.
# Move the downloaded file to DATA_PATH + 'tabular/cardio.csv'. 
df = pd.read_csv(DATA_PATH + 'tabular/cardio.csv', sep=';').drop(['id'], axis=1)
train, test = train_test_split(df, test_size=0.2, random_state=42)
train.to_csv(DATA_PATH + 'tabular/cardio_train.csv', sep=',', index=False)
test.to_csv(DATA_PATH + 'tabular/cardio_test.csv', sep=',', index=False)

# 2. National Health Examination Blood Test Data. -Table 2 *XGBoost
# Download and unzip  a data file on 'https://nhiss.nhis.or.kr/down/%EA%B5%AD%EA%B0%80%EA%B1%B4%EA%B0%95%EA%B2%80%EC%A7%84_%ED%98%88%EC%95%A1%EA%B2%80%EC%82%AC_%EB%8D%B0%EC%9D%B4%ED%84%B0.zip'.
# Move only the unzipped csv file to DATA_PATH + 'tabular/nh_blood.csv'.
df = pd.read_csv(DATA_PATH + 'tabular/nh_blood.csv', sep=',')
train, test = train_test_split(df, test_size=0.2, random_state=42)
train.to_csv(DATA_PATH + 'tabular/nh_blood_train.csv', sep=',', index=False)
test.to_csv(DATA_PATH + 'tabular/nh_blood_test.csv', sep=',', index=False)

## Medical Image Data.
os.makedirs(DATA_PATH + 'images/', exist_ok=True)

# 3. MedMNIST Benchmark. -Table 3, 4 *EfficientNetB0
os.makedirs(DATA_PATH + 'images/medmnist', exist_ok=True)

# 2D
medMnists2D = ['Blood', 'Breast', 'Chest', 'Derma', 'OCT', 'OrganA', 'OrganC', 'OrganS', 'Path', 'Pneumonia', 'Retina', 'Tissue']
medMnists2D = list(map(lambda x: x + 'MNIST', medMnists2D))

# 3D
medMnists3D = ['Adrenal', 'Fracture', 'Nodule', 'Organ', 'Synapse', 'Vessel']
medMnists3D = list(map(lambda x: x + 'MNIST3D', medMnists3D))

for Mnist in medMnists2D + medMnists3D:
    funcName = getattr(medmnist, Mnist)
    for typ in ['train', 'val', 'test']:
        data = funcName(split=typ, download=True, root=DATA_PATH + 'images/medmnist/')
        funcName.save(data, folder=DATA_PATH + 'images/')

# 4. ISIC 2020 Challenge Dataset. -Table 5 *EfficientNetB0
# Download and unzip a file on 'https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_JPEG.zip'.
# Download a file on 'https://isic-challenge-data.s3.amazonaws.com/2020/ISIC_2020_Training_GroundTruth.csv'.
# Move the unzipped directory to DATA_PATH + 'images/isic2020/'.
# Move the csv file to DATA_PATH + 'images/train.csv'.

## Biosignal Sensor Dataset.
os.makedirs(DATA_PATH + 'signals/', exist_ok=True)

# 5. MIT-BIH Arrhythmia Dataset. -Table 6 *1D CNN
# Download and unzip two files on 'https://www.kaggle.com/datasets/shayanfazeli/heartbeat'.
# Move the 'mitbih_train.csv' and the 'mitbih_test.csv' to DATA_PATH + 'signals/'.

# 6. PyhsioNet/Cinc 2017 Challenge Dataset. -Table 7 *XGBoost
# Download and unzip a file on 'https://archive.physionet.org/challenge/2017/training2017.zip'
# Move the 'training2017' directory to DATA_PATH + 'signals/'.
FS = 300
WINDOW_SIZE = 60*FS
files = sorted(glob.glob(DATA_PATH + 'signals/training2017/*.mat'))
#train = np.zeros((len(files), 1))
train = [[0] for _ in range(len(files))]
for idx, f in enumerate(files):
    record = f[:-4] # remove '.mat'.
    record = record[-6:] # remove previous directory path.
    mat_data = scipy.io.loadmat(f[:-4] + '.mat')
    data = mat_data['val'].squeeze()
    data = np.nan_to_num(data) # remove NaNs and Infs
    secs = len(data)/300
    samps = int(secs*250)
    data = scipy.signal.resample(data, samps)
    data = data[-1000:]
    data = data - np.mean(data)
    sdscaler = StandardScaler()
    data = sdscaler.fit_transform(data[:, np.newaxis])
    train[idx] = data.T

csvfile = list(csv.reader(open(DATA_PATH + 'signals/training2017/REFERENCE.csv')))
classes = ['N', 'O', 'A', '~']
for row in range(len(csvfile)):
    train[row] = np.append(train[row], (classes.index(csvfile[row][1])))
train = pd.DataFrame(train)

N = train.loc[train[1000] == 0]
O = train.loc[train[1000] == 1]
A = train.loc[train[1000] == 2]
S = train.loc[train[1000] == 3]

count = int(len(N) * 0.03 + len(O) * 0.03 + len(A) * 0.03)
N = resample(N, replace=False, n_samples=int(len(N)*0.97), random_state=42)
train_N, test_N = train_test_split(N, test_size=0.2, random_state=42)
O = resample(O, replace=False, n_samples=int(len(O)*0.97), random_state=42)
train_O, test_O = train_test_split(O, test_size=0.2, random_state=42)
A = resample(A, replace=False, n_samples=int(len(A)*0.97), random_state=42)
train_A, test_A = train_test_split(A, test_size=0.2, random_state=42)
S = resample(S, replace=True, n_samples=count + len(S), random_state=42)
train_S, test_S = train_test_split(S, test_size=0.2, random_state=42)
train = pd.concat([train_N, train_O, train_A, train_S], ignore_index=True)
test = pd.concat([test_N, test_O, test_A, test_S], ignore_index=True)

train.to_csv(DATA_PATH + 'signals/cinc_train.csv', sep=',', index=False)
test.to_csv(DATA_PATH + 'signals/cinc_test.csv', sep=',', index=False)
