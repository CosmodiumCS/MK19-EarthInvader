FROM python:3.9-slim

# create app directory in container
RUN mkdir -p /app
WORKDIR /app

# copy source code to container
COPY . /app

# install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# set environment variable
ENV TOKEN=yourtoken

# run the application
CMD ["python3", "main.py"]