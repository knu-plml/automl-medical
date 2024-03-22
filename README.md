## The official implementation of the paper "Medical Data Analysis Using AutoML Frameworks"

We support 4 AutoML frameworks [AutoGluon](https://github.com/autogluon/autogluon), [auto-sklearn](https://github.com/automl/auto-sklearn), [AutoKeras](https://autokeras.com/), and [TPOT](https://github.com/EpistasisLab/tpot) for analyzing medical and healthcare data.

Please download the above programs into your environment.

# Get datasets
First of all, you need to execute 'mkdir.py', create directories for the datasets.
```
python3 mkdir.py
```
Next, you need to actively download some datasets(1-cardio, 2-nh_blood, 4-ISIC_2020, 5-MIT-BIH in 'data.py') by yourself because the datasets have some problems like filename encoding, authorization for automatic download on Kaggle, etc.

Please read 'data.py', download datasets, unzip them, and move them to the right locations.

Lastly, execute 'data.py' for data preprocessing.
```
python3 data.py
```

Now, Datasets are ready to be used in AutoMLs.

# Train, Test AutoML
### Note, AutoMLs for medical imaging(MedMNIST(2D, 3D) and ISIC-2020) have some issues, will be updated soon.

The way to train/test AutoML.
```
cd src
python3 main.py --data <dataset_name> --output_root <output_directory> --train_flag <train_flag> --model <model_name>
```

Arguments:<br>
<dataset_name>: Name of the dataset [cardio, nheb, mitbih, cinc] # MedMNIST2D, 3D, and ISIC-2020 will be updated soon.<br>
<output_directory>: Directory where the model and results will be saved.<br>
<train_flag>: Set to 1 for training or 0 for testing.<br>
<model_name>: Choice one of AutoML models [autosklearn, tpot, autokeras, autogluon].
