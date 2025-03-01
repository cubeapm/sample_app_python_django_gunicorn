# Elastic Instrumentation

This branch contains code for Elastic instrumentation.

By default, hitting an API endpoint will generate a trace, which is sent to CubeAPM. This behavior is controlled via environment variables in [docker-compose.yml](docker-compose.yml).

Refer the project README below for more details.

## Troubleshooting

If the app does not show up in CubeAPM after integration is done, add the below environment variables to check Elastic agent logs.

```shell
# Print Elastic agent logs on screen (also see wsgi.py for additional requirements)
ELASTIC_APM_LOG_FILE=stdout
# Set Elastic agent log level to debug if needed to see detailed logs
#ELASTIC_APM_LOG_LEVEL=debug
```

---

# Python Django Gunicorn Instrumentation

This is a sample app to demonstrate how to instrument Python Django Gunicorn app with **Datadog**, **Elastic**, **New Relic** and **OpenTelemetry**. It contains source code for the Django app which interacts with various services like Redis, MySQL, etc. to demonstrate tracing for these services. This repository has a docker compose file to set up all these services conveniently.

The code is organized into multiple branches. The main branch has the Django app without any instrumentation. Other branches then build upon the main branch to add specific instrumentations as below:

| Branch                                                                                         | Instrumentation | Code changes for instrumentation                                                                                |
| ---------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| [main](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/main)         | None            | -                                                                                                               |
| [datadog](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/datadog) | New Relic       | [main...datadog](https://github.com/cubeapm/sample_app_python_django_gunicorn/compare/main...datadog) |
| [elastic](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/elastic) | New Relic       | [main...elastic](https://github.com/cubeapm/sample_app_python_django_gunicorn/compare/main...elastic) |
| [newrelic](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/newrelic) | New Relic       | [main...newrelic](https://github.com/cubeapm/sample_app_python_django_gunicorn/compare/main...newrelic) |
| [otel](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/otel)         | OpenTelemetry   | [main...otel](https://github.com/cubeapm/sample_app_python_django_gunicorn/compare/main...otel)         |

# Setup

Clone this repository and go to the project directory. Then run the following commands

```
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
docker compose up --build

# Run the following command in a separate terminal to apply the database migrations.
# This is only needed during first-time setup. Repeat executions are harmless though.
source ./bin/activate
python manage.py migrate
```

Django app will now be available at `http://localhost:8000/apis/`.

The app has various API endpoints to demonstrate integrations with Redis, MySQL, etc. Check out [apis/views.py](apis/views.py) for the list of API endpoints.

# Contributing

Please feel free to raise PR for any enhancements - additional service integrations, library version updates, documentation updates, etc.
