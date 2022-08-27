#!/usr/bin/python
# created by : Boulbalah lahcen

from discord.ext import commands

 

class mor(commands.Cog):
    def __init__(self, client):
        self.client = client
    # Dictionary representing the morse code
    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def mor(self, ctx, action, *, text):
        cipher = ''
        # Dictionary representing the morse code
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        # encode morse
        if action == "encode" or action == "e":
            # encode to morse
            
            for letter in text:
                if letter != ' ':
                    output += MORSE_CODE_DICT[letter] + ' '
                else:
                    output += ' '
            # output = cipher                    
            await ctx.send(output)
            return [output, True]

        # decode mor
        if action == "decode" or action == "d":
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
                    if i == 2 :
        
                        # adding space to separate words
                        output += ' '
                    else:
                        # accessing the keys using their values (reverse of encryption)
                        output += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                        .values()).index(citext)]
                        citext = ''
            
            await ctx.send(output)
            return [output,True]

async def setup(client):
    await client.add_cog(mor(client))

