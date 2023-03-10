# Marvel-Search
This is a Flask-based backend for search comic in the Marvel API. It is contained within a Docker container for ease of deployment.

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Before you begin, you will need to have the following software installed on your machine:

- Docker
- Python 3
- pip

## Installing
1. Clone this repository:
```bash
git clone https://github.com/guillermoreyesv/Marvel-Search.git
```

2. Navigate to the repository directory:
```bash
cd Marvel-Search
```

3. Copy the .env.example file to .env:
```bash
cp .env.example .env
```
4. Open the .env file and update the values to match your environment.

### Using docker
5. Make docker network
```bash
docker network create --subnet=172.18.0.0/16 marvel-network
```

6. Build the Docker container:
```bash
docker build -t search-comic .
```

7. Run the container:
```bash
docker run -d -p 8000:8000 --network marvel-network --ip 172.18.0.10 --name search-container search-comic 
```

8. Your Marvel-Search should now be up and running in http://127.0.0.1:8000!

### In local

5. Start a virtualenv:
```python
py -m venv .python-version
```

6. Activate virtualenv:
```bash
.\.python-version\Scripts\Activate.ps1
```

7. Install the required packages:
```python
pip install --no-cache-dir -r requirements.txt
```

8. Start the application:
```bash
python run.py
```

9. Your Marvel-Search should now be up and running in http://127.0.0.1:5000!

## Deployment
To deploy this application to a production environment, you will need to follow the steps above, making any necessary modifications to match your environment.

## Built With
- <ins>Flask</ins> - A lightweight Python web framework.
- <ins>Docker</ins> - A platform for building and deploying applications in containers.