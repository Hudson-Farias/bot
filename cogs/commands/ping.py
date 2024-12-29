from discord.ext.commands.bot import Bot
from discord import Interaction, app_commands
from discord.ext.commands import Cog, command
from discord.ext.commands.context import Context


class Ping(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    async def _ping(self):
        return f'{self.bot.latency*100:.2f}ms'


    @app_commands.command(name = 'ping')
    async def slash(self, inter: Interaction):
        message = await self._ping()
        await inter.response.send_message(message, ephemeral = False)


    @command(name = 'ping')
    async def text(self, ctx: Context):
        message = await self._ping()
        await ctx.message.reply(message)




async def setup(bot: Bot):
    await bot.add_cog(Ping(bot))
