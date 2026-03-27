"""
OpenClaw AI Integration Module
Handles communication with OpenClaw AI API
"""

import os
import aiohttp
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class OpenClawAI:
    """Interface for OpenClaw AI operations."""
    
    def __init__(self, api_key: str, api_url: Optional[str] = None):
        """
        Initialize OpenClaw AI client.
        
        Args:
            api_key: API key for OpenClaw authentication
            api_url: Optional custom API URL
        """
        self.api_key = api_key
        self.api_url = api_url or os.getenv('OPENCLAW_API_URL', 'https://api.openclaw.local')
        self.session = None
        self.model = os.getenv('AI_MODEL', 'gemini-pro')
    
    async def initialize(self):
        """Initialize async HTTP session."""
        if not self.session:
            self.session = aiohttp.ClientSession()
    
    async def close(self):
        """Close async HTTP session."""
        if self.session:
            await self.session.close()
    
    async def get_response(self, prompt: str, max_tokens: int = 1000) -> str:
        """
        Get AI response from OpenClaw.
        
        Args:
            prompt: User prompt/query
            max_tokens: Maximum tokens in response
        
        Returns:
            AI-generated response text
        """
        try:
            await self.initialize()
            
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'prompt': prompt,
                'model': self.model,
                'max_tokens': max_tokens,
                'temperature': 0.7
            }
            
            async with self.session.post(
                f'{self.api_url}/api/generate',
                json=payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('response', 'No response received')
                else:
                    logger.error(f'API error: {response.status}')
                    return f'Error: OpenClaw API returned status {response.status}'
        
        except aiohttp.ClientError as e:
            logger.error(f'Connection error: {e}')
            return 'Error: Unable to connect to OpenClaw API'
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return f'Error: {str(e)}'
    
    async def get_available_models(self) -> list:
        """
        Get list of available AI models.
        
        Returns:
            List of available model names
        """
        try:
            await self.initialize()
            headers = {'Authorization': f'Bearer {self.api_key}'}
            
            async with self.session.get(
                f'{self.api_url}/api/models',
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('models', [])
                return []
        except Exception as e:
            logger.error(f'Error fetching models: {e}')
            return []
    
    async def test_connection(self) -> bool:
        """
        Test connection to OpenClaw API.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            await self.initialize()
            headers = {'Authorization': f'Bearer {self.api_key}'}
            
            async with self.session.get(
                f'{self.api_url}/api/health',
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                return response.status == 200
        except Exception as e:
            logger.error(f'Connection test failed: {e}')
            return False
