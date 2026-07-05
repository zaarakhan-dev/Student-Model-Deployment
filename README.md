#  Student Performance Prediction Model Deployment

##  Project Overview

This project demonstrates the complete deployment of a Machine Learning model using **Flask** and **Docker**. The model predicts whether a student is likely to pass based on academic and demographic information.

The project covers the complete deployment pipeline including model training, API creation, Docker containerization, and API testing.

---

##  Features

- Student performance prediction
- Machine Learning model deployment using Flask
- REST API for predictions
- Docker containerization
- API testing using Postman
- Ready for cloud deployment

---

##  Project Structure

```
Student-Model-Deployment
│
├── app.py
├── train_model.py
├── model.pkl
├── StudentsPerformance.csv
├── Dockerfile
├── requirements.txt
├── README.md
├── Report.pdf
│
└── screenshots
    ├── docker-build.png
    ├── docker-running.png
    ├── postman-api.png
    ├── browser-homepage.png
    └── docker-terminal.png   
```

---

##  Dataset

Dataset: Students Performance Dataset

Features used:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score
- Average Score

Target:

- Pass (1)
- Fail (0)

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Docker
- Postman

---

##  Workflow

```
Dataset
    ↓
Preprocessing
    ↓
Model Training
    ↓
Save Model (model.pkl)
    ↓
Flask API
    ↓
Docker Image
    ↓
Docker Container
    ↓
Prediction API
```

---

##  Docker Commands

### Build Docker Image

```bash
docker build -t student-api .
```

### Run Docker Container

```bash
docker run -p 5000:5000 student-api
```

### View Running Containers

```bash
docker ps
```

### View Docker Images

```bash
docker images
```

---

##  API Endpoint

### Home

```
GET /
```

Returns

```
Student Performance Prediction API is Running!
```

---

### Prediction Endpoint

```
POST /predict
```

Example JSON

```json
{
    "gender": 1,
    "race/ethnicity": 2,
    "parental level of education": 3,
    "lunch": 1,
    "test preparation course": 1,
    "math score": 80,
    "reading score": 85,
    "writing score": 90,
    "Average score": 85
}
```

Example Response

```json
{
    "Prediction": 1
}
```

---

##  Results

- Flask API Successfully Created
- Docker Image Successfully Built
- Docker Container Successfully Executed
- Prediction API Successfully Tested Using Postman

---

##  Learning Outcomes

- Machine Learning Model Deployment
- Flask API Development
- Docker Containerization
- REST API Testing
- Production Deployment Basics

---

##  Author

**Zaara Khan**

Summer Internship Project 2026
