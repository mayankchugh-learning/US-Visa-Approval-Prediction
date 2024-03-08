**US Visa Approval Prediction**

**YouTube URL for Deployment https://youtu.be/p81ouOZVDTs**


**LinkedIn: https://www.linkedin.com/in/mchugh77/**



**🔍 Description for US Visa Approval Prediction for Machine Learning Model - MLOps Project:**

The US Visa Approval Prediction project aims to develop a machine learning model that can accurately predict the approval or rejection of US visa applications. This project adopts a modular coding approach, leveraging various technologies to build an end-to-end solution. The primary technologies used in this project include:

**🐍 Python:** Python, a versatile and widely-used programming language for machine learning, is employed for data preprocessing, feature engineering, and model development.

**📓 Jupyter Notebook:** Jupyter Notebook provides an interactive and collaborative environment to explore and analyze the data, experiment with different algorithms, and fine-tune the model parameters.

**🖥️ Visual Studio Code:** Visual Studio Code, a powerful integrated development environment (IDE), is utilized for writing modular and scalable code. It enables efficient coding practices, debugging, and version control integration with Git, ensuring better collaboration among team members.

**🍃 MongoDB:** MongoDB, a NoSQL document database, is used to store and manage the visa application data. It provides flexibility and scalability for handling large datasets efficiently.

**🐙 GitHub:** GitHub serves as the version control and collaboration platform, allowing team members to work together, track changes, and manage the project's codebase effectively.

**⚡ FastAPI:**  FastAPI, a modern web framework for building APIs, is used to create a robust and scalable API for serving the machine learning model predictions. It offers high performance and automatic documentation generation.

**☁️ AWS S3:**  AWS S3 (Simple Storage Service) is utilized for storing and managing the dataset and other project-related files. It provides secure and scalable cloud storage for easy accessibility and data sharing.

By combining these technologies, the US Visa Approval Prediction project aims to develop a reliable and efficient machine learning model that can assist in predicting the outcome of US visa applications, streamlining the visa approval process, and improving decision-making.


# US-Visa-Approval-Prediction

## Git commands

```bash


git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n visa python=3.8 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements.txt
```


```bash
python app.py
```


### https://www.kaggle.com/datasets/moro23/easyvisa-dataset?resource=download

## Workflow

1. constant
2. config_entity
3. artifact_entity
4. conponent
5. pipeline
6. app.py / demo.py


### Export the  environment variable
```bash

export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID = <AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY = <AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION = <AWS_DEFAULT_REGION>

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject


## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:


	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade -y

	#required

	docker --version

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	docker --version

	sudo usermod -aG docker ubuntu

	newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO	