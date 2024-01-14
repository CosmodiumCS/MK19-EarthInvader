import nextcord
from nextcord.ext import commands
#from main import guild_id

# match file name with classname
class metric(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Metric - Loaded")

    @nextcord.slash_command(description="Convert metric to imperial", guild_ids=[414625175217242113]
    )
    async def metric(self, interaction: nextcord.Interaction, unit, value):
        value = float(value)
        if unit.lower() == "kilometers" or unit.lower() == "km":
            converted_value = value * 0.621371
            response = f"`{value}` kilometers \nis \n`{converted_value:.2f}` miles"
        elif unit.lower() == "liters" or unit.lower() == "l":
            converted_value = value * 0.264172
            response = f"`{value}` liters \nis \n`{converted_value:.2f}` gallons"
        elif unit.lower() == "kilograms" or unit.lower() == "kg":
            converted_value = value * 2.20462
            response = f"`{value}` kilograms \nis \n`{converted_value:.2f}` pounds"
        elif unit.lower() == "miles" or unit.lower() == "m":
            converted_value = value / 0.621371
            response = f"`{value}` miles \nis \n`{converted_value:.2f}` kilometers"
        elif unit.lower() == "gallons" or unit.lower() == "gal":
            converted_value = value / 0.264172
            response = f"`{value}` gallons \nis \n`{converted_value:.2f}` liters"
        elif unit.lower() == "pounds" or unit.lower() == "lb":
            converted_value = value / 2.20462
            response = f"`{value}` pounds \nis \n`{converted_value:.2f}` kilograms"
        await interaction.response.send_message(response)

    # Handle Errors
    @metric.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/metric`  `<value>`

**Examples:**
> Shorthand: `/temp`  `km` `160`
> Longhand: `/temp`  `kilograms`  `40`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(metric(client))
