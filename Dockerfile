FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir boto3 flask

COPY ["python/main.py", "/app/"]
CMD ["python3", "/app/main.py"]
