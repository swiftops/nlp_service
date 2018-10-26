#!/bin/sh
echo "Starting server"
#python -m rasa_core.run -d train_model/models/dialogue -u train_model/models/current/nlu \
#    --port 5003 --credentials train_model/credentials.yml

python -m rasa_utils.bot -d train_model/models/dialogue -u train_model/models/current/nlu \
    --port 5003