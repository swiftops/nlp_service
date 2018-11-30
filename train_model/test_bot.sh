#!/bin/sh
#python -m rasa_core.run -d models/dialogue
echo "Starting bot for testing"
python -m rasa_core.run -d train_model/models/dialogue -u train_model/models/current/nlu