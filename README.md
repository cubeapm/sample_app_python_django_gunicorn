# New Relic Instrumentation

This branch contains code for New Relic instrumentation.

Hitting an API endpoint will generate the corresponding traces. By default, New Relic agents send data to New Relic servers. However, if an environment variable `NEW_RELIC_HOST` is found, the agents send data to the domain mentioned in this environment variable's value instead of sending to New Relic servers. Thus, by adding the environment variable NEW_RELIC_HOST=<domain_of_cubeapm_server> in the [docker-compose.yml](docker-compose.yml). New Relic agent will send data to your CubeAPM servers instead of New Relic servers.
However, there is one more thing that needs to be taken care of. New Relic agents send data using HTTPS on port 443. However, CubeAPM expects data on port 3130 over HTTP. So, a load balancer (or HTTP reverse proxy) is needed to accept data on HTTPS/443 and forward to CubeAPM on HTTP/3130.

That's it! New Relic agents can now be used to send data to CubeAPM.

+------------------+      +------------------+      +------------------+
|  Application    |       |  Load Balancer  |       |     CubeAPM     |
| +------------+  |  -->  | +------------+  |  -->  | +------------+  |
| |New Relic   |  | HTTPS | |            |  | HTTP  | |            |  |
| |Agent       |  |  443  | |            |  | 3130  | |            |  |
| +------------+  |       | +------------+  |       | +------------+  |
+------------------+      +------------------+      +------------------+


Earlier, we were using a load balancer, but for localhost, we can use **ngrok**. Here are the steps to set it up:

1. Ngrok should be installed – If ngrok is not installed, install it first.

2. Run ngrok on HTTP port 3130 – Execute the following command in the terminal:

    **ngrok http 3130**

3. Copy the ngrok forwarding link – Once ngrok is running, it will provide a forwarding URL like this:

    **Forwarding           https://1977-43-230-105-16.ngrok-free.app -> http://localhost:3130**

Replace <domain_of_cubeapm_server> with this forwarding link (1977-43-230-105-16.ngrok-free.app) – Use this URL in place of <domain_of_cubeapm_server>.

This will allow New Relic agents to connect to the CubeAPM server on localhost via HTTPS.

Refer the project README below for more details.

---

# Python Django Gunicorn Instrumentation

This is a sample app to demonstrate how to instrument Python Django Gunicorn app with **New Relic** and **OpenTelemetry**. It contains source code for the Django app which interacts with various services like Redis, MySQL, etc. to demonstrate tracing for these services. This repository has a docker compose file to set up all these services conveniently.

The code is organized into multiple branches. The main branch has the Django app without any instrumentation. Other branches then build upon the main branch to add specific instrumentations as below:

| Branch                                                                                         | Instrumentation | Code changes for instrumentation                                                                                |
| ---------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------- |
| [main](https://github.com/cubeapm/sample_app_python_django_gunicorn/tree/main)         | None            | -                                                                                                               |
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
