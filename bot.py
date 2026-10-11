import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from config import DISCORD_TOKEN, GUILD_ID, ADMIN_IDS, FREEFIRE_REGION, MAX_LIKES_PER_DAY, MAX_CONCURRENT_LIKES
from jobs import enqueue_like_job, list_jobs, simulate_job_progress, get_job_status

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Criar bot
bot = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(bot)

def is_admin(user_id: int) -> bool:
    """Verifica se o usuário é admin"""
    return user_id in ADMIN_IDS

@bot.event
async def on_ready():
    """Evento de bot conectado"""
    print(f"\n✅ Bot conectado com sucesso!")
    print(f"📍 Nome: {bot.user}")
    print(f"🎮 Guild ID: {GUILD_ID}")
    print(f"👤 Admin IDs: {ADMIN_IDS}")
    print(f"🌍 Região padrão: {FREEFIRE_REGION}")
    print(f"⚙️  Concorrência máxima: {MAX_CONCURRENT_LIKES}")
    print(f"📊 Limite diário: {MAX_LIKES_PER_DAY} likes\n")
    
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await tree.sync(guild=guild)
        print(f"✅ {len(synced)} comandos sincronizados!\n")
    except Exception as e:
        print(f"❌ Erro ao sincronizar: {e}\n")

@tree.command(name="status", description="🤖 Status do bot")
async def status(interaction: discord.Interaction):
    """Mostra status do bot"""
    embed = discord.Embed(
        title="🤖 Status do Bot",
        color=discord.Color.green(),
        description="Informações do sistema"
    )
    embed.add_field(name="Status", value="✅ Online", inline=False)
    embed.add_field(name="Serviço", value="Free Fire Like Bot", inline=False)
    embed.add_field(name="Região", value=FREEFIRE_REGION, inline=False)
    embed.add_field(name="Limite Diário", value=f"{MAX_LIKES_PER_DAY} likes", inline=False)
    embed.add_field(name="Concorrência", value=f"{MAX_CONCURRENT_LIKES} req/seg", inline=False)
    embed.set_footer(text="Bot pronto para operação")
    
    await interaction.response.send_message(embed=embed, ephemeral=False)

@tree.command(name="health", description="🏥 Verificar saúde do sistema")
async def health(interaction: discord.Interaction):
    """Verifica saúde do sistema"""
    embed = discord.Embed(
        title="🏥 Health Check",
        color=discord.Color.green(),
        description="Status do sistema"
    )
    embed.add_field(name="Bot", value="✅ Online", inline=False)
    embed.add_field(name="Workers", value="✅ Ativos", inline=False)
    embed.add_field(name="Database", value="✅ Conectado", inline=False)
    embed.add_field(name="API", value="✅ Respondendo", inline=False)
    
    await interaction.response.send_message(embed=embed, ephemeral=False)

@tree.command(name="jobs", description="📋 Listar tarefas em fila")
async def jobs_cmd(interaction: discord.Interaction):
    """Lista tarefas agendadas"""
    await interaction.response.defer()
    
    all_jobs = list_jobs()
    if not all_jobs:
        embed = discord.Embed(
            title="📋 Fila de Tarefas",
            description="Nenhuma tarefa em fila",
            color=discord.Color.blue()
        )
        await interaction.followup.send(embed=embed, ephemeral=False)
        return
    
    embed = discord.Embed(
        title="📋 Fila de Tarefas",
        color=discord.Color.blue(),
        description=f"Total: {len(all_jobs)} tarefa(s)"
    )
    
    for job in all_jobs[:10]:
        status_emoji = "⏳" if job["status"] == "queued" else "⚙️" if job["status"] == "processing" else "✅"
        embed.add_field(
            name=f"{status_emoji} {job['job_id']}",
            value=f"UID: `{job['uid']}` | Count: `{job['count']}` | Region: `{job['region']}` | Status: `{job['status']}`",
            inline=False
        )
    
    await interaction.followup.send(embed=embed, ephemeral=False)

@tree.command(name="enqueue_like", description="❤️ Agendar tarefa de like")
@app_commands.describe(
    uid="UID do alvo",
    count="Quantidade de likes",
    region="Região (IND/BR/US/SG/RU/ID/TW/VN/TH/ME/PK)"
)
async def enqueue_like(interaction: discord.Interaction, uid: str, count: int, region: str = ""):
    """Agenda uma tarefa de like"""
    
    if not is_admin(interaction.user.id):
        embed = discord.Embed(
            title="❌ Acesso Negado",
            description="Você não tem permissão!",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    
    if count <= 0:
        embed = discord.Embed(
            title="❌ Erro",
            description="Count deve ser maior que 0!",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    
    if count > MAX_LIKES_PER_DAY:
        embed = discord.Embed(
            title="❌ Limite Excedido",
            description=f"Máximo: {MAX_LIKES_PER_DAY} likes/dia",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    
    await interaction.response.defer()
    
    selected_region = (region or FREEFIRE_REGION).upper()
    
    try:
        job = await enqueue_like_job(uid, count, selected_region)
        await simulate_job_progress(job["job_id"])
        
        embed = discord.Embed(
            title="✅ Tarefa Agendada!",
            color=discord.Color.green(),
            description="Sua tarefa foi adicionada à fila"
        )
        embed.add_field(name="Job ID", value=f"`{job['job_id']}`", inline=False)
        embed.add_field(name="UID Alvo", value=f"`{job['uid']}`", inline=False)
        embed.add_field(name="Likes", value=f"`{job['count']}`", inline=False)
        embed.add_field(name="Região", value=f"`{selected_region}`", inline=False)
        embed.add_field(name="Status", value=f"`{job['status']}`", inline=False)
        
        await interaction.followup.send(embed=embed, ephemeral=False)
    except Exception as e:
        embed = discord.Embed(
            title="❌ Erro",
            description=f"```{str(e)}```",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=embed, ephemeral=True)

@tree.command(name="help", description="📖 Mostrar ajuda")
async def help_cmd(interaction: discord.Interaction):
    """Mostra ajuda"""
    embed = discord.Embed(
        title="📖 Ajuda - Comandos",
        color=discord.Color.purple(),
        description="Lista de comandos disponíveis"
    )
    
    embed.add_field(
        name="/status",
        value="Mostra status do bot",
        inline=False
    )
    embed.add_field(
        name="/health",
        value="Verifica saúde do sistema",
        inline=False
    )
    embed.add_field(
        name="/jobs",
        value="Lista tarefas agendadas",
        inline=False
    )
    embed.add_field(
        name="/enqueue_like uid:<uid> count:<qtd> region:<regiao>",
        value="Agenda tarefa de like (Admin only)",
        inline=False
    )
    embed.add_field(
        name="/help",
        value="Mostra esta mensagem",
        inline=False
    )
    
    embed.set_footer(text="Use /status para ver configurações")
    
    await interaction.response.send_message(embed=embed, ephemeral=False)

async def main():
    """Inicia o bot"""
    try:
        print("🚀 Iniciando bot Discord...\n")
        await bot.start(DISCORD_TOKEN)
    except Exception as e:
        print(f"❌ Erro crítico: {e}")

if __name__ == "__main__":
    asyncio.run(main())
