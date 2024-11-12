# Pull the Python base image
FROM python:3.13-alpine

# Set environment variables to avoid writing pyc files and set the default locale
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

# Create a directory for the application code inside the container
RUN mkdir /code
WORKDIR /code

# Copy the requirements file and install system dependencies for MySQL
COPY requirements.txt /code/

# Update apk repositories and install build dependencies for MySQL
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    pkgconfig \
    mariadb-dev \
    && rm -rf /var/cache/apk/*  # Clean up apk cache

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Install python-dotenv to load environment variables from .env file
RUN pip install python-dotenv

# Expose the port on which Django will run
EXPOSE 8009

# Set the entry point to run the Django development server with migrations
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8009"]
