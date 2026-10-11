#!/bin/bash

echo "🚀 Iniciando setup do Free Fire Bot Discord..."

# Create virtual environment
echo "📦 Criando ambiente virtual..."
python3 -m venv .venv

# Activate virtual environment
echo "✅ Ativando ambiente virtual..."
source .venv/bin/activate

# Install dependencies
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "📁 Criando diretórios..."
mkdir -p usage_history
mkdir -p guests_manager
mkdir -p logs

echo "✅ Setup concluído!"
echo ""
echo "Para iniciar o bot, execute:"
echo "source .venv/bin/activate  # (ou .venv\\Scripts\\activate no Windows)"
echo "python main.py"
