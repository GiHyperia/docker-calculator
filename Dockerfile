# a. Alpine base image (pinned version)
FROM alpine:3.20

LABEL maintainer="YOUR NAME" \
      description="Python calculator configured with environment variables"

# Alpine does not include Python: install it from the Alpine package repository
RUN apk add --no-cache python3

# c. Environment variables consumed by the calculator (defaults, can be overridden with -e)
ENV APP_NAME="Docker Calculator" \
    APP_AUTHOR="Giovana Assis" \
    CALC_OPERATION="add" \
    CALC_NUM1="10" \
    CALC_NUM2="5"

# b. Add the calculator repository (project folder) to the image
WORKDIR /app
COPY . /app

# e. Command executed when the container starts
CMD ["python3", "calculator.py"]
