FROM python:3.12.7-alpine3.20 AS builder

# Copy the requirements file and install dependencies
COPY ../requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

FROM python:3.12.7-alpine3.20

# Set the build arguments
ARG DOCKER_USER=app
ARG DOCKER_USER_ID=1000
ARG DOCKER_GROUP=app
ARG DOCKER_GROUP_ID=1000

# Create a user and group to run our app using the same id as the host user
# This is to avoid permission issues between the host and the container
RUN addgroup -g ${DOCKER_GROUP_ID} ${DOCKER_GROUP} \
    && adduser -D -u ${DOCKER_USER_ID} -G ${DOCKER_GROUP} ${DOCKER_USER}

# Copy the installed dependencies from the builder image
COPY --from=builder /usr/local/bin/black /usr/local/bin/black
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy the source code
COPY ../src /mnt/app/src
COPY ../var /mnt/app/var

# Tell docker that all future commands should run as the app user
USER ${DOCKER_USER}

# Set the working directory
WORKDIR /mnt/app
