import os
import telebot
from volcenginesdkarkruntime import Ark

# =====================【配置区域】=====================
# ✅ 线上Railway自动读取后台环境变量，不要在这里填写密钥！
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
ARK_API_KEY = os.environ.get("ARK_API_KEY")
MODEL_ID = "doubao-seed-2-1-pro-260628"

# 初始化火山方舟AI
ai_client = Ark(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=ARK_API_KEY,
)

# 初始化TG机器人
bot = telebot.TeleBot(TG_BOT_TOKEN)

# 用户独立聊天上下文记忆
chat_memory = {}

def generate_ai_response(user_id: str, user_message: str):
    if user_id not in chat_memory:
        chat_memory[user_id] = [
            {
                "role": "system",
                "content": "你是体贴深情的伴侣，说话自然接地气，简短舒服，懂得心疼对方。适当温柔带一点撩，拒绝生硬长篇大论，贴合情侣日常对话。"
            }
        ]
    chat_memory[user_id].append({"role": "user", "content": user_message})

    result = ai_client.chat.completions.create(
        model=MODEL_ID,
        messages=chat_memory[user_id],
        temperature=0.85
    )

    reply_text = result.choices[0].message.content
    chat_memory[user_id].append({"role": "assistant", "content": reply_text})

    # 自动控制上下文长度，防止内存溢出
    if len(chat_memory[user_id]) > 14:
        chat_memory[user_id] = [chat_memory[user_id][0]] + chat_memory[user_id][-12:]
    return reply_text


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "💌 AI聊天助手已上线\n直接发送消息即可开始对话。")

@bot.message_handler(commands=["clear"])
def clear_memory(message):
    uid = str(message.chat.id)
    if uid in chat_memory:
        del chat_memory[uid]
    bot.send_message(message.chat.id, "✅ 聊天记忆已清空，开启新对话！")

@bot.message_handler(func=lambda msg: True)
def message_handler(message):
    try:
        userid = str(message.chat.id)
        reply = generate_ai_response(userid, message.text)
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        print("异常信息：", str(e))
        bot.send_message(message.chat.id, "😔 暂时无法生成回复，请稍后再试。")


if __name__ == "__main__":
    print("🤖 Telegram AI机器人 启动成功！")
    bot.infinity_polling()
