# which python image to use
FROM python:3.11

# set the working directory to /app
WORKDIR /app

# upgrade the pip to latest version
RUN pip install --no-cache-dir --upgrade pip

# copy the requirements file for dependents

COPY gcp_training/requirements.txt .

# install the requirements from requiremenst file using pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# install the specified packages with special version
RUN pip3 install "xlrd==1.1.0" -t "old_xlrd"

# copy the rest of the working directory content into the container of /app
COPY . .

# Cloud Run requires port 8080
#ENV PORT=8080
#EXPOSE 8080

# run main.py when container launches
CMD ["python", "gcp_training/main.py"]

