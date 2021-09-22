import discord
from discord.ext import commands

Client = commands.Bot(command_prefix = "+")

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role("Owner", "Moderators")
    async def Clear(self, ctx, amount = 10):
        await ctx.channel.purge(limit = amount)

    @commands.command()
    @commands.has_any_role("Owner", "Moderators")
    async def Kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(f"{member} was kicked for {reason}")
    
    @commands.command()
    @commands.has_any_role("Owner", "Moderators")
    async def Ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f"{member} was banned for {reason}")
    
    @commands.command()
    @commands.has_any_role("Owner", "Moderators")
    async def Unban(self, ctx, *, member):
        Banned_users = await ctx.guild.bans()
        Member_name, Member_discriminator = member.split("#")

        for ban_entry in Banned_users:
            Selected_user = ban_entry.user

            if (Selected_user.name, Selected_user.discriminator) == (Member_name, Member_discriminator):
                await ctx.guild.unban(Selected_user)
                await ctx.send(f"{Selected_user} was unbanned")
                return


def setup(bot):
    bot.add_cog(AdminCommands(bot))