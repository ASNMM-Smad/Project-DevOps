FROM python:3.12-rc-alpine3.16
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
RUN ls -l /app
CMD ["python3", "/app/MainScores.py", "&"]
