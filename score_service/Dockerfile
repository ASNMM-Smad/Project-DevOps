FROM python:3.12-rc-alpine3.16
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "/app/MainScores.py", "&"]
