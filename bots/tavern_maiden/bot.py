from lolka import Member, Guild, RawReactionActionEvent

def setup(client, settings, config):
    guild_id = config.get("guild_id")

    autorole = config.get("autorole")
    role_id = autorole.get("role_id")
    if not role_id:
        raise ValueError("В config.json нужен autorole.role_id")

    react_role = config.get("react_role")


    @client.event
    async def on_ready():
        print(f"ready as {client.guilds}")

    @client.event
    async def on_member_join(member):
        role = member.guild.get_role(role_id)
        if role is None:
            print(f"role {role_id} not found in guild {member.guild.id}")
            return
        await member.add_roles(role, reason="autorole on join")

    @client.event
    async def on_raw_reaction_add(payload: RawReactionActionEvent):
        #print(payload)
        message_id = payload.message_id
        if message_id == react_role["message_id"]:
            react_name = payload.emoji.name
            role_id = react_role["map"][react_name]
            if role_id is not None:
                member = payload.member
                if member is None:
                    _guild_id = payload.guild_id if payload.guild_id else guild_id
                    guild = client.get_guild(_guild_id)
                    member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)
                role = member.guild.get_role(role_id)
                await member.add_roles(role, reason="react_role")
        return

    @client.event
    async def on_raw_reaction_remove(payload: RawReactionActionEvent):
        #print(payload)
        message_id = payload.message_id
        if message_id == react_role["message_id"]:
            react_name = payload.emoji.name
            role_id = react_role["map"][react_name]
            if role_id is not None:
                member = payload.member
                if member is None:
                    _guild_id = payload.guild_id if payload.guild_id else guild_id
                    guild = client.get_guild(_guild_id)
                    member = guild.get_member(payload.user_id) or await guild.fetch_member(payload.user_id)
                role = member.guild.get_role(role_id)
                await member.remove_roles(role, reason="react_role")
        return
         
        
