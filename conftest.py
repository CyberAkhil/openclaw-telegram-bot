"""Pytest configuration and fixtures."""

import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'src'))


@pytest.fixture(scope='session')
def test_config():
    """Provide test configuration."""
    return {
        'test_user_id': 12345,
        'test_token': 'test_token_12345',
        'test_timeout': 5,
        'test_max_retries': 3,
    }


@pytest.fixture(scope='function')
def mock_update():
    """Provide a mock Telegram update object."""
    class MockUser:
        id = 12345
        first_name = 'Test'
        last_name = 'User'
        username = 'testuser'

    class MockChat:
        id = 12345
        type = 'private'

    class MockMessage:
        message_id = 1
        date = 1234567890
        chat = MockChat()
        from_user = MockUser()
        text = 'test message'

    class MockUpdate:
        update_id = 1
        message = MockMessage()

    return MockUpdate()


@pytest.fixture(scope='function')
def mock_context():
    """Provide a mock Telegram context object."""
    class MockContext:
        def __init__(self):
            self.bot_data = {}
            self.user_data = {}
            self.chat_data = {}

    return MockContext()


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        'markers', 'unit: mark test as a unit test'
    )
    config.addinivalue_line(
        'markers', 'integration: mark test as an integration test'
    )
    config.addinivalue_line(
        'markers', 'slow: mark test as slow running'
    )
