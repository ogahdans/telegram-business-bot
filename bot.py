from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = "8501448057:AAHTQrSMhDd6DwDC6p9ZLwEVomINw1gphfI"
ADMIN_ID = 5268298897  # your Telegram numeric ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Welcome to Our Business Bot!*\n\n"
        "We offer professional digital services tailored to your needs.\n\n"
        "📞 *Phone:* +2349032885936\n"
        "📧 *Email:* ogahdans@gmail.com\n\n"
        "Use the menu below to get started 👇",
        parse_mode="Markdown"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Help Menu*\n\n"
        "/start – Welcome message\n"
        "/price – View service prices\n"
        "/order – Place an order\n"
        "/contact – Contact details\n"
        "/help – Help menu",
        parse_mode="Markdown"
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 *Our Services & Prices (₦)*\n\n"
        "• Logo Design – ₦20,000\n"
        "• Website Design – ₦150,000\n"
        "• Telegram Bot Development – ₦100,000\n\n"
        "📌 Custom projects are welcome.\n"
        "Use /order to proceed.",
        parse_mode="Markdown"
    )


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 *Place an Order*\n\n"
        "Please type the service you want and any details.\n"
        "An admin will contact you shortly.",
        parse_mode="Markdown"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Contact Us*\n\n"
        "Phone: +234XXXXXXXXXX\n"
        "Email: yourname@email.com\n\n"
        "We respond fast 🚀",
        parse_mode="Markdown"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("contact", contact))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

