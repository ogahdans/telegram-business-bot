from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8501448057:AAHTQrSMhDd6DwDC6p9ZLwEVomINw1gphfI"
ADMIN_ID = 5268298897  # replace with your Telegram numeric ID

COMPANY_NAME = "DANIEL TECH SOLUTIONS"
CONTACT_PHONE = "+234-903-288-5936"
CONTACT_EMAIL = "ogahdans@gmail.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 Welcome to {COMPANY_NAME}\n\n"
        "We provide smart digital solutions to help businesses grow.\n\n"
        "Commands:\n"
        "/price – View services\n"
        "/order – Place an order\n"
        "/help – Get help"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"{COMPANY_NAME} Help Center\n\n"
        "1️⃣ Use /price to see services\n"
        "2️⃣ Use /order to place an order\n\n"
        f"📞 {CONTACT_PHONE}\n"
        f"📧 {CONTACT_EMAIL}"
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Price List\n\n"
        "🤖 Telegram Bot Setup – ₦50,000\n"
        "📱 WhatsApp Bot Setup – ₦60,000\n"
        "🌐 Website Design – ₦150,000\n\n"
        "Use /order to continue"
    )


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = user.username if user.username else "No username"

    await update.message.reply_text(
        "✅ Order received!\n\n"
        "Please send:\n"
        "• Service Needed\n"
        "• Budget\n"
        "• Phone Number"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "📥 NEW ORDER\n\n"
            f"👤 Name: {user.first_name}\n"
            f"🔗 Username: {username}\n"
            f"🆔 ID: {user.id}"
        )
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("order", order))

    print("✅ Bot is running on Render...")
    app.run_polling()


if __name__ == "__main__":
    main()

