import os
import nest_asyncio
nest_asyncio.apply()
import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# 机器人密钥
BOT_TOKEN = "8141203692:AAEh8yYqIwNPC8BXRXb8BL3NUlXFqoEyOec"

# 情话文案库
love_words = [
    "人海茫茫，遇见你是我最大幸运。",
    "不用事事逞强，在我身边你可以安心做小孩。",
    "平淡日常里，满心期盼和你相伴。",
    "再难熬的夜晚，我都愿意静静听你诉说委屈。",
    "你的喜怒哀乐，时时刻刻牵动我的心绪。",
    "奔赴你，好好拥抱你。"
]

blind_box = [
    "愿：累了就好好歇息，别硬扛",
    "愿：所有疲惫都会慢慢消散",
    "愿：我一直惦记着你",
    "愿：烦恼慢慢远离你"
]

# /start 启动指令
async def start(update: Update, context):
    btn = [[KeyboardButton("抽取暖心短句")]]
    keyboard = ReplyKeyboardMarkup(btn, resize_keyboard=True)
    await update.message.reply_text("哈喽，随时可以抽取暖心句子✨", reply_markup=keyboard)

# 消息响应
async def message_handle(update: Update, context):
    text = update.message.text
    if text == "抽取暖心短句":
        pick = random.choice(love_words)
        await update.message.reply_text(pick)
    else:
        await update.message.reply_text("点击按钮抽取暖心短句哦")

# 主程序
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handle))
    print("机器人启动成功")
    app.run_polling()

if __name__ == "__main__":
    main()
