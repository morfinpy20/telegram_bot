import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
import time

bot = AsyncTeleBot("8702861148:AAEjK9eLhPzocsPFLR7POc96hFQyuoRbjuk")
target_message = ""
target_chats = set()

@bot.message_handler(commands=['start'])
async def start(message: Message):
    target_chats.add(message.chat.id)
    await bot.reply_to(message, "Бот активен. Группа добавлена")

@bot.message_handler(commands=['set_message'])
async def set_msg(message: Message):
    global target_message
    target_message = message.text.replace("/set_message", "").strip()
    await bot.reply_to(message, f"Сообщение установлено: {target_message}")

async def send_every_15_min():
    while True:
        if target_message and target_chats:
            for chat_id in target_chats:
                try:
                    await bot.send_message(chat_id, target_message)
                except:
                    pass
        await asyncio.sleep(900)

@bot.message_handler(commands=['stop_bot'])
async def stop(message: Message):
    await bot.reply_to(message, "Остановка...")
    exit()

async def main():
    asyncio.create_task(send_every_15_min())
    await bot.infinity_polling()

asyncio.run(main())