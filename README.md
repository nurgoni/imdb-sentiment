# Sentiment Analysis ML App with Docker

## Table of Contents
- [Project Description](#project-description)
- [Getting Started with Docker](#getting-started-with-docker)

## Project Description
This repository contains a simple machine learning application for sentiment analysis of the IMDb dataset. The goal of the project is to containerize the application using Docker, providing a portable and reproducible environment for running the sentiment analysis model.

The sentiment analysis model predicts whether a given movie review has a positive or negative sentiment based on the text content of the review. The focus of this repository is primarily on Docker practices and not on maximizing model accuracy or complexity.

## Getting Started with Docker
To get started with the ML app using Docker, follow these steps:

### Prerequisites
Make sure you have Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).

### Build the Docker Image
1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Build the Docker image:
    ```bash
    docker build -t sentiment-analysis-app .
    ```

### Run Docker Container
Once the Docker image is built successfully, you can run the container:
```bash
docker run -p 8080:8080 sentiment-analysis-app
```
This command runs the Docker container and maps port 8080 on your local machine to port 8080 inside the container, where the ML app is hosted.

### Access the sentiment analysis app

Open your web browser and go to `http://localhost:8080` to access the sentiment analysis app. You should see instructions on how to send requests to the API for sentiment analysis.