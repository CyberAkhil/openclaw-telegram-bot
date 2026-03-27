#!/usr/bin/env python3
"""Main entry point for OpenClaw Telegram Bot."""

import asyncio
import os
import logging
from dotenv import load_dotenv

# Import bot and logging
from src.logging_config import get_logger, LogConfig
from src.bot import OpenClawBot
from src.rate_limiter import RateLimiter, AbuseDetector

# Initialize logging
LogConfig.setup_logging()
logger = get_logger(__name__)

# Load environment variables
load_dotenv()


def main():
    """Main entry point."""
    logger.info("Starting OpenClaw Telegram Bot...")
    
    # Get configuration from environment
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    openclaw_api_key = os.getenv('OPENCLAW_API_KEY')
    openclaw_url = os.getenv('OPENCLAW_INSTANCE_URL')
    
    if not all([bot_token, openclaw_api_key, openclaw_url]):
        logger.error("Missing required environment variables")
        raise ValueError("TELEGRAM_BOT_TOKEN, OPENCLAW_API_KEY, and OPENCLAW_INSTANCE_URL are required")
    
    # Initialize rate limiter
    rate_limiter = RateLimiter(max_requests=10, time_window=60)
    abuse_detector = AbuseDetector()
    
    # Create and start bot
    logger.info(f"Initializing bot with token: {bot_token[:10]}...")
    bot = OpenClawBot(
        token=bot_token,
        openclaw_api_key=openclaw_api_key,
        openclaw_url=openclaw_url,
        rate_limiter=rate_limiter,
        abuse_detector=abuse_detector
    )
    
    logger.info("Bot initialized successfully")
    logger.info("Starting polling...")
    
    # Start the bot
    bot.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
        raise
