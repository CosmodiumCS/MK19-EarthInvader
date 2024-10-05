# leet [encoding] package for the the Skeleton Key project
# created by : Cosmo

import nextcord
from nextcord.ext import commands
#from main import guild_id

# leet chr
leet_dictionary_enc = {
    "a": "4",
    "b": "8",
    "e": "3",
    "g": "6",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}

# invert leet chr
leet_dictionary_dec = {v: k for (k, v) in leet_dictionary_enc.items()}

# match file name with classname
class leet(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Leet - Loaded")

    @nextcord.slash_command(description="L33T Encode / Decode" #guild_ids=[guild_id]
    )
    async def leet(self, interaction: nextcord.Interaction, action, text):
        message = ""

        # "encode" or "e" entered
        if action in ["encode", 'e']:
            text = text.lower()
            output = ''.join(
                (
                    leet_dictionary_enc[character]
                    if character in leet_dictionary_enc
                    else character
                )
                for character in text
            )
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            text = text.lower()
            output = ''.join(
                (
                    leet_dictionary_dec[character]
                    if character in leet_dictionary_dec
                    else character
                )
                for character in text
            )
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors

    @leet.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/leet`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/leet`  `e`  `some text to encode`
> Longhand: `/leet`  `decode`  `50m3 73x7`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(leet(client))
