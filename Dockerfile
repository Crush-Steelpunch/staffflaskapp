FROM quay.io/bitnami/python:3.10
WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]
