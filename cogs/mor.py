#!/usr/bin/python
# created by : Boulbalah lahcen

from discord.ext import commands

 

class mor(commands.Cog):
    def __init__(self, client):
        self.client = client
    # Dictionary representing the morse code
    encode_table = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        " ": "SPACE",
    }
    #reverse encode tabale
    decode_table = {v: k for k, v in encode_table.items()}
    def encode(self,s):
        enc = " ".join(self.encode_table[x] for x in s)
        return enc.replace(" SPACE ", "   ")

    def decode(self,encoded):
        symbols = encoded.replace("   ", " SPACE ").split(" ")
        return "".join(self.decode_table[x] for x in symbols)

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def mor(self, ctx, action, *, text):

        # encode morse
        if action == "encode" or action == "e":
            # encode to morse
            output = self.encode(text) 
            await ctx.send(output)
            return [output, True]

        # decode mor
        if action == "decode" or action == "d":
            output = self.decode(text)
            await ctx.send(output)
            return [output,True]

async def setup(client):
    await client.add_cog(mor(client))

