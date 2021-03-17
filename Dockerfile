FROM python:3.6-alpine3.12
RUN mkdir /app
WORKDIR /app
RUN chgrp -R 0 /app && \
    chmod -R g=u /app
RUN adduser --disabled-password --shell /bin/bash user && addgroup user root
RUN apk update -q --no-cache \
    && apk add -q --no-cache python3 py3-pip
COPY requirements.txt ./
RUN pip3 install -r ./requirements.txt -t /app
RUN apk del py3-pip
COPY . .
RUN chmod +x start.sh
USER user
CMD ["sh", "start.sh"]
