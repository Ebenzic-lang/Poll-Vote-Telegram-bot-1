from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8647237147:AAGLTtPLMTx_Hp_iO8PG6A6MdhHCxCkDwGY"

# MAIN MENU
main_menu = ReplyKeyboardMarkup(
    [["START", "REPORT"], ["NOVA", "SAFECHECK"]],
    resize_keyboard=True
)

# START FLOW MENU
start_menu = ReplyKeyboardMarkup(
    [["🚀 First step"], ["👤 My profile"], ["🌐 Back to NOVA"]],
    resize_keyboard=True
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "DD PROTOCOL uses a gamified interaction model.\n\n"
        "Any associations belong to the brand narrative only.\n\n"
        "Click I AGREE to continue.",
        reply_markup=ReplyKeyboardMarkup([["I AGREE"]], resize_keyboard=True)
    )

# HANDLE ALL BUTTONS
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "I AGREE":
        await update.message.reply_text(
            "✅ Profile linked\n\n"
            "NOVA access is active.\n"
            "Your profile is now connected.\n\n"
            "Take the first step to start growing your profile.",
            reply_markup=main_menu
        )

    elif text == "START":
        await update.message.reply_text(
            "Choose your next action:",
            reply_markup=start_menu
        )

    elif text == "🚀 First step":
        await update.message.reply_text("You are starting your journey...")

    elif text == "👤 My profile":
        await update.message.reply_text("Profile details loading...")

    elif text == "🌐 Back to NOVA":
        await update.message.reply_text(
            "Back to main menu",
            reply_markup=main_menu
        )

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
