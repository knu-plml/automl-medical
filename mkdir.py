DATA_PATH='./dataset/'

## EMRs.
os.makedirs(DATA_PATH + 'tabular/', exist_ok=True)
## Medical Image Data.
os.makedirs(DATA_PATH + 'images/', exist_ok=True)
os.makedirs(DATA_PATH + 'images/medmnist', exist_ok=True)

## Biosignal Sensor Dataset.
os.makedirs(DATA_PATH + 'signals/', exist_ok=True)
