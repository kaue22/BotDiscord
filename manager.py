import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import MissingRequiredArgument, CommandNotFound


class Manager(commands.Cog):
    """ MANAGER """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronto! Estou conectado como {self.bot.user}")

    # Evento async para não retornar mensagens do bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor,{message.author.name},não ofenda os demais usuários!"
            )

        await message.delete()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        hello = self.bot.get_channel(915984953395785800)

        message = await hello.send(f"Bem vindo {member.mention}  ao canal do estudo aws HLIS!!")

        await asyncio.sleep(10)
        await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os Parametros")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O Comando não existe")
        else:
            raise error


def setup(bot):
    bot.add_cog(Manager(bot))
