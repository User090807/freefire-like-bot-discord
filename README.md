# Free Fire Like Discord Bot

Integração planejada entre um bot do Discord e a API de likes do Free Fire.

## Estado atual

Este repositório ainda não está executável: não contém `main.py` nem `requirements.txt`, embora o `setup.sh` dependa deles. Os arquivos atuais são apenas uma base de configuração; não tente iniciar o bot até que esses arquivos sejam adicionados.

## Configuração de ambiente

Quando o código do bot estiver disponível:

1. Copie `.env.example` para `.env`.
2. Preencha `DISCORD_TOKEN`, `GUILD_ID`, `ADMIN_IDS` e `JWT_SECRET` com os valores do seu ambiente.
3. Mantenha os valores reais somente em `.env` local ou nos Secrets do Replit — nunca no GitHub nem no chat.

O `.gitignore` exclui `.env` e arquivos de dados locais. Se um token já foi publicado, revogue-o no Discord Developer Portal e gere outro: apagar o valor da versão atual não o remove do histórico do Git.

## Setup

O script `setup.sh` só poderá instalar dependências e iniciar o bot depois que `requirements.txt` e `main.py` forem adicionados.
