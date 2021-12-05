import discord
from discord import channel, client
from discord.ext import commands, tasks
import datetime
import requests
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


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


@bot.event
async def on_member_join(member):
    hello = bot.get_channel(915984953395785800)

    message = await hello.send(f"Bem vindo {member.mention}  ao canal do estudo aws HLIS!!")

    await asyncio.sleep(10)
    await message.delete()


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
        await ctx.send(f"O cep é {cep} e {logradouro} e {bairro}")


@bot.command(name="foipior")
async def foi_pior(ctx):
    await ctx.send(file=discord.File('foipior.jpeg'))

@bot.command(name="jamais")
async def foi_pior(ctx):
    await ctx.send(file=discord.File('jamais.jpeg'))


# Atualiza data e hora no canal geral do servidor
@tasks.loop(seconds=86400)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(915984953395785804)  # id do canal geral

    await channel.send("****************** Data atual ****************** :" + now)


bot.run("TOKEN_AQUI")  # TOKEN QUE VOCÊ PEGA NA PAGINA DE DESENVOLVEDOR DO DISCORD
