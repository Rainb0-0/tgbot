from asyncio import sleep
import asyncio
from datetime import date
from telebot.async_telebot import AsyncTeleBot
#from models import Admin

bot = AsyncTeleBot("7311979632:AAERWplEO_fUbTZ60YpDhUZafjNu9ICDJmo", parse_mode=None)

FILE_ID = "AgADsBQAAiFUQFA"

EBI = 6360717290

ME = 5213337459

ADMINS = [ME, EBI]

#@bot.message_handler(commands=['add_admin'])
#async def add_admin(message):
#    if message.from_user.id not in ADMINS:
#        await bot.reply_to(message=message, text="You are not an admin bitch")
#        return
#    if message.reply_to_message == None:
#        await bot.reply_to(message=message, text="Reply to a fucker to make them an admin")
#        return
#    new_admin = Admin(id=message.reply_to_message.from_user.id, date=date.today(), chat=0)
#    new_admin.save()
#    for p in Admin.select():
#        print(p.id)

@bot.message_handler(content_types=["animation"])
async def no_none_zarif_gif(message):
    if (message.document.file_unique_id != FILE_ID):
        await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)

@bot.message_handler(func=lambda m : True)
async def heart(message):
    if message.from_user.id in ADMINS and message.text == "قلب":
        messageRepCh = message.chat.id
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        msg = await bot.send_message(text="❤️", chat_id=message.chat.id)
        hearts = ["🧡", "💛", "💚", "🩵", "💙", "💜"]
        for heart in hearts:
            await sleep(0.5)
            await bot.edit_message_text(heart, message_id=msg.message_id, chat_id=messageRepCh)


asyncio.run(bot.polling())
