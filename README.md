[![Build Status](https://dev.azure.com/swiftops/swiftops/_apis/build/status/swiftops.nlp_service)](https://dev.azure.com/swiftops/swiftops/_build/latest?definitionId=2)

# nlp_service

NLP service for SwiftOps (Work-in-progress)

## Getting started

### Prerequisites

Install prerequesists by executing following command

```shell
python -m pip install -r requirements.txt
```

### Configuration

Update following configuration files as per your dialog flow needs or start with templates given.
*   train_model/stories.md
*   train_model/domain.yml
*   train_model/nlu.md

Configure credentials for your prefered conversation channel
Note; We have given example of Slack, as well as Bot UI, more on the way
*   train_model/credentials.yml

### Training 

train models using folling command

```shell
./train_model/train.sh
```

## Testing

You can test your model on ither command prompt or if you have Jupyter notebook, use train_model/test.ipynb

```shell
./train_model/test_bot.sh
```

## Starting rasa_core server

Start Server to connect to your configured communication chanel, Slack in this case.
You can start the server with ither command line utility or start using bot/bot_listner.py

### using Command line

```shell
./start_core.sh
```

### using python command

```shell
python service.py
```

your server is started on port 5002
Make your server accessible on the Internet so that Slack can communicate with it.
You need to download ngrok utility for the same.

```shell
ngrok http 5002
```

Configure Forwarding url in Slack API.
open your slack client and enjoy your conversation.

## Starting Conversation UI

```shell
python chat_ui/conversation_interface.py
```

your CUI server is started on port 8080