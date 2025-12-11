from dotenv import load_dotenv
import os
import telebot

load_dotenv()  # Загружаем переменные окружения из .env

# Получение токена и chat id из env
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(TOKEN)

# Чтение текста из файла
with open('input.txt', encoding='utf-8') as file:
    text = file.read().strip()

# Отправляем сообщение в чат
bot.send_message(CHAT_ID, text)

# Нужен будет файл .env с записями
# TELEGRAM_BOT_TOKEN=your_bot_token_here
# CHAT_ID=your_chat_id_here

# Запуск
# pip install python-dotenv pyTelegramBotAPI
# python send_to_telegram.py
