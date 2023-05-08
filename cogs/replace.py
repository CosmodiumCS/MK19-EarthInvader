# character replacer
# created by Soulsender

import nextcord
from nextcord.ext import commands

# match file name with classname
class replacer(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Replacer - Loaded")

    @nextcord.slash_command(description="Text Replacer")
    async def replace(self, interaction: nextcord.Interaction, template_char, replace_char, text):
        message = ""
        output = text.replace(template_char, replace_char)

        message = f"**Replaced `{template_char}` with `{replace_char}` in `{text}`:**\n{output}"

        await interaction.response.send_message(message)        

    # Handle Errors
    @replace.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
        **Syntax**
        > Usage - `/replace`  `<what you want to replace>` `<thing to replace with>`  `<text>`

        **Examples:**
        > Input: `/replace`  `o` `5` `Hello World`
        > Output: `Hell5 W5rld`

        > Input: `/replace` `Hello` `Goodbye` `Hello World`
        > Output: `Goodbye World`
        """
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(replacer(client))
