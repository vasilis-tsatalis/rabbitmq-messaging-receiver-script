# Use an existing docker image as a base
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create directory
RUN mkdir /app

# Copy app.py file
COPY . ./app

#Change working directory
WORKDIR /app

# COPY requirements.txt
COPY ./requirements.txt ./

RUN pip install -r requirements.txt 

EXPOSE 5000

# Tell what to do when it starts as a container
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","5000"]