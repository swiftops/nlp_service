#!/bin/sh

echo "NLU Training started"
python -m rasa_nlu.train -c ./train_model/nlu_config.yml --data ./train_model/nlu.md -o ./train_model/models --fixed_model_name nlu --project current --verbose
echo "NLU Training Completed"

echo "Core training started"
python -m rasa_core.train -d ./train_model/domain.yml -s ./train_model/stories.md -o ./train_model/models/dialogue
echo "Core Training Completed"
