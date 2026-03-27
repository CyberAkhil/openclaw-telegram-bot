#!/usr/bin/env python3
"""
OpenClaw Telegram Bot - Main Entry Point

Run this script to start the OpenClaw Telegram Bot
Usage: python main.py
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bot import main

if __name__ == "__main__":
    print("Starting OpenClaw Telegram Bot...")
    print("Configuration:")
    print(f"  - Bot Token: {os.getenv('TELEGRAM_BOT_TOKEN', 'NOT SET')[:10]}...")
    print(f"  - OpenClaw API: {os.getenv('OPENCLAW_API_URL', 'NOT SET')}")
    print(f"  - Azure Region: {os.getenv('AZURE_REGION', 'eastus')}")
    print(f"  - AI Model: {os.getenv('AI_MODEL', 'gemini-pro')}")
    print()
    
    try:
        main()
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
