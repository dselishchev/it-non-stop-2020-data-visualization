#!/bin/bash
uvicorn --interface wsgi --host 0.0.0.0 --port ${PORT} main:app
