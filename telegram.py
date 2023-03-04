from rasa.core.channels.telegram import TelegramInput
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig
from rasa.core.interpreter import NaturalLanguageInterpreter
from rasa.core.utils import configure_file_logging

import logging

logging.basicConfig(level=logging.INFO)

credentials_file = "credentials.yml"
endpoint = EndpointConfig("http://localhost:5005")
interpreter = NaturalLanguageInterpreter.create("models/nlu")
input_channel = TelegramInput(
    credentials_file=credentials_file,
    parse_mode="Markdown"
)
agent = Agent.load("models/dialogue", interpreter=interpreter, action_endpoint=endpoint)

configure_file_logging(agent.log_file)

input_channel.start_polling(agent, debug=True)
