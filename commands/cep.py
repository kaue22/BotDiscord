import discord
import requests
from discord.ext import commands


class Cep(commands.Cog):
    """ CEP WITH USER """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cep", help="CEP--Apenas para testar a API...")
    async def find_cep(self, ctx, cep):
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        data = response.json()
        cep = data.get("cep")
        logradouro = data.get("logradouro")
        bairro = data.get("bairro")

        if cep:
            await ctx.send(f"O cep é {cep} e {logradouro} e {bairro}")


def setup(bot):
    bot.add_cog(Cep(bot))
