from lolka import Interaction, app_commands, Member
from ..context import BotContext
from typing import Literal

def setup(ctx: BotContext):
    
    @ctx.tree.command(name="ping", description="Проверка связи")
    async def ping(interaction: Interaction):
        await interaction.response.send_message("pong", ephemeral=True)


    @ctx.tree.command(name="roll", description="Бросить кубик")
    async def roll(
            interaction: Interaction, 
            roll_type: Literal ['d6', 'd21', 'coin']
    ):
        bot_response = ''
        match roll_type:
            case 'd6':
                bot_response = str(randint(1, 6))
            case 'd21':
                bot_response = str(randint(1, 21))
            case 'coin':
                bot_response = str(randint(1, 2)).replace("1", "орёл").replace("2", "решка")
        await interaction.response.send_message(f"{roll_type}: {bot_response}")
    
    @ctx.tree.command(name='random')
    @app_commands.describe(raw_input='Значения через "-"')
    async def random(
            interaction: Interaction,
            user: Member,
            raw_input: str = 'Камень-Ножницы-Бумага'
    ):
        options = raw_input.split('-')
        bot_response = options[randint(0, options.__len__() - 1)]
        await interaction.response.send_message(f"{user.mention}: {bot_response}")


    @ctx.tree.command(name='do')
    @app_commands.rename(text='описание')
    async def action(
        interaction: Interaction,
        text: str
    ):
        await interaction.response.send_message(f"{interaction.user.mention} {text}")