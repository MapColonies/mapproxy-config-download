FROM python:3.6-alpine3.12
RUN addgroup -S app && adduser -S app -G app
RUN mkdir /app
WORKDIR /app
RUN mkdir downloads
RUN apk update -q --no-cache \
    && apk add -q --no-cache python3 py3-pip
COPY requirements.txt ./
RUN pip3 install -r ./requirements.txt -t /app
RUN apk del py3-pip
COPY . .
RUN chmod +x start.sh
RUN python3 /app/confd/generate-config.py
RUN chown -R app .
USER app:app
CMD ["sh", "start.sh"]
