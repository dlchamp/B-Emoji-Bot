from datetime import datetime
from sys import version

from disnake import Intents
from disnake import __version__ as disnake_version
from disnake.ext.commands import InteractionBot

from bot import __version__ as bot_version
from bot.bb import BB

intents = Intents.default()
bot = InteractionBot(intents=intents)


@bot.listen()
async def on_ready():
    print(
        f"Bot Started at {datetime.now().strftime('%m-%d-%Y %H:%M')}\n"
        f"Disnake version: {disnake_version}\n"
        f"System: {version}\n"
        f"Bot Version: {bot_version}\n"
        f"Bot Name: {bot.user.name}\n"
        f"Bot ID: {bot.user.id}\n"
        f"Latency Status: {bot.latency}s\n"
        "----------------------------------------------------------------"
    )


bot.add_cog(BB(bot))
