[![Build Status](https://dev.azure.com/swiftops/swiftops/_apis/build/status/swiftops.nlp_service)](https://dev.azure.com/swiftops/swiftops/_build/latest?definitionId=2)

# nlp_service

NLP service for SwiftOps 

Rasa NLU is an open-source natural language processing tool for intent classification and entity extraction in chatbots.
This service is used to implement rasa core nlu for chatops integration with slack.To read more [rasa nlu] (https://rasa.com/docs/nlu/)


# Getting started

## Prerequisites

Install prerequesists by executing following command

```shell
python -m pip install -r requirements.txt
```

## Configuration

Update following configuration files as per your dialog flow needs or start with templates given.
* train_model/stories.md
* train_model/domain.yml
* train_model/nlu.md

Configure credentials for your prefered conversation channel
Note; We have given example of Slack, more on the way
* train_model/credentials.yml

## Training 

train models using folling command

```shell
./train_model/train.sh
```

## Testing

You can test your model on ither command prompt or if you have Jupyter notebook, use train_model/test.ipynb

```shell
./train_model/test_bot.sh
```

## Starting server

Start Server to connect to your configured communication chanel, Slack in this case.

```shell
./start_core.sh
```

your server is started on port 5002
Make your server accessible on the Internet so that Slack can communicate with it.
You need to download ngrok utility for the same.

```shell
ngrok http 5002
```

## Running action server

* Custom action needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.    

* Start the custom action server by running: 

```shell
python -m rasa_core_sdk.endpoint --actions actions.actions
```


Configure Forwarding url in Slack API.
open your slack client and enjoy your conversation.
