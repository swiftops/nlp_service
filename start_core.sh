#!/bin/sh
echo "Starting Rasa_Core server with Channel configuration, NLU and Dialogue module"
python -m rasa_core.run -d train_model/models/dialogue -u train_model/models/current/nlu \
    --port 5002 --endpoints train_model/endpoints.yml --credentials train_model/credentials.yml
