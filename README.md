
---

# 🚗 **Vehicle Project**

Welcome to the **Vehicle Project**! This repository demonstrates an end-to-end machine learning pipeline that incorporates **data ingestion**, **data validation**, **model training**, and **CI/CD integration** for automated deployments.

This guide will help you get started with setting up and running the project on your local machine or cloud environment. 

---

## 📚 Table of Contents

1. [Project Setup](#project-setup)
2. [MongoDB Setup](#mongodb-setup)
3. [Logging, Exception Handling, and Notebooks](#logging-exception-handling-and-notebooks)
4. [Data Ingestion](#data-ingestion)
5. [Data Validation, Transformation & Model Trainer](#data-validation-transformation--model-trainer)
6. [AWS Services Setup](#aws-services-setup)
7. [Model Evaluation & Pusher](#model-evaluation--pusher)
8. [Prediction Pipeline](#prediction-pipeline)
9. [CI/CD Setup](#cicd-setup)
10. [Additional Setup](#additional-setup)

---

## 🛠️ Project Setup

### 1. **Create Project Template**
- Run the `template.py` script to generate the project structure.

### 2. **Configure `setup.py` & `pyproject.toml`**
- Edit `setup.py` and `pyproject.toml` to import local packages as described in `crashcourse.txt`.

### 3. **Set Up Virtual Environment & Install Dependencies**
1. Create and activate a virtual environment:

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
```

2. Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Check installed packages:

```bash
pip list
```

---

## 🗄️ MongoDB Setup

### 4. **Sign Up for MongoDB Atlas**
- Create a MongoDB Atlas account and set up a new project.
- Deploy a new cluster with the M0 service tier.

### 5. **Create Database User & Access**
- Create a database user with a username and password.
- In the "Network Access" section, add `0.0.0.0/0` to allow connections from anywhere.

### 6. **Get Connection String**
- Navigate to "Project > Cluster" and get the connection string. Replace the placeholder password with your own.

### 7. **Set Up Jupyter Notebook**
- Create a `notebook` folder and add a `mongoDB_demo.ipynb` notebook.
- Push the dataset to MongoDB from within the notebook.

### 8. **Verify MongoDB Data**
- Browse your collection on MongoDB Atlas and verify your data is in key-value format.

---

## 🔧 Logging, Exception Handling, and Notebooks

### 9. **Logger & Exception Handling**
- Write a `logger.py` file for logging and an `exception.py` file for handling errors.
- Test both in the `demo.py` script.

### 10. **EDA & Feature Engineering**
- Create and add notebooks for **Exploratory Data Analysis (EDA)** and **Feature Engineering**.

---

## 💾 Data Ingestion

### 11. **Set Up Data Ingestion**
1. Define constants in `constants/__init__.py`.
2. Implement the MongoDB connection function in `configuration.mongo_db_connections.py`.
3. Fetch data from MongoDB in the `data_access` folder and transform it into a dataframe.

### 12. **Configure MongoDB URL**
- On **Mac/Linux**, set the MongoDB connection URL in the terminal:

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>......"
```

- On **Windows**, set it through the Environment Variables UI or terminal.

---

## 🔍 Data Validation, Transformation & Model Trainer

### 13. **Data Validation**
- Complete the implementation of the **Data Validation** component by referencing the `utils.main_utils.py` and `config.schema.yaml` files.

### 14. **Data Transformation**
- Implement the **Data Transformation** component and add the `estimator.py` file to the `entity` folder.

### 15. **Model Trainer**
- Add the model training logic to the `estimator.py` file and implement the **Model Trainer** component.

---

## ☁️ AWS Services Setup

### 16. **Set Up AWS IAM User**
1. Log in to the AWS Console and create a new IAM user named `firstproj`.
2. Attach the `AdministratorAccess` policy and download the **Access Keys** CSV.

### 17. **Set Environment Variables**
1. Set the environment variables in your terminal:

```bash
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```

2. Verify with:

```bash
echo $AWS_ACCESS_KEY_ID
```

### 18. **Create S3 Bucket**
- Create an S3 bucket named `my-model-mlopsproj` in **us-east-1** region and ensure public access is enabled.

### 19. **Configure AWS S3 in Project**
- Implement code to interact with AWS S3 for storing models and other artifacts.

---

## 🏆 Model Evaluation & Pusher

### 20. **Model Evaluation**
- Implement logic to evaluate model performance based on a predefined threshold.

### 21. **Model Pusher**
- Set up functionality to push the trained model to an S3 bucket for deployment.

---

## 🚀 Prediction Pipeline

### 22. **Set Up Prediction Pipeline**
1. Develop the prediction pipeline in `app.py`.
2. Create `static` and `templates` directories to build the frontend for serving predictions.

---

## 🔄 CI/CD Setup

### 23. **Docker & GitHub Actions Setup**
1. Set up the `Dockerfile` and `.dockerignore`.
2. Create GitHub Actions workflows under `.github/workflows/aws.yaml` to automate the CI/CD pipeline.
3. Set up **AWS ECR** to store Docker images and configure a self-hosted runner on **EC2**.

### 24. **EC2 Setup & Docker Installation**
1. Launch an **EC2 instance** with Ubuntu.
2. Install **Docker** on the EC2 machine:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### 25. **Connect GitHub to EC2**
- Set up a self-hosted GitHub Actions runner on your EC2 instance by following the on-screen instructions.

### 26. **Activate EC2 Port 5000**
- Edit security groups to allow inbound traffic on **port 5000** for your application.

---

## 🔧 Additional Setup

### 27. **Set Up GitHub Secrets**
- Go to **GitHub > Settings > Secrets and Variables** and add the following secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_DEFAULT_REGION`
  - `ECR_REPO`

### 28. **Access the Prediction App**
- Once deployed, access the prediction app via the **EC2 public IP**: `http://<public-ip>:5000`.

---

## 📈 Conclusion

The **Vehicle Project** provides a comprehensive example of a complete machine learning pipeline with end-to-end deployment. You’ve successfully implemented data ingestion, validation, transformation, model training, and deployment with CI/CD using **MongoDB**, **AWS**, **Docker**, and **GitHub Actions**.

---

## 📝 Contributions

Feel free to fork, improve, and submit issues or pull requests. Contributions are welcome!

---

## 📱 Connect with Me

- [GitHub](https://github.com/karsworld)
- [LinkedIn](https://www.linkedin.com/in/karuna-prasanthi-kp/)

---
