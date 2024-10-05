import nextcord
from nextcord.ext import commands
#from main import guild_id

# match file name with classname
class metric(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Metric - Loaded")

    @nextcord.slash_command(description="Convert metric to imperial"
    )
    async def metric(self, interaction: nextcord.Interaction, unit, value):
        value = float(value)
        if unit.lower() in ["kilometers", "km"]:
            converted_value = value * 0.621371
            response = f"`{value}` kilometers \nis \n`{converted_value:.2f}` miles"
        elif unit.lower() in ["liters", "l"]:
            converted_value = value * 0.264172
            response = f"`{value}` liters \nis \n`{converted_value:.2f}` gallons"
        elif unit.lower() in ["kilograms", "kg"]:
            converted_value = value * 2.20462
            response = f"`{value}` kilograms \nis \n`{converted_value:.2f}` pounds"
        elif unit.lower() in ["miles", "m"]:
            converted_value = value / 0.621371
            response = f"`{value}` miles \nis \n`{converted_value:.2f}` kilometers"
        elif unit.lower() in ["gallons", "gal"]:
            converted_value = value / 0.264172
            response = f"`{value}` gallons \nis \n`{converted_value:.2f}` liters"
        elif unit.lower() in ["pounds", "lb"]:
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
