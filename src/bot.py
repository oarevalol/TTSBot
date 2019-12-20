#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from config.auth import token
from gtts import gTTS
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('TTSBot')


def start(bot, context):
    logger.info('Command received')
    job = context.job
    context.bot.send_message(
        chat_id=bot.message.chat_id,
        text="¡Hi! I'm a bot"
    )

def tts(bot, context):
    text_to_speech = (' '.join(context.args))
    lang = 'es-us'
    tts_object = gTTS(text=text_to_speech, lang=lang)
    tts_object.save("tts.ogg")
    logger.info(f'File created with text: {text_to_speech}')
    audio_file = "tts.ogg"
    context.bot.send_voice(chat_id=bot.message.chat_id, voice=open(audio_file, 'rb'))

if __name__ == '__main__':
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('tts', tts, pass_args=True))

    updater.start_polling()
    updater.idle()