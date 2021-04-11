# Chatbot
Chatbot designed to provide customer service for an E-commerce. You can ask it questions concerning o
pening hours, product catalog, payment methods, delivery and return policy. The bot is trained in Danish, 
yet it can easily be modified to other languages or task by editing the intents.json file. 

<h2> Requirements </h2>
First setup a virtual environment which is used by Django to execute an application.

In order to run the Chatbot, you will need to install django, django-channels and associated libraies 
for the chat service as well is torch, numpy and nltk for the bot functionality. If you have pip installed 
it can be done by running these following commands:

```
pip install django
pip install channels
pip install channels_redis
pip install nltk
pip install torch 
```

<h2> How to run </h2>

To run the application you simply execute the command which starts a server with the appication:

```
python manage.py runserver
```

<h2> Screenshot of application </h2>
<img src="https://github.com/montymse/Chatbot/blob/master/Frontpage.png" width="400" height="450" />
<img src="https://github.com/montymse/Chatbot/blob/master/Chat.png" width="400" height="450" />
