from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
COMPANY_NAME = "DANIEL TECH SOLUTIONS"
CONTACT_PHONE = "+234-903-288-5936"
CONTACT_EMAIL = "ogahdans@gmail.com"


# 🔴 REPLACE THESE
BOT_TOKEN = "8501448057:AAHTQrSMhDd6DwDC6p9ZLwEVomINw1gphfI"
ADMIN_ID = 5268298897  # paste your numeric Telegram ID here

# -------- COMMAND FUNCTIONS --------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"👋 Welcome to *{COMPANY_NAME}*\n\n"
        "We provide smart digital solutions to help businesses grow faster.\n\n"
        "📌 What you can do here:\n"
        "• View our services & pricing\n"
        "• Place an order\n"
        "• Get quick support\n\n"
        "👇 Available Commands:\n"
        "/price – View price list\n"
        "/order – Place an order\n"
        "/help – How this bot works\n\n"
        "We’re glad to have you here 😊"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"ℹ️ *{COMPANY_NAME} – Help Center*\n\n"
        "How to use this bot:\n"
        "1️⃣ Use /price to view services\n"
        "2️⃣ Use /order to place an order\n"
        "3️⃣ Our team will contact you shortly\n\n"
        f"📞 Phone: {CONTACT_PHONE}\n"
        f"📧 Email: {CONTACT_EMAIL}",
        parse_mode="Markdown"
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💼 *{COMPANY_NAME} – Price List*\n\n"
        "🤖 Telegram Bot Setup – ₦50,000\n"
        "📱 WhatsApp Bot Setup – ₦60,000\n"
        "🌐 Website Design – ₦150,000\n"
        "🛠 Monthly Maintenance – ₦10,000\n\n"
        "Use /order to get started ✅",
        parse_mode="Markdown"
    )


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    await update.message.reply_text(
        f"✅ *Order Received by {COMPANY_NAME}*\n\n"
        "Please send the following details:\n\n"
        "• Service Needed:\n"
        "• Your Budget:\n"
        "• Phone Number:\n\n"
        "Our team will contact you shortly.",
        parse_mode="Markdown"
    )

    admin_message = (
        f"📥 *NEW ORDER – {COMPANY_NAME}*\n\n"
        f"👤 Name: {user.first_name}\n"
        f"🔗 Username: @{user.username}\n"
        f"🆔 User ID: {user.id}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=admin_message,
        parse_mode="Markdown"
    )

    # Notify admin
    admin_message = (
        "📥 NEW ORDER ALERT\n\n"
        f"👤 Name: {user.first_name}\n"
        f"🔗 Username: @{user.username}\n"
        f"🆔 User ID: {user.id}\n"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_message)

# -------- BOT SETUP --------

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("order", order))

print("✅ Business bot is running...")
app.run_polling()
