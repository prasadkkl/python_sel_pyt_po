#!/bin/bash

echo "========== Installing dependencies =========="
pip install --upgrade pip
pip install -r requirements.txt

echo "========== Running tests with pytest =========="
pytest --browser_name firefox tests/

echo "========== Test execution finished =========="
