from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 🔴 PUT YOUR NEW TOKEN HERE (MAKE SURE IT WORKS)
TOKEN = "8636769004:AAGpv03DV4O5uO79Cm-U1npF6lpdxMRXCF8"

# MAIN MENU
main_menu = ReplyKeyboardMarkup(
    [["START", "REPORT"], ["NOVA", "SAFECHECK"]],
    resize_keyboard=True
)

# START FLOW MENU
start_menu = ReplyKeyboardMarkup(
    [["First step"], ["My profile"], ["Back to NOVA"]],
    resize_keyboard=True
)

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "DD PROTOCOL uses a gamified interaction model.\n\n"
        "Click I AGREE to continue.",
        reply_markup=ReplyKeyboardMarkup([["I AGREE"]], resize_keyboard=True)
    )

# HANDLE BUTTONS
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "I AGREE":
        await update.message.reply_text(
            "Profile linked.\nNOVA access active.\n\nChoose an option below:",
            reply_markup=main_menu
        )

    elif text == "START":
        await update.message.reply_text(
            "Choose your next action:",
            reply_markup=start_menu
        )

    elif text == "First step":
        await update.message.reply_text("Starting process...")

    elif text == "My profile":
        await update.message.reply_text("Loading profile...")

    elif text == "Back to NOVA":
        await update.message.reply_text("Back to main menu", reply_markup=main_menu)

    elif text == "REPORT":
        await update.message.reply_text("Report section")

    elif text == "NOVA":
        await update.message.reply_text("NOVA system active")

    elif text == "SAFECHECK":
        await update.message.reply_text("Safety check complete")

# RUN BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
