#!/usr/bin/env bash
cd dirname "$0"
export FLASK_APP=find_a_brew
export FLASK_ENV=development
flask run
