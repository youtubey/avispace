import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    activity = discord.Game(name="Waiting...\nby uwuness", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Бот запустился!")

@bot.command(name = "test", pass_context = True)
@commands.has_permissions( administrator = True)
async def test(ctx):
    await ctx.channel.purge(limit = 1);
    embed = discord.Embed(
        color = discord.Color(value = int('2F3136', 16)),
        title = "**ТЕСТ**",
        description = "**AviSpace**"
        )
    embed.set_footer(text=f"© AviSpace — Все права защищены!")

    await ctx.send(embed = embed)

bot.run(settings['token'])