#!/bin/sh
echo "Starting server"
python -m rasa_core.run -d train_model/models/dialogue -u train_model/models/current/nlu \
    --port 5002 --credentials train_model/credentials.yml
