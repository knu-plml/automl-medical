@@ -1,27 +1,27 @@
## The official implementation of the paper "Medical Data Analysis Using AutoML Frameworks"

We support 4 AutoML frameworks [AutoGluon](https://github.com/autogluon/autogluon), [auto-sklearn](https://github.com/automl/auto-sklearn), [AutoKeras](https://autokeras.com/), and [TPOT](https://github.com/EpistasisLab/tpot) for analyzing medical and healthcare data.
Currently, we support four AutoML frameworks [AutoGluon](https://github.com/autogluon/autogluon), [auto-sklearn](https://github.com/automl/auto-sklearn), [AutoKeras](https://autokeras.com/), and [TPOT](https://github.com/EpistasisLab/tpot) for analyzing medical and healthcare data.

Please download the above programs into your environment.
To test, download the above programs into your environment.

# Get datasets
First of all, you need to execute 'mkdir.py', create directories for the datasets.
First, run 'mkdir.py' to create directories for the datasets.
```
python3 mkdir.py
```
Next, you need to actively download some datasets(1-cardio, 2-nh_blood, 4-ISIC_2020, 5-MIT-BIH in 'data.py') by yourself because the datasets have some problems like filename encoding, authorization for automatic download on Kaggle, etc.
Next, download the datasets (1-cardio, 2-nh_blood, 4-ISIC_2020, 5-MIT-BIH in 'data.py') by yourself, as the datasets have some issues like filename encoding, authorization for automatic download on Kaggle, etc.

Please read 'data.py', download datasets, unzip them, and move them to the right locations.
Read 'data.py', download the datasets, unzip them, and move them to the right locations.

Lastly, execute 'data.py' for data preprocessing.
Finally, run 'data.py' for data preprocessing.
```
python3 data.py
```

Now, Datasets are ready to be used in AutoMLs.
Now, the datasets are ready to be used in AutoMLs.

# Train, Test AutoML
### Note, AutoMLs for medical imaging(MedMNIST(2D, 3D) and ISIC-2020) have some issues, will be updated soon.
# Train and Test AutoML
### The code for using AutoML for medical imaging (MedMNIST(2D, 3D) and ISIC-2020) has some issues and will be uploaded soon.

The way to train/test AutoML.
```
@@ -33,4 +33,4 @@ Arguments:<br>
<dataset_name>: Name of the dataset [cardio, nheb, mitbih, cinc] # MedMNIST2D, 3D, and ISIC-2020 will be updated soon.<br>
<output_directory>: Directory where the model and results will be saved.<br>
<train_flag>: Set to 1 for training or 0 for testing.<br>
<model_name>: Choice one of AutoML models [autosklearn, tpot, autokeras, autogluon].
<model_name>: Choose one of the AutoML models [autosklearn, tpot, autokeras, autogluon].
0 comments on commit ff8f07c