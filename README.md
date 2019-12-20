# TTSBot

Dockerized Telegram Text to Speech bot

It receives the string ```/tts <sentence>``` and answer with an audio

Available as @ArevaloBot in Telegram

To replicate this bot, follow these instructions:

* Clone this repository
* Create your own bot talknig with @BotFather
* Edit config/auth.py file with the token provided by BotFather
* Run ```docker build -t ttsbot:local .```
* Then ```docker run -d ttsbot:local```

TODO: Support to choose language
