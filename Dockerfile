FROM python:3.10-alpine

# create app directory in container
WORKDIR /app

# copy only necessary files to container
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# copy the rest of the source code
COPY . .

# set environment variable
ENV TOKEN=yourtoken

# create a non-root user and switch to it
RUN adduser -D myuser
USER myuser

# run the application
CMD ["python3", "src/main.py"]