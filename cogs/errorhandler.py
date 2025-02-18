import discord, datetime
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            CommandNotFoundEmbed = discord.Embed(
                title = "Warning",
                description = "The command that you tried to send wasn't was found.",
                timestamp = datetime.datetime.utcnow(),
                colour = 0xff0011
            )
            CommandNotFoundEmbed.set_footer(text = f"{self.bot.user.name}", icon_url = f"{self.bot.user.avatar_url}")
            await ctx.send(embed = CommandNotFoundEmbed)
        
        elif isinstance(error, commands.MissingPermissions):
            MissingPermissionsEmbed = discord.Embed(
                title = "Warning",
                description = "You are missing permission to run this command!",
                timestamp = datetime.datetime.utcnow(),
                colour = 0xff0011
            )
            MissingPermissionsEmbed.set_footer(text = f"{self.bot.user.name}", icon_url = f"{self.bot.user.avatar_url}")
            await ctx.send(embed = MissingPermissionsEmbed)
        
        elif isinstance(error, commands.UserInputError):
            UserInputErrorEmbed = discord.Embed(
                title = "Warning",
                description = "Something wrong happen in your input, please check your input and try again!",
                timestamp = datetime.datetime.utcnow(),
                colour = 0xff0011
            )
            UserInputErrorEmbed.set_footer(text = f"{self.bot.user.name}", icon_url = f"{self.bot.user.avatar_url}")
            await ctx.send(embed = UserInputErrorEmbed)
        
        elif isinstance(error, commands.CommandOnCooldown):
            CommandCooldownEmbed = discord.Embed(
                title = "Warning",
                description = f"**{error}**",
                timestamp = datetime.datetime.utcnow(),
                colour = 0xff0011
            )
            CommandCooldownEmbed.set_footer(text = f"{self.bot.user.name}", icon_url = f"{self.bot.user.avatar_url}")
            await ctx.send(embed = CommandCooldownEmbed)

        elif isinstance(error, commands.CommandError):
            CommandErrorEmbed = discord.Embed(
                title = "Warning",
                description = "Error has been occurred, please send a bug report in the issues page on GitHub",
                timestamp = datetime.datetime.utcnow(),
                colour = 0xff0011
            )
            CommandErrorEmbed.add_field(name = "Error: ", value = error)
            CommandErrorEmbed.add_field(name = "Link to GitHub: ", value = "https://github.com/OctoBanon-Main/Unnamed-bot/issues")
            CommandErrorEmbed.set_footer(text = f"{self.bot.user.name}", icon_url = f"{self.bot.user.avatar_url}")
            await ctx.send(embed = CommandErrorEmbed)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
    print("Error handler successfully registered")