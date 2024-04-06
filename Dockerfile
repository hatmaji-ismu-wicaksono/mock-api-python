FROM python:3.10-alpine

WORKDIR /app
RUN apk update && apk add --no-cache --virtual .update-deps ca-certificates
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
