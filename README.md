## The official implementation of the paper "Medical Data Analysis Using AutoML Frameworks"

Currently, we support four AutoML frameworks [AutoGluon](https://github.com/autogluon/autogluon), [auto-sklearn](https://github.com/automl/auto-sklearn), [AutoKeras](https://autokeras.com/), and [TPOT](https://github.com/EpistasisLab/tpot) for analyzing medical and healthcare data.

To test, download the above programs into your environment.

# Get datasets
First, run 'mkdir.py' to create directories for the datasets.
```
python3 mkdir.py
```
Next, download the datasets (1-cardio, 2-nh_blood, 4-ISIC_2020, 5-MIT-BIH in 'data.py') by yourself, as the datasets have some issues like filename encoding, authorization for automatic download on Kaggle, etc.

Read 'data.py', download the datasets, unzip them, and move them to the right locations.

Finally, run 'data.py' for data preprocessing.
```
python3 data.py
```

Now, the datasets are ready to be used in AutoMLs.

# Train and Test AutoML
### The code for using AutoML for medical imaging (MedMNIST(2D, 3D) and ISIC-2020) has some issues and will be uploaded soon.

The way to train/test AutoML.
```
cd src
python3 main.py --data <dataset_name> --output_root <output_directory> --train_flag <train_flag> --model <model_name>
```

Arguments:<br>
```<dataset_name>```: Name of the dataset [cardio, nheb, mitbih, cinc] # MedMNIST2D, 3D, and ISIC-2020 will be updated soon.<br>
```<output_directory>```: Directory where the model and results will be saved.<br>
```<train_flag>```: Set to 1 for training or 0 for testing.<br>
```<model_name>```: Choose one of the AutoML models [autosklearn, tpot, autokeras, autogluon].
