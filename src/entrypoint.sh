#!/bin/bash
gunicorn main:app --bind 0.0.0.0:8011 -k uvicorn.workers.UvicornWorker -w 10
