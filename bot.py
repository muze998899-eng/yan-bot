import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "8141203692:AAEh8yYqIwNPC8BXRXb8BL3NUlXFqoEyOec"

bot = telebot.TeleBot(BOT_TOKEN)

love_words = [
    "人海茫茫，遇见你是我最大幸运。",
    "不用事事逞强，在我身边你可以安心做小孩。",
    "平淡日常里，满心期盼和你相伴。",
    "再难熬的夜晚，我都愿意静静听你诉说委屈。",
    "你的喜怒哀乐，时时刻刻牵动我的心绪。",
    "奔赴你，好好拥抱你。"
]


@bot.message_handler(commands=["start"])
def start_msg(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("抽取暖心短句"))

    bot.send_message(
        message.chat.id,
        "哈喽，随时可以抽取暖心句子✨",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda msg: True)
def receive_msg(message):
    text = message.text.strip()

    if text == "抽取暖心短句":
        reply = random.choice(love_words)
        bot.send_message(message.chat.id, reply)
    else:
        bot.send_message(message.chat.id, "点击下方按钮抽取暖心短句哦")


if __name__ == "__main__":
    print("🤖 机器人启动成功！")
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("机器人已停止")
