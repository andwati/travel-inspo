from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from . import handlers


def main(token: str) -> None:
    """Run the bot"""
    application = Application.builder().token(token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", handlers.start))

    # Register callback query handler
    application.add_handler(CallbackQueryHandler(handlers.button))

    # Start the bot
    application.run_polling()
