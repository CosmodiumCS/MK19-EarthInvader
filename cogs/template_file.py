# template

import nextcord
from nextcord.ext import commands
from main import guild_id

# match file name with classname
class template_file(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"template_file - Loaded")

    @nextcord.slash_command(description="Template Encode / Decode", guild_ids=[guild_id])
    async def template_file(self, interaction: nextcord.Interaction, action, text):

        # If not enc/dec this stays blank and throws error
        message = ""
        # "encode" or "e" entered
        if action == "encode" or action == 'e':
            output = ""


            # Encoding in here to output


            message = f"**Encoded:**\n{output}"

        # "decode" or "d" entered
        if action == "decode" or action == 'd':
            output = ""


            # Decoding in here to output


            message = f"**Decoded:**\n{output}"

        await interaction.response.send_message(message)

    # Handle Errors
    @template_file.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):

        # Help Menu
        message = """
**Syntax**
> Usage - `/template_file`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/template_file`  `e`  `some text to encode`
> Longhand: `/template_file`  `decode`  `c29tZSB0ZXh0`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(template_file(client))
