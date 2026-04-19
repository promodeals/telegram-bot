import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working 👍")

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
