import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working 👍")
from flask import Flask
import threading

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running"

def run_web():
    import os
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

# Run Telegram bot
async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

# Start both
import asyncio

def start_all():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

threading.Thread(target=start_all).start()

if __name__ == "__main__":
    run_web()

async def refund(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """💸 Refund Processed

Aapka refund initiate kar diya gaya hai.
2–5 working days me aa jayega.

❤️ Team Promodeals
"""
    await update.message.reply_text(message)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("refund", refund))

print("Bot running...")
app.run_polling()
