# Fastapi-dockerized-boilerplate

This project contains a simple dockerised fastapi example <br>

## Installation

Follow these steps to set up and run the project : <br>

1. Create a Python virtual environment: <br>


 ```python3 -m venv fastapi ``` <br> 
 
 ```cd fastapi ``` <br>

2.Activate the virtual environment: <br>
 ```source bin/activate ``` <br>

3.Install FastAPI and Uvicorn: <br>
 ```python3 -m pip install fastapi uvicorn[standard] ``` <br>

4.Run the Docker container: <br>
 ```sudo docker run -p 8080:80 my-fastapi-app ``` <br>

5.Install Docker compose: <br>
 ```sudo apt install docker-compose ``` <br>
 
6.Run the Docker compose file: <br>
 ```sudo docker-compose up ``` <br>

## Usage
Once the application is running, you can access the API documentation at: <br>

http://localhost:8080/docs 