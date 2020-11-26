#!/bin/bash
uvicorn --interface wsgi --host 0.0.0.0 --port 8080 main:app
