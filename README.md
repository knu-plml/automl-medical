### Google Cloud AutoML 
1. Login to Google and go to Google Cloud main menu. 

2. Click on 'Go to console'. 
![alt text](image.png)
3. Click on 'CREATE OR SELECT A PROJECT'.
![alt text](2.JPG)
4. Click on 'NEW PROJECT' from the top right corner of screen and put your project name and create.
![alt text](3.JPG)
![alt text](4.JPG)
5. Click on 'CREATE OR SELECT A PROJECT' and select the project you created.
![alt text](5.JPG)
6. Once when you are in your project, click on the searchbar on the top and search for 'Vertext AI'.
![alt text](6.JPG)
7. Before you start, click on 'ENABLE ALL RECOMMENTED APIS'.
![alt text](7.JPG)
8. Select 'Dataset' from the 'TOOL' from left of your screen and Click 'CREATE DATASET'.
![alt text](8.JPG)
10. Select 'TABULAR' tab and select 'Regression/classifation' and click 'CREATE'.
![alt text](9.JPG)
11. Select 'Upload CSV files from your computer' from Select a data source and 'SELECT FILES' and upload your file.(ex:cardio.csv)
![alt text](10.JPG)
13. Select your Cloud Storage path by clicking 'BROWSE'. There will be a bucket that generated autometically. Click on your bucket from 'Buckets' list and click 'SELECT' and click 'CONTINUE'.
![alt text](11.JPG)
16. Click 'TRAIN NEW MODEL' from left side of you screen and select 'Other'.
![alt text](12.JPG)
17. From 'Training method', select AutoML and 'CONTINUE'.
![alt text](13.JPG)
18. From 'Model detail', Select the target column(cardio) and 'CONTINUE'.
![alt text](14.JPG)
*note: If you click 'ADVANCED OPTIONS', it is possible to adjust data split.
![alt text](15.JPG)
19. Click 'CONTINUE'
![alt text](16.JPG)
19. From 'Training options' Select all feature columns that is necessary and 'CONTINUE'
![alt text](17.JPG)
20. From 'Compute and Pricing', put '1' for 'Budget' and click 'START TRAINING'.
![alt text](18.JPG)
22. You can check your training by clicking 'Training' from 'TOOLS' in 'MODEL DEVELOPEMNT' section. After training is finished, click on the finished training
![alt text](20.JPG)
23. Check the result
![alt text](19.JPG)