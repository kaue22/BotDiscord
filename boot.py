import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

#Quando digitar o prefixo !oi executa a função send_hello
@bot.commands(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Ola, " + name

    await ctx.send(response)


bot.run("TOKEN_AQUI")