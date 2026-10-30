from lolka import Interaction, app_commands
from ..context import BotContext

def setup(ctx: BotContext):
    @ctx.tree.command(name="quote")
    @app_commands.rename(link='ссылка')
    async def quote(
        interaction: Interaction,
        link: str
    ):
        id = link[link.rfind('/')+1:]
        message = await interaction.channel.fetch_message(id)
        
        embed = Embed(description=message.content or "*без текста*",
                      colour=Colour.gold(), timestamp=message.created_at)
        embed.set_author(name=message.author.display_name,
                         icon_url=message.author.display_avatar.url)
        embed.set_footer(text=f"#{interaction.channel.name}")
        await interaction.response.send_message(content='Цитата дня: '
                                                , embed=embed
                                                )