# mor [encoding] package for the the Skeleton Key project
# created by : Boulbalah lahcen

import nextcord
from nextcord.ext import commands
#from main import guild_id

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', 'a': '.-', 'b': '-...',
                   'c': '-.-.', 'd': '-..', 'e': '.',
                   'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-',
                   'l': '.-..', 'm': '--', 'n': '-.',
                   'o': '---', 'p': '.--.', 'q': '--.-',
                   'r': '.-.', 's': '...', 't': '-',
                   'u': '..-', 'v': '...-', 'w': '.--',
                   'x': '-..-', 'y': '-.--', 'z': '--..'}

# match file name with classname


class mor(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mor - Loaded")

    @nextcord.slash_command(description="Morse Encode / Decode" #guild_ids=[guild_id]
    )
    async def mor(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = "".join(
                f'{MORSE_CODE_DICT[letter]} ' if letter != ' ' else ' '
                for letter in text
            )
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            text += ' '
            output = ''
            citext = ''
            for letter in text:

                # checks for space
                if (letter != ' '):

                    # counter to keep track of space
                    i = 0

                    # storing morse code of a single character
                    citext += letter

                # in case of space
                else:
                    # if i = 1 that indicates a new character
                    i += 1

                    # if i = 2 that indicates a new word
                    if i == 2:

                        # adding space to separate words
                        output += ' '
                    else:
                        # accessing the keys using their values (reverse of encryption)
                        output += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                    .values()).index(citext)]
                        citext = ''
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors

    @mor.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/mor`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/mor`  `e`  `some text to encode`
> Longhand: `/mor`  `decode`  `... --- -- .  - . -..- -`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(mor(client))
