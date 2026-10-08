import os
import time

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Posso buscar voos em dinheiro ou milhas. "
        "Envie origem, destino, data e janela de flexibilidade."
    )


if not TOKEN or TOKEN == "dummy-token":
    print("TELEGRAM_BOT_TOKEN not configured. Bot disabled for this environment.")
    while True:
        time.sleep(60)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
