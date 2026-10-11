# 🎮 Free Fire Like Bot Discord - Guia do Replit

## ⚙️ Configuração Rápida no Replit

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/User090807/freefire-like-bot-discord.git
```

### Passo 2: Instalar dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Secrets no Replit

1. **Clique no ícone de cadeado** (Secrets) na barra esquerda
2. **Clique em "Create Secret"** e adicione:

#### Secret 1: DISCORD_TOKEN
```
Key: DISCORD_TOKEN
Value: [COLE SEU TOKEN DO BOT AQUI]
```

#### Secret 2: GUILD_ID
```
Key: GUILD_ID
Value: [ID DO SEU SERVIDOR DISCORD]
```

#### Secret 3: ADMIN_IDS
```
Key: ADMIN_IDS
Value: [SEU ID DE USUÁRIO DISCORD]
```

### Passo 4: Executar o bot

Clique em **"Run"** ou execute:
```bash
python main.py
```

Você verá:
```
==================================================
🎮 Free Fire Like Bot Discord
==================================================

✅ Bot conectado com sucesso!
📍 Nome: YourBot#0000
🎮 Guild ID: 123456789
👤 Admin IDs: [987654321]
🌍 Região padrão: IND
⚙️  Concorrência máxima: 20
📊 Limite diário: 100 likes

✅ 7 comandos sincronizados!
```

---

## 📝 Comandos Disponíveis

### `/status`
Mostra o status atual do bot

```
🤖 Status do Bot
Status: ✅ Online
Serviço: Free Fire Like Bot
Região: IND
Limite Diário: 100 likes
Concorrência: 20 req/seg
```

### `/health`
Verifica a saúde do sistema

```
🏥 Health Check
Bot: ✅ Online
Workers: ✅ Ativos
Database: ✅ Conectado
API: ✅ Respondendo
```

### `/jobs`
Lista todas as tarefas agendadas

```
📋 Fila de Tarefas
Total: 2 tarefa(s)

⏳ job_1
UID: 123456 | Count: 50 | Region: IND | Status: queued

✅ job_2
UID: 789012 | Count: 30 | Region: BR | Status: completed
```

### `/enqueue_like`
Agenda uma tarefa de like (Admin only)

```
/enqueue_like uid:123456789 count:50 region:IND
```

Resposta:
```
✅ Tarefa Agendada!
Job ID: job_1
UID Alvo: 123456789
Likes: 50
Região: IND
Status: completed
```

### `/help`
Mostra todos os comandos com descrições

---

## 🔐 Segurança - IMPORTANTE!

**NUNCA compartilhe seu token do Discord!**

Se você expor o token:
1. Resete imediatamente no Discord Developer Portal
2. Vá em: https://discord.com/developers/applications
3. Clique no seu bot → Bot → Reset Token
4. Gere um novo token
5. Atualize o Secret no Replit

---

## 🆘 Troubleshooting

### ❌ "DISCORD_TOKEN não configurado"
- Verifique se você criou o Secret no Replit
- Clique em "Run" novamente após criar o Secret

### ❌ "GUILD_ID não configurado"
- Ative "Developer Mode" no Discord (Usuário → Configurações → Avançado)
- Clique com botão direito no servidor → Copy Server ID
- Atualize o Secret no Replit

### ❌ "ADMIN_IDS não configurado"
- Clique com botão direito em você no Discord → Copy User ID
- Atualize o Secret no Replit

### ❌ Comandos não aparecem
- Reinicie o bot (clique em "Stop" e depois "Run")
- Aguarde 10-15 segundos para sincronizar com Discord

---

## 📚 Estrutura do Projeto

```
freefire-like-bot-discord/
├── main.py              # Entry point do bot
├── bot.py               # Implementação do Discord bot
├── config.py            # Configurações (lê Secrets)
├── jobs.py              # Sistema de filas
├── requirements.txt     # Dependências Python
├── install.sh           # Script de instalação
├── REPLIT_SETUP.md      # Este arquivo
└── README.md            # Documentação completa
```

---

## 🚀 Próximas Etapas

Depois que o bot estiver rodando:

1. **Testar comandos no Discord**
   - Digite `/status` no servidor
   - Veja se o bot responde

2. **Expandir funcionalidades**
   - Adicionar integração com Free Fire API
   - Implementar criptografia AES-CBC
   - Adicionar autenticação JWT

3. **Configurar auto-run no Replit**
   - Crie um `.replit` file
   - Configure para iniciar automaticamente

---

## 💬 Suporte

Se tiver problemas:
1. Verifique os Secrets estão corretos
2. Reinicie o bot
3. Verifique os logs de erro
4. Crie uma issue no GitHub

---

**Desenvolvido com ❤️ para a comunidade Free Fire**
