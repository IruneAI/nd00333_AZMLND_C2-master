

# Operationalizing Machine Learning 

The main goal of this project is to configure a cloud-based machine learning **production** model, deploy it, and consume it as well as enable workflows automation via pipelines.

The dataset used for this project is the [BankMarketing](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) based on [UCI BankMarketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing).  It is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The **classification** goal is to predict if the client will subscribe a term deposit (variable y).

The main key steps of this project would be the following ones:

1. Authentication
2. Automated ML Experiment
3. Deploy the best model
4. Enable logging
5. Swagger Documentation
6. Consume the model endpoints
7. Create, Publish and Consume a pipeline

A further documentation and explanations around each main steps will be provided: 15 minutes screencast + all process screenshots.

## Architectural Diagram

The following architectural diagram describes various **stages** that are critical to the overall flow as well as the **input/outputs** of them.

![GitHub pipeline](/starter_files/images/workflow_udacity.png)


## Key Steps

Further explanation on each key steps:
### Step 1: Authentication

This first step consist on allowing the authentication. For that we should create a Service Principal (SP) account and associate it with your specific workspace (allow the access to it). **NOTE: This step is only required if you are using your own Azure account.**

### Step 2: Automated ML Experiment
Once the security is enabled and authentication is completed, we should create our experiment using Automated ML, configure a compute cluster, and use that cluster to run the experiment.

For that we should take these actions:

1. Initialize our workspace.
2. Create a new AutoML run
3. Select and upload desired dataset (*BankMarketing train dataset in our case*)
![datasets_screenshot](/starter_files/images/datasets_screenshot.png)
**Fig1. Registered datasets** 

4. Create a new AutoML experiment.
![automl_run](/starter_files/images/automlconfig.png)

**Fig2. Create automl run config** 

5. Configure and attach our desired compute cluster (*Standard_DS12_v2, min_nodes:1*)
![compute_cluster_creation](/starter_files/images/autml.png)
**Fig3. Create compute cluster** 

6. Configure experiment run (*Classification, Exit criterion 3 hours, Concurrency 5)* and execute it.

![experiment_automl_finished_metrics](/starter_files/images/experiment_automl_finished_metrics.png)
**Fig4. Classification experiment completed** 

7. Identify the best model.
This step allow us to identify the best performance model to be deployed later on. For further metrics details please refer to /images.

![experiment_automl_algorithms](/starter_files/images/experiment_automl_algorithms.png)
**Fig 5. Best model Voting Ensemble with 0.91988 Accuracy** 




### Step 3: Deploy the best model
The best model will be deployed/exposed to later infererence stages.

![best_model_deployment](/starter_files/images/best_model_deployment.png)
**Fig 6. Best model deployment** 

![deployment_sucess](/starter_files/images/deployment_sucess.png)
**Fig 7. Deployment success** 


### Step 4: Enable logging
Once the model is deployed, this step will enable Application Insights (AI) and retrieve useful logs.

![applicacions_insights_enabled](/starter_files/images/applicacions_insights_enabled.png)
**Fig 8. Application Insights enabled** 


![logs](/starter_files/images/logs.png)
**Fig 9. logs.py running** 
![logs](/starter_files/images/deployment_logs.png)
**Fig 10. Deployment logs** 


### Step 5: Swagger Documentation
### Step 6: Consume the model endpoints
### Step 7: Create, Publish and Consume a pipeline

*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
