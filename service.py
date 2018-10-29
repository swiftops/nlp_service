from  rasa_utils import bot_server_channel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

# Creating the Interpreter and Agent
def load_agent():
    interpreter = RasaNLUInterpreter("train_model/models/current/nlu")
    agent = Agent.load("train_model/models/dialogue", interpreter=interpreter)
    return agent


# Creating the server
def main_server():
    agent = load_agent()

    channel = bot_server_channel.BotServerInputChannel(agent, port=5003)
    agent.handle_channels([channel], http_port=5002)


main_server()
