from lolka import RawReactionActionEvent
from ..context import BotContext

def setup(ctx: BotContext):
    client = ctx.client
    react_role = ctx.config.params["react_role"]
    
    @client.event
    async def on_raw_reaction_add(payload: RawReactionActionEvent):
        message_id = payload.message_id
        if message_id == react_role["message_id"]:
            react_name = payload.emoji.name
            role_id = react_role["map"].get(react_name)
            if role_id is not None:
                member = payload.member
                if member is None:
                    guild = await ctx.get_guild()
                    member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)
                role = member.guild.get_role(role_id)
                await member.add_roles(role, reason="react_role")
        return

    @client.event
    async def on_raw_reaction_remove(payload: RawReactionActionEvent):
        message_id = payload.message_id
        if message_id == react_role["message_id"]:
            react_name = payload.emoji.name
            role_id = react_role["map"].get(react_name)
            if role_id is not None:
                member = payload.member
                if member is None:
                    guild = await ctx.get_guild()
                    member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)
                role = member.guild.get_role(role_id)
                await member.remove_roles(role, reason="react_role")
        return