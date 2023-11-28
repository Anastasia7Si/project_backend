FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000