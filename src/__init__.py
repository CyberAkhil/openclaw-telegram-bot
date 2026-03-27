"""
OpenClaw Telegram Bot - Source package

This package contains the main bot logic and integrations
for connecting OpenClaw AI with Telegram via Microsoft Azure.
"""

__version__ = "1.0.0"
__author__ = "CyberAkhil"
__description__ = "OpenClaw AI integrated with Telegram Bot deployed on Microsoft Azure"

from .bot import main
from .openclaw_integration import OpenClawAI
from .azure_integration import AzureConnector

__all__ = [
    'main',
    'OpenClawAI',
    'AzureConnector',
]
