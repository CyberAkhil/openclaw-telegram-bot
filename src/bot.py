#!/usr/bin/env python3
"""
OpenClaw Telegram Bot
An integration of OpenClaw AI with Telegram Bot deployed on Microsoft Azure
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openclaw_integration import OpenClawAI
from azure_integration import AzureConnector

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize OpenClaw and Azure
openclaw = OpenClawAI(api_key=os.getenv('OPENCLAW_API_KEY'))
azure = AzureConnector(
    subscription_id=os.getenv('AZURE_SUBSCRIPTION_ID'),
    resource_group=os.getenv('AZURE_RESOURCE_GROUP')
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}!\n"
        "Welcome to OpenClaw Telegram Bot. Send me any message and I'll help you with AI assistance!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
    /start - Start the bot
    /help - Show this help message
    /model - Show available models
    /status - Check system status
    
    Send any message to get AI responses powered by OpenClaw
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and process with OpenClaw AI."""
    user_message = update.message.text
    
    # Show typing indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    try:
        # Get response from OpenClaw AI
        response = await openclaw.get_response(user_message)
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await update.message.reply_text(
            "Sorry, there was an error processing your request. Please try again."
        )

async def model_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show available AI models."""
    models_info = """
    Available AI Models:
    - Gemini Pro (Google)
    - OpenRouter (Multiple models)
    - HuggingFace Transformers
    
    Current model: {}
    """.format(os.getenv('AI_MODEL', 'gemini-pro'))
    await update.message.reply_text(models_info)

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check system status."""
    try:
        status = await azure.get_status()
        await update.message.reply_text(f"System Status: {status}")
    except Exception as e:
        logger.error(f"Error checking status: {e}")
        await update.message.reply_text("Unable to check system status.")

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("model", model_command))
    application.add_handler(CommandHandler("status", status_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
