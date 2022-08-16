from string import punctuation

import disnake
from disnake.ext import commands


class BB(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Extension loaded: {self.qualified_name}")

    @commands.message_command(name="swap_first_letter")
    async def b_first_letter(
        self, interaction: disnake.MessageCommandInteraction, message: disnake.Message
    ):
        """Replace the first letter of each word in target message with "B" emoji"""

        content = message.content
        new_content = ""

        for index, char in enumerate(message.content):
            # we onlY want to change the first letter of a word if the word is not a single letter
            # in length (example: "a", "I")
            if index == 0 or content[index - 1] == " " and content[index + 1] != " ":
                new_content += "🅱️"
                continue

            new_content += char

        await interaction.response.send_message(new_content)

    @commands.message_command(name="swap_all_bs")
    async def b_to_emoji(
        self, interaction: disnake.MessageCommandInteraction, message: disnake.Message
    ):
        """Replace the first letter of each word in target message with "B" emoji"""

        content = message.content
        new_content = ""

        for char in content:
            if char.lower() == "b":
                new_content += "🅱️"
                continue

            new_content += char

        await interaction.response.send_message(new_content)
