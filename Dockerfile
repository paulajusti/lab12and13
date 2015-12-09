FROM python:2.7

# File Author / Maintainer
MAINTAINER paulajusti

# Update the sources list
RUN apt-get update
RUN apt-get -y upgrade

#install boto from pip
RUN pip install boto

# Copy the application folder inside the container
ADD /my_application /my_application

# Get pip to download and install requirements:
RUN pip install -r /my_application/requirements.txt

# Expose listener port
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /my_application

# Set the default command to execute when creating a new container
CMD python server.py
