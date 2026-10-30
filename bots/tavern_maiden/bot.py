from lolka import app_commands
from .context import BotContext
from .events import reactions, lifecycle, members 
from .commands import admin, config, fun, quote

MODULES = [
    lifecycle, 
    members, 
    reactions, 
    admin,
    config,
    fun, 
    quote
    ]

def setup(client, settings, config):
    ctx = BotContext(
        client=client,
        settings=settings,
        config=config,
        tree=app_commands.CommandTree(client)
    )
    for module in MODULES:
        module.setup(ctx)

# from lolka import Member, Guild, Message, Embed, Colour, Interaction, RawReactionActionEvent, app_commands
# from random import randint
# from typing import Literal

# def setup(client, settings, config):
#     tree = app_commands.CommandTree(client)
#     GUILD_ID = config.params.get("guild_id")
#     GUILD = client.get_guild(GUILD_ID)


#     @client.event
#     async def on_ready():
#         print(f"ready as {client.application}")


#     @client.event
#     async def on_member_join(payload: Member):
#         member = payload
#         autorole = config.params.get("autorole")
#         role = member.guild.get_role(autorole["role_id"])
#         if role is None:
#             print(f"role {role_id} not found in guild {member.guild.id}")
#             return
#         await member.add_roles(role, reason="autorole on join")


#     @client.event
#     async def on_raw_reaction_add(payload: RawReactionActionEvent):
#         message_id = payload.message_id
#         react_role = config.params.get("react_role")
#         if message_id == react_role["message_id"]:
#             react_name = payload.emoji.name
#             role_id = react_role["map"][react_name]
#             if role_id is not None:
#                 member = payload.member
#                 if member is None:
#                     member = GUILD.get_member(payload.user_id) or await GUILD.fetch_member(payload.user_id)
#                 role = member.guild.get_role(role_id)
#                 await member.add_roles(role, reason="react_role")
#         return


#     @client.event
#     async def on_raw_reaction_remove(payload: RawReactionActionEvent):
#         message_id = payload.message_id
#         if message_id == react_role["message_id"]:
#             react_name = payload.emoji.name
#             role_id = react_role["map"][react_name]
#             if role_id is not None:
#                 member = payload.member
#                 if member is None:
#                     member = GUILD.get_member(payload.user_id) or await GUILD.fetch_member(payload.user_id)
#                 role = member.guild.get_role(role_id)
#                 await member.remove_roles(role, reason="react_role")
#         return
         

#     @tree.command(name="ping", description="Проверка связи", guild=GUILD)
#     async def ping(interaction: Interaction):
#         await interaction.response.send_message("pong", ephemeral=True)


#     @tree.command(name="roll", description="Бросить кубик", guild=GUILD)
#     async def roll(
#             interaction: Interaction, 
#             roll_type: Literal ['d6', 'd21', 'coin']
#     ):
#         bot_response = ''
#         match roll_type:
#             case 'd6':
#                 bot_response = str(randint(1, 6))
#             case 'd21':
#                 bot_response = str(randint(1, 21))
#             case 'coin':
#                 bot_response = str(randint(1, 2)).replace("1", "орёл").replace("2", "решка")
#         await interaction.response.send_message(f"{roll_type}: {bot_response}")


#     @tree.command(name='random', guild=GUILD)
#     @app_commands.describe(raw_input='Значения через "-"')
#     async def random(
#             interaction: Interaction,
#             user: Member,
#             raw_input: str = 'Камень-Ножницы-Бумага'
#     ):
#         options = raw_input.split('-')
#         bot_response = options[randint(0, options.__len__() - 1)]
#         await interaction.response.send_message(f"{user.mention}: {bot_response}")


#     @tree.command(name='do', guild=GUILD)
#     @app_commands.describe(text='')
#     @app_commands.rename(text='описание')
#     async def action(
#         interaction: Interaction,
#         text: str
#     ):
#         await interaction.response.send_message(f"{interaction.user.mention} {text}")

#     #TO DO пока реализуем через command и сслыку на сообщение ибо context_menu не работает
#     # @tree.context_menu()
#     # async def react(
#     #     interaction: Interaction,
#     #     message: Message
#     # ):
#     #     await interaction.response.send_message(f"Very cool message!")

#     @tree.command(name="quote")
#     @app_commands.rename(link='ссылка')
#     async def quote(
#         interaction: Interaction,
#         link: str
#     ):
#         id = link[link.rfind('/')+1:]
#         message = await interaction.channel.fetch_message(id)
        
#         embed = Embed(description=message.content or "*без текста*",
#                       colour=Colour.gold(), timestamp=message.created_at)
#         embed.set_author(name=message.author.display_name,
#                          icon_url=message.author.display_avatar.url)
#         embed.set_footer(text=f"#{interaction.channel.name}")
#         await interaction.response.send_message(content='Цитата дня: '
#                                                 , embed=embed
#                                                 )

#     #Для отладки
#     # @client.event
#     # async def on_interaction(interaction: Interaction):
#     #     print(interaction.data)
#     #     return

#     @client.event
#     async def setup_hook():
#         await tree.sync(guild=GUILD)
        