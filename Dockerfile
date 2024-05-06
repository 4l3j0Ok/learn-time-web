ARG API_URL=http://localhost:80
# Stage 1: init
FROM python:3.12.3-slim-bullseye as init
# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app/src
COPY ./src /app/src

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

RUN apt-get update && apt-get install -y unzip curl

# Install app requirements and reflex inside virtualenv
COPY requirements.txt .
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Set up environment variables
ENV APP_PATH=/app/src/app
# For frontend to know where to send requests
ENV API_URL=$API_URL

# Export static copy of frontend to /app/.web/_static
RUN reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into slim image 
FROM python:3.12.3-slim-bullseye
WORKDIR /app/src

# User configuration
RUN adduser --disabled-password --home /app reflex

# Copy artifacts from init stage
COPY --chown=reflex --from=init /app/src .

# Copy virtualenv from init stage
COPY --chown=reflex --from=init /app/.venv /app/.venv
USER reflex

# Set up environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV APP_PATH=/app/src/app

CMD reflex run --env prod --backend-only
