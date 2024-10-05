# r13 [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands

# match file name with classname
class r13(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("R13 - Loaded")

    @nextcord.slash_command(description="Rot13 Encode / Decode")
    async def r13(self, interaction: nextcord.Interaction, action,text):
        message = ""
        key = 13

        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # encryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((((((ord(character) + key) - 65)) % 26) + 65))
                    else:
                        output += chr((((((ord(character) + key) - 97)) % 26) + 97))
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # decryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((((((ord(character) - key) - 65)) % 26) + 65))
                    else:
                        output += chr((((((ord(character) - key) - 97)) % 26) + 97))
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors

    @r13.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/r13`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/r13`  `e`  `some text to encode`
> Longhand: `/r13`  `decode`  `fbzr grkg`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(r13(client))
