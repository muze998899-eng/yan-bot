import os
import nest_asyncio
nest_asyncio.apply()
import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 读取环境变量填入你的机器人token
BOT_TOKEN = os.getenv("8141203692:AAEh8yYqIwNPC8BXRXb8BL3NUlXFqoEyOec")

# 文案库
love_words = [
    "人海茫茫，遇见你是我最大幸运。",
    "不用事事逞强，在我身边你可以安心做小孩。",
    "平淡日常里，满心期盼和你相伴。",
    "再难熬的夜晚，我都愿意静静听你诉说委屈。",
    "你的喜怒哀乐，时时刻刻牵动我的心绪。",
    "我只想奔赴你，好好拥抱你。"
]

blind_box = [
    "❤️今日心愿：累了就好好歇息，别硬扛",
    "🌹小寄语：愿所有疲惫都会慢慢消散",
    "💌悄悄话：我一直惦记着你",
    "✨好运卡：烦恼远离，万事顺心"
]

makeup_words = [
    "不必追求完美，你的模样我都喜欢",
    "不用勉强自己，舒服自在最重要",
    "不必独自承担，记得身后还有我"
]

# 启动欢迎
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("💌写给妍"), KeyboardButton("🎁爱心盲盒")],
        [KeyboardButton("💖暖心语录"), KeyboardButton("🖼生成图片")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    welcome_text = """🌸 欢迎来到【妍的小世界】
随时和我聊天，把心事慢慢诉说。"""
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# 消息处理
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💌写给妍":
        letter = """💌致 妍：

认识你以后，生活多了独一无二的你。
从前我不善表达，遇见你总想好好照顾你，盼你常常展露笑容。

我知道你独立要强，习惯独自扛下所有疲惫，经常熬夜忙于工作，忽略休息。每次看见，我满心心疼。

我也有很多做得不够好的时候。太在乎你，就容易胡思乱想。
这份敏感不是想要束缚你，只是你在我心中分量太重。

不必凡事硬撑，难过疲惫的时候，我愿意静静陪着你。"""
        await update.message.reply_text(letter)

    elif text == "🎁爱心盲盒":
        msg = random.choice(blind_box)
        await update.message.reply_text(msg)

    elif text == "💖暖心语录":
        msg = random.choice(love_words)
        await update.message.reply_text(msg)

    elif text == "🖼生成图片":
        # 创建简易文字图片
        img = Image.new("RGB", (600,300), color="#222233")
        draw = ImageDraw.Draw(img)
        content = random.choice(makeup_words)
        draw.text((50,120), content, fill="#ffc0cb", font_size=26)
        img.save("temp.png")
        await update.message.reply_photo(photo=open("temp.png", "rb"))

    else:
        await update.message.reply_text("收到啦，我认真看完你的话✨")


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
