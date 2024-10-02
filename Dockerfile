FROM python:3.12
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/

# Start a shell session to debug
CMD ["/bin/bash"]

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]