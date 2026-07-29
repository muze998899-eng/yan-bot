import nest_asyncio
nest_asyncio.apply()
import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = "8141203692:AAEh8yYqIwNPC8BXRXb8BL3NUlXFqoEyOec"

love_words = [
    "人海茫茫，遇见你是我最大幸运。",
    "不用事事逞强，在我身边你可以安心做小孩。",
    "平淡日常里，满心期盼和你相伴。",
    "再难熬的夜晚，我都愿意静静听你诉说委屈。",
    "你的喜怒哀乐，时时刻刻牵动我的心绪。",
    "奔赴你，好好拥抱你。"
]

def start(update: Update, context):
    buttons = [[KeyboardButton("抽取暖心短句")]]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text("哈喽，随时可以抽取暖心句子✨", reply_markup=keyboard)

def message_handler(update: Update, context):
    text = update.message.text
    if text == "抽取暖心短句":
        msg = random.choice(love_words)
        update.message.reply_text(msg)
    else:
        update.message.reply_text("点击下方按钮抽取暖心短句哦")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    print("机器人启动成功✅")
    updater.start_polling()

if __name__ == "__main__":
    main()
