FROM python:3.11.1-alpine3.17

ARG UID
ARG GID

RUN apk add --update --no-cache bash git

WORKDIR /mnt/app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt && \
  addgroup -g ${GID} code && adduser -D -G code -u ${UID} code

USER code

CMD while [ true ]; do sleep 3; done
