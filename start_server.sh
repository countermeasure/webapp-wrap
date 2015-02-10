#!/bin/bash

# A script to start a Gunicorn server for a webapp


#Set these variables
PROJECT_NAME="project"
PROJECT_DIR="path/to/the/project"
VIRTUALENVWRAPPER_DIR="/path/to/the/virtualenvwrapper.sh/file"
VIRTUALENV_NAME="virtualenv"
PORT="8001"


echo "#####################################################################"
echo "## The Gunicorn server for $PROJECT_NAME is starting."
echo "#####################################################################"
echo

cd "$PROJECT_DIR"
source "$VIRTUALENVWRAPPER_DIR"
workon "$VIRTUALENV_NAME"
gunicorn "$PROJECT_NAME".wsgi --bind 127.0.0.1:"$PORT" --daemon
