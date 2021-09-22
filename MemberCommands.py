import discord
import randfacts
from discord.ext import commands

Client = commands.Bot(command_prefix = "+")

class MemberCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def RandomFact(self, ctx):
        Fact = randfacts.get_fact()
        await ctx.send(f"Random fact: {Fact}")

def setup(bot):
    bot.add_cog(MemberCommands(bot))