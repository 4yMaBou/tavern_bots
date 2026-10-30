from lolka import Member
from ..context import BotContext


def setup(ctx: BotContext):
    client = ctx.client

    @client.event
    async def on_member_join(payload: Member):
        member = payload
        autorole = ctx.config.params.get("autorole")
        role = member.guild.get_role(autorole["role_id"])
        if role is None:
            print(f"role {role_id} not found in guild {member.guild.id}")
            return
        await member.add_roles(role, reason="autorole on join")
