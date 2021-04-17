

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

For that we follow this actions:

1. Initialize our workspace.
2. Create a new AutoML run
![automl_run](/starter_files/images/automlconfig.png)

**Fig1. Create automl run config** 

3. Select and upload desired dataset (*BankMarketing train dataset in our case*)
![datasets_screenshot](/starter_files/images/datasets_screenshot.png)
**Fig2. Registered datasets** 

4. Create a new AutoML experiment.
5. Configure and attach our desired compute cluster (*Standard_DS12_v2, min_nodes:1*)
![compute_cluster_creation](/starter_files/images/autml.png.png)
**Fig3. Create compute cluster** 

7. Configure experiment run (*Classification, Exit criterion 3 hours, Concurrency 5)* and execute it.
8. Identify the best model.



### Step 3: Deploy the best model
### Step 4: Enable logging
### Step 5: Swagger Documentation
### Step 6: Consume the model endpoints
### Step 7: Create, Publish and Consume a pipeline

*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
