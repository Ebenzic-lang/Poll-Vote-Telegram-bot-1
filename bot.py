from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8647237147:AAH8FPtETd5egKHGhmR88k-EYBgIjJxqI-k"

menu_keyboard = ReplyKeyboardMarkup(
    [["START", "REPORT"], ["NOVA", "SAFECHECK"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome.\nClick I AGREE to continue.",
        reply_markup=ReplyKeyboardMarkup([["I AGREE"]], resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "I AGREE":
        await update.message.reply_text(
            "Access granted.",
            reply_markup=menu_keyboard
        )

    elif text == "START":
        await update.message.reply_text("Starting...")

    elif text == "REPORT":
        await update.message.reply_text("Report section")

    elif text == "NOVA":
        await update.message.reply_text("NOVA active")

    elif text == "SAFECHECK":
        await update.message.reply_text("Safe check done")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
