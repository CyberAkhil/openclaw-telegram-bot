# OpenClaw Telegram Bot - Deployment Guide

This guide provides instructions for setting up and deploying the OpenClaw Telegram Bot on Microsoft Azure.

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Telegram Bot Token (from @BotFather on Telegram)
- OpenClaw AI API Key
- Microsoft Azure Account with:
  - Subscription ID
  - Resource Group
  - Virtual Machine or App Service for hosting

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/CyberAkhil/openclaw-telegram-bot.git
cd openclaw-telegram-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your actual credentials:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
OPENCLAW_API_KEY=your_openclaw_api_key
AZURE_SUBSCRIPTION_ID=your_subscription_id
AZURE_RESOURCE_GROUP=your_resource_group
AI_MODEL=gemini-pro
```

### 5. Run the Bot Locally

```bash
python src/bot.py
```

## Azure Deployment

### 1. Create Azure Resources

```bash
# Set variables
RESOU RCEGROUP="openclaw-rg"
LOCATION="eastus"
VMNAME="openclaw-vm"

# Create resource group
az group create --name $RESOURCEGROUP --location $LOCATION
```

### 2. Deploy to Azure App Service

```bash
# Create App Service Plan
az appservice plan create \
  --name openclaw-plan \
  --resource-group $RESOURCEGROUP \
  --sku B1 \
  --is-linux

# Create Web App
az webapp create \
  --resource-group $RESOURCEGROUP \
  --plan openclaw-plan \
  --name openclaw-bot \
  --runtime "PYTHON|3.9"
```

### 3. Deploy Code to Azure

```bash
# Using Git deployment
az webapp up \
  --name openclaw-bot \
  --resource-group $RESOURCEGROUP \
  --runtime "python|3.9"
```

### 4. Configure Environment Variables in Azure

```bash
az webapp config appsettings set \
  --resource-group $RESOURCEGROUP \
  --name openclaw-bot \
  --settings \
    TELEGRAM_BOT_TOKEN="your_bot_token" \
    OPENCLAW_API_KEY="your_api_key" \
    AZURE_SUBSCRIPTION_ID="your_subscription_id" \
    AZURE_RESOURCE_GROUP="$RESOURCEGROUP"
```

## Docker Deployment (Optional)

### 1. Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "src.bot"]
```

### 2. Build and Push to Azure Container Registry

```bash
az acr build --registry openclawregistry --image openclaw-bot:latest .
```

### 3. Deploy Container to Azure Container Instances

```bash
az container create \
  --resource-group $RESOURCEGROUP \
  --name openclaw-bot \
  --image openclawregistry.azurecr.io/openclaw-bot:latest \
  --environment-variables TELEGRAM_BOT_TOKEN="your_token" OPENCLAW_API_KEY="your_key"
```

## Monitoring and Logs

### View Application Logs

```bash
# Stream logs in real-time
az webapp log tail \
  --name openclaw-bot \
  --resource-group $RESOURCEGROUP
```

### Monitor Performance

```bash
# Check resource usage
az monitor metrics list \
  --resource "/subscriptions/{subscription}/resourceGroups/{resource-group}/providers/Microsoft.Web/sites/openclaw-bot" \
  --metric "Requests,Errors,CPU"
```

## Troubleshooting

### Bot not responding

1. Check bot token is correct
2. Verify Azure VM/App Service is running
3. Check firewall rules allow outbound connections
4. Review application logs for errors

### Connection issues with OpenClaw API

1. Verify API key is valid
2. Check API endpoint is accessible
3. Review network security groups in Azure
4. Check IP whitelist in OpenClaw settings

## Scaling and Optimization

### Horizontal Scaling (Multiple Instances)

```bash
az appservice plan update \
  --name openclaw-plan \
  --resource-group $RESOURCEGROUP \
  --sku "S1"

az webapp up-to-date --instance-count 2
```

### Enable Auto-scaling

```bash
az monitor autoscale create \
  --resource-group $RESOURCEGROUP \
  --resource-type "Microsoft.Web/serverFarms" \
  --resource-name openclaw-plan \
  --min-count 1 \
  --max-count 3
```

## Security Considerations

1. Use Azure Key Vault for secrets management
2. Enable SSL/TLS for all communications
3. Set up firewall rules to restrict access
4. Implement rate limiting for API calls
5. Regular security updates for dependencies
6. Monitor and log all bot activities

## Maintenance

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Backup Configuration

```bash
# Export current settings
az webapp config appsettings list \
  --name openclaw-bot \
  --resource-group $RESOURCEGROUP > backup.json
```

## Support

For issues or questions:
- Check GitHub Issues: https://github.com/CyberAkhil/openclaw-telegram-bot/issues
- Review Azure documentation: https://docs.microsoft.com/azure/
- Contact OpenClaw support for API-related issues
