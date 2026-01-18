#Use official python image
FROM python:3.12-slim
#Set working directory
WORKDIR /app
#Copy all files to container
COPY swap2.py .
# Command to run Python file
CMD ["python","swap2.py"]