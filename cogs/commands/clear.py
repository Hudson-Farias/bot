from discord.ext.commands.bot import Bot
from discord import Interaction, app_commands
from discord.ext.commands import Cog, command, has_guild_permissions
from discord.ext.commands.context import Context
from discord.channel import TextChannel


class Clear(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.delete_after = 10


    async def _clear(self, channel: TextChannel, amount: int):
        await channel.purge(limit = amount)
        return 'Mensagens excluídas'


    @app_commands.command(name = 'clear')
    @has_guild_permissions(manage_messages = True)
    async def slash(self, inter: Interaction):
    # async def slash(self, inter: Interaction, amount: Option(int, default = 30), channel: Option(GuildChannel, required = False)):
        amount = 30

        message = await self._clear(inter.channel, amount)
        await inter.response.send_message(message, ephemeral = False, delete_after = 10)

        # if channel:
        #     await channel.purge(limit = amount)

        # else:
        #     await inter.channel.purge(limit = amount)

        # else:
        #     msg = message('Txt/MissingPermissions.txt')
        #     await inter.response.send_message(msg, ephemeral=True)


    @command(name = 'clear')
    @has_guild_permissions(manage_messages = True)
    async def text(self, ctx: Context, amount: int = 30, channel: TextChannel = None):
        channel = channel if channel else ctx.channel

        message = await self._clear(channel, amount)
        await ctx.channel.send(message, delete_after = self.delete_after)




async def setup(bot: Bot):
    await bot.add_cog(Clear(bot))
