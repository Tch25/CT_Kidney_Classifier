
#choose the environment in which we will run our code
FROM python:3.10.6-slim

#Set a working directory with any name
WORKDIR /app

#copy the requirement files in the current directory (/app)
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

#Copy all the code here
COPY . .

#open port 8000 for traffic
EXPOSE 8080

#cOMMAND TO START THE api
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
