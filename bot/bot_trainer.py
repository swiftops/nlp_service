# NLU Training Imports
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Core Training Imports
from rasa_core.agent import Agent

# Training NLU Model
training_data = load_data('train_model/nlu.md')
trainer = Trainer(config.load("train_model/nlu_config.yml"))
trainer.train(training_data)
model_directory = trainer.persist('train_model/models')

# Training Core Model
agent = Agent('train_model/domain.yml')
data = agent.load_data('train_model/stories.md')
agent.train(data)
