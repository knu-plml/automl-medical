### Google Cloud AutoML 
1. Login to Google and go to Google Cloud main menu. 

2. Click on 'Go to console'. 
![1](https://github.com/knu-plml/automl-medical/assets/89115326/9dde30f1-6a34-4b5a-9c37-ab69445e6fad)
---
3. Click on 'CREATE OR SELECT A PROJECT'.
![2](https://github.com/knu-plml/automl-medical/assets/89115326/648b12b9-0d01-4e5d-9ec9-0bad0c3f976d)
---
4. Click on 'NEW PROJECT' from the top right corner of screen and put your project name and create.
![3](https://github.com/knu-plml/automl-medical/assets/89115326/c0936f87-9757-41d6-9b6f-ad96b38d1584)
![4](https://github.com/knu-plml/automl-medical/assets/89115326/8a7dd317-2682-476c-8c3e-cd491c03eddc)
---
5. Click on 'CREATE OR SELECT A PROJECT' and select the project you created.
![5](https://github.com/knu-plml/automl-medical/assets/89115326/b099aa0c-8f34-4075-be08-3af61d17aba1)
6. Once when you are in your project, click on the searchbar on the top and search for 'Vertext AI'.
![6](https://github.com/knu-plml/automl-medical/assets/89115326/9301e615-2771-4ebd-9860-53da9356bcd7) 
---
7. Before you start, click on 'ENABLE ALL RECOMMENTED APIS'.
![7](https://github.com/knu-plml/automl-medical/assets/89115326/f2685b36-45f5-47ec-884e-9ef952674465)
---
8. Select 'Dataset' from the 'TOOL' from left of your screen and Click 'CREATE DATASET'.
![8](https://github.com/knu-plml/automl-medical/assets/89115326/25db82f7-c75b-43b3-a582-f19d62301208)
---
10. Select 'TABULAR' tab and select 'Regression/classifation' and click 'CREATE'.
![9](https://github.com/knu-plml/automl-medical/assets/89115326/18075a1c-6715-4b17-8d8d-dd8449d57321)
---
11. Select 'Upload CSV files from your computer' from Select a data source and 'SELECT FILES' and upload your file.(ex:cardio.csv)
![10](https://github.com/knu-plml/automl-medical/assets/89115326/823dae4f-f394-42b9-a742-9c06d5e6a6be)
---
12. Select your Cloud Storage path by clicking 'BROWSE'. There will be a bucket that generated autometically. Click on your bucket from 'Buckets' list and click 'SELECT' and click 'CONTINUE'.
![11](https://github.com/knu-plml/automl-medical/assets/89115326/63842c1b-e47d-4a17-aff8-032525cf0cf1)
---
13. Click 'TRAIN NEW MODEL' from left side of you screen and select 'Other'.
![12](https://github.com/knu-plml/automl-medical/assets/89115326/a6814c82-ce8b-420d-b36b-eb6ca2039a19)
---
14. From 'Training method', select AutoML and 'CONTINUE'.
![13](https://github.com/knu-plml/automl-medical/assets/89115326/10e3fa70-4cde-482a-aeb8-268219707db7)
---
15. From 'Model detail', Select the target column(cardio) and 'CONTINUE'.
![14](https://github.com/knu-plml/automl-medical/assets/89115326/168dcc7c-308f-44d2-8a20-4f281b88c013)
---
* Note: If you click 'ADVANCED OPTIONS', it is possible to adjust data split.
![15](https://github.com/knu-plml/automl-medical/assets/89115326/b4fffc08-2fb1-4d50-a81b-69594dc6f3a5)
---
16. Click 'CONTINUE'
![16](https://github.com/knu-plml/automl-medical/assets/89115326/2f9b27f5-862b-47c7-b8bf-0c908e5b49f6)
---
17. From 'Training options' Select all feature columns that is necessary and 'CONTINUE'
![17](https://github.com/knu-plml/automl-medical/assets/89115326/c1faa0b7-1f11-416f-b772-426e7f059d32)
---
18. From 'Compute and Pricing', put '1' for 'Budget' and click 'START TRAINING'.
![18](https://github.com/knu-plml/automl-medical/assets/89115326/ab6f5421-6039-4089-8bf5-4c9c9352a7d1)
---
19. You can check your training by clicking 'Training' from 'TOOLS' in 'MODEL DEVELOPEMNT' section. After training is finished, click on the finished training
![20](https://github.com/knu-plml/automl-medical/assets/89115326/1103f4b1-2b6c-4825-9871-a00173cfd60b)
---
20. Check the result
![19](https://github.com/knu-plml/automl-medical/assets/89115326/abb65612-60b3-4efb-b2c8-5ffb578503b4)
