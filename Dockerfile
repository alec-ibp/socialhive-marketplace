#################
# FINAL BUILDER #
#################

FROM python:3.9.5-slim-buster as builder

# set working directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install OS dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip
RUN pip install --upgrade pip

# Copy project dependencies
COPY ./requirements.txt /code/requirements.txt

# Build project dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /code/wheels -r requirements.txt

###############
# FINAL IMAGE #
###############

FROM python:3.9.5-slim-buster

# set working directory
WORKDIR /code

# Create unprivileged user and group
RUN addgroup --gid 1001 --system app \
    && adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

# Fetch data from builder stage
COPY --from=builder /code/wheels /wheels
COPY --from=builder /code/requirements.txt /code/requirements.txt

# install project dependencies
RUN pip install --no-cache /wheels/*

# Copy project
COPY . /code/

# use the unprivileged user
USER app

EXPOSE 8080

CMD ["python", "main.py"]
