#!/bin/sh

echo "NLU Training started"
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
echo "NLU Training Completed"

echo "Core training started"
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
echo "Core Training Completed"
