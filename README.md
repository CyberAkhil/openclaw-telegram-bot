# OpenClaw Telegram Bot 🤖

A production-ready Telegram bot powered by OpenClaw AI, deployed on Microsoft Azure with support for multiple AI models and real-world conversation handling.

## Overview

This project demonstrates a **practical AI integration** combining OpenClaw (an advanced AI agent framework) with Telegram Bot API. It's deployed on Microsoft Azure VM with SSH tunneling for secure communication, showcasing real-world AI deployment patterns.

## Key Features

- **🧠 OpenClaw AI Integration** - Advanced conversational AI agent capabilities
- **🔄 Multi-Model Support** - Seamless switching between Gemini 2.0 Flash, OpenRouter, and HuggingFace models
- **💬 Telegram Bot Interface** - User-friendly bot commands and conversation handling
- **☁️ Azure Cloud Deployment** - Scalable cloud infrastructure with SSH tunneling
- **🔍 Web Search** - Real-time information retrieval via DuckDuckGo integration
- **📝 Conversation History** - Context-aware responses with stateful conversation management
- **🔐 Environment-Based Config** - Secure credential management with .env configuration

## Architecture

```
Telegram User
    ↓
Telegram Bot API
    ↓
Python Bot Handler (SSH Tunnel)
    ↓
Microsoft Azure VM
    ↓
OpenClaw Agent Framework
    ↓
AI Models (Gemini/OpenRouter/HuggingFace)
    ↓
Response to User
```

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.9+ |
| **Bot Framework** | python-telegram-bot |
| **Cloud Platform** | Microsoft Azure (Ubuntu VM) |
| **AI Engine** | OpenClaw 2026.3.23+ |
| **Models** | Google Gemini, OpenRouter, HuggingFace |
| **Networking** | SSH Tunneling |
| **Configuration** | Environment Variables |

## Installation & Setup

### Prerequisites

- Python 3.9+
- Telegram Bot Token (from BotFather)
- Azure VM or local machine
- OpenClaw API credentials
- At least one AI model API key (Gemini, OpenRouter, or HuggingFace)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/CyberAkhil/openclaw-telegram-bot.git
   cd openclaw-telegram-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

4. **Start the bot**
   ```bash
   python main.py
   ```

## Configuration

Edit `.env` file with the following variables:

```env
# Telegram Configuration
TELEGRAM_BOT_TOKEN=your_token_here

# OpenClaw Configuration
OPENCLAW_API_KEY=your_api_key
OPENCLAW_INSTANCE_URL=your_instance_url

# Azure SSH Configuration
AZURE_VM_HOST=your_azure_vm_ip
AZURE_VM_USER=your_username
AZURE_VM_KEY_PATH=/path/to/ssh/key
AZURE_VM_PORT=22

# AI Model Selection
DEFAULT_MODEL=gemini  # gemini, openrouter, or huggingface
GEMINI_API_KEY=your_gemini_key
OPENROUTER_API_KEY=your_openrouter_key
HUGGINGFACE_API_KEY=your_hf_key
```

See `.env.example` for detailed configuration options.

## Project Structure

```
.
├── src/
│   ├── bot.py                    # Main bot logic
│   ├── openclaw_integration.py   # OpenClaw API wrapper
│   ├── azure_integration.py      # Azure VM SSH handling
│   └── __init__.py
├── main.py                       # Entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # Configuration template
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
├── DEPLOYMENT.md                 # Production deployment guide
├── ROADMAP.md                    # Future features & improvements
├── CONTRIBUTING.md               # Contribution guidelines
├── ACTION_ITEMS.md               # Tracked improvements
└── LICENSE                       # MIT License
```

## Usage

### Bot Commands

- `/start` - Initialize bot and show welcome message
- `/help` - Display available commands
- `/ask <query>` - Send query to OpenClaw AI
- `/search <query>` - Search the web and get AI summary
- `/model <name>` - Switch between AI models
- `/history` - Show conversation history
- `/clear` - Clear conversation history

### Example Conversation

```
User: /ask What is machine learning?

Bot: Machine learning is a subset of artificial intelligence that enables 
systems to learn and improve from experience without explicit programming...
```

## Deployment

### Azure Deployment

For detailed Azure deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Local Development

```bash
python main.py
```

### Docker Deployment (Optional)

```bash
docker build -t openclaw-bot .
docker run --env-file .env openclaw-bot
```

## Future Improvements

See [ROADMAP.md](ROADMAP.md) for planned features including:
- Unit and integration tests
- CI/CD pipeline with GitHub Actions
- Advanced logging system
- Rate limiting and abuse protection
- Structured configuration management for production
- Enhanced error handling and monitoring

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenClaw team for the advanced AI framework
- Telegram Bot API documentation
- Python-telegram-bot community
- Azure documentation and tutorials

---

**Status**: Active Development | **Python**: 3.9+ | **License**: MIT
