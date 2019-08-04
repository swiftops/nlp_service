from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
#from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

# load nlu trained model
interpreter = RasaNLUInterpreter('train_model/models/current/nlu')
# load swift-ent trained agent
agent = Agent.load('train_model/models/dialogue', interpreter=interpreter)

input_channel = SlackInput(
    slack_token="xoxb-449949744724-451493539782-uPGGdm5tiFb4p1hKhqmjlxej",
    slack_channel="@general"
    )

s = agent.handle_channels([input_channel], 5002, serve_forever=True)
