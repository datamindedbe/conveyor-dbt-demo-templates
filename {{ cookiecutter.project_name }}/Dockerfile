FROM public.ecr.aws/dataminded/dbt:v1.5.0

WORKDIR /app
COPY . .

# set environment variables
ENV DBT_PROFILES_DIR="/app"

# install dependencies
RUN dbt deps

# Using DBT ls makes sure that the DBT cache is populated, this allows DBT to use the cache every time it is started up, this will significantly reduce the startup latency of DBT jobs with many models
RUN dbt ls