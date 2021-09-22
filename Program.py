from discord.ext import commands
from os import environ
from dotenv import load_dotenv
load_dotenv()

Client = commands.Bot(command_prefix = "+")

@Client.event
async def on_ready():
    print("Bot is ready.")

extenstions = ["Cogs.MemberCommands", "Cogs.HighLevelCommands"]

if __name__ == "__main__":
    for ext in extenstions:
        Client.load_extension(ext)

Client.run(environ.get("BOT_TOKEN"))