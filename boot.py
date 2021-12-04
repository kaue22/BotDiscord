import datetime
import discord
from discord.ext import commands,tasks

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()

#Evento async para não retornar mensagens do bot
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor,{message.author.name},não ofenda os demais usuários!"
            )

            await message.delete()

    await bot.process_commands(message)

#Quando digitar o prefixo !oi executa a função send_hello
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Ola, " + name

    await ctx.send(response)
#Atualiza data e hora no canal geral do servidor
@tasks.loop(seconds=100)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(915984953395785804) #id do canal geral

    await channel.send("Data atual :" + now)


bot.run("TOKEN_AQUI") #TOKEN QUE VOCÊ PEGA NA PAGINA DE DESENVOLVEDOR DO DISCORD