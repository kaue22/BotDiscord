import discord
from discord import channel
from discord.ext import commands, tasks
import datetime
import requests


bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()


# Evento async para não retornar mensagens do bot
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


# Quando digitar o prefixo !oi executa a função send_hello
@bot.command(name="ola")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Ola, " + name

    await ctx.send(response)


# Func para o bot calcular
@bot.command(name="calcular")
async def calculate_expression(ctx,
                               *expression):  # *expression é para pegar todos os argumentos passados no parametro expression (tupla)
    expression = ''.join(expression)  # .join para pegar cada elemento da tupla e inserir na string ("")
    response = eval(expression)

    await ctx.send("A Resposta é : " + str(response))


@bot.command(name="cep")
async def find_cep(ctx, cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    data = response.json()
    cep = data.get("cep")
    logradouro = data.get("logradouro")
    bairro = data.get("bairro")

    if cep:
        await ctx.send(f"O valor do par é {cep} e {logradouro} e {bairro}")


# Atualiza data e hora no canal geral do servidor
@tasks.loop(seconds=100)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(ID_CANAL_AQUI)  # id do canal geral

    await channel.send("Data atual :" + now)


bot.run(
    "TOKEN_AQUI")  # TOKEN QUE VOCÊ PEGA NA PAGINA DE DESENVOLVEDOR DO DISCORD
