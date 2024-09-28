# Pull the Python base image
FROM python:alpine


#it create a directory in run time 
RUN mkdir /code

# Set the working directory in the container
WORKDIR /code
copy requirements.txt requirements.txt

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir  -r requirements.txt

# Copy the project files from the host to the container
COPY . /code

# Create a volume for Django's static files
VOLUME /code:/code/Django

# Run Django migrations
RUN python manage.py makemigrations && python manage.py migrate

# Expose port 8009 to access the Django server from outside the container
EXPOSE 8009

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8009"]
