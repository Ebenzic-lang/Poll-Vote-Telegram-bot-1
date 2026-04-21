from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8647237147:AAFrBDZ7dtA8Qy0ZAjSJf_YQDbC3qQ3A_qg"

main_menu = ReplyKeyboardMarkup(
    [["START", "REPORT"], ["NOVA", "SAFECHECK"]],
    resize_keyboard=True
)

start_menu = ReplyKeyboardMarkup(
    [["First step"], ["My profile"], ["Back to NOVA"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome\nClick I AGREE to continue",
        reply_markup=ReplyKeyboardMarkup([["I AGREE"]], resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "I AGREE":
        await update.message.reply_text("Access granted", reply_markup=main_menu)

    elif text == "START":
        await update.message.reply_text("Choose option", reply_markup=start_menu)

    elif text == "First step":
        await update.message.reply_text("Starting...")

    elif text == "My profile":
        await update.message.reply_text("Profile...")

    elif text == "Back to NOVA":
        await update.message.reply_text("Back", reply_markup=main_menu)

    elif text == "REPORT":
        await update.message.reply_text("Report")

    elif text == "NOVA":
        await update.message.reply_text("NOVA active")

    elif text == "SAFECHECK":
        await update.message.reply_text("Safe check")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
