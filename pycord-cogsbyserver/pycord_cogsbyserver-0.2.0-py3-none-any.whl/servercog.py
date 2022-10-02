from discord import Guild, slash_command
from discord.ext.commands import Cog, Bot
from typing import Type
from .utils import find_guild
from functools import wraps

DMS = None

# Pretty much every available event. Not the raw
# ones, though, because I don't want to have to
# extract the guild from every payload object for
# that small of a use-case.
SERVER_EVENT_NAMES = [
    "on_typing",

    "on_message","on_message_delete", "on_bulk_message_delete",

    "on_message_edit", "on_reaction_add", "on_reaction_remove",
    "on_reaction_clear", "on_reaction_clear_emoji",

    "on_interaction",

    "on_application_command", "on_application_command_completion",
    "on_application_command_error", "on_unknown_application_command",

    "on_private_channel_update", "on_private_channel_pins_update",

    "on_guild_channel_delete", "on_guild_channel_create",
    "on_guild_channel_update", "on_guild_channel_pins_update",

    "on_thread_join", "on_thread_create", "on_thread_remove",
    "on_thread_delete", "on_thread_update",

    "on_guild_integrations_update", "on_integration_create",
    "on_integration_update",

    "on_webhooks_update",

    "on_member_join", "on_member_remove", "on_member_update",

    "on_presence_update",
    "on_user_update",

    "on_guild_join", "on_guild_remove", "on_guild_update",

    "on_guild_role_create", "on_guild_role_delete", "on_guild_role_update",

    "on_guild_emojis_update", "on_guild_stickers_create",

    "on_guild_available", "on_guild_unavailable",
    
    "on_voice_state_update",

    "on_stage_instance_create", "on_stage_instance_delete",
    "on_stage_instance_update",

    "on_member_ban", "on_member_unban",

    "on_invite_create", "on_invite_delete",

    "on_group_join", "on_group_remove",

    "on_scheduled_event_create", "on_scheduled_event_update",
    "on_scheduled_event_delete", "on_scheduled_event_user_add",
    "on_scheduled_event_user_remove",

    "on_auto_moderation_rule_create", "on_auto_moderation_rule_update",
    "on_auto_moderation_rule_delete",
]

# As of right now this is just on_ready but idk.
# More later maybe.
UNIVERSAL_EVENT_NAMES = [
    "on_ready"
]
EVENT_NAMES = SERVER_EVENT_NAMES + UNIVERSAL_EVENT_NAMES

class ServerCog:
    def __init__(self, bot: Bot, guild: Guild, is_dm: bool = False):
        self.bot = bot
        self.guild = guild
        self.is_dm = is_dm
    
    _listeners: dict[str, dict[str, str]] = {}
    _slash_cmds: dict[str, dict[str, str]] = {}

    @classmethod
    def make_cog(cls, bot: Bot):
        return ServerCogGroup(cls, bot)

    @classmethod
    def listener(cls, name: str = None):
        def decorator(func):
            qn:str = func.__qualname__
            cog_cls = ".".join(qn.split(".")[:-1])
            ev_name = func.__name__ if name is None else name
            if ev_name not in cls._listeners:
                cls._listeners[ev_name] = {}
            l = cls._listeners[ev_name]
            l[cog_cls] = func.__name__
            return func
        return decorator
    
    @classmethod
    def slash_command(cls, name:str = None):
        def decorator(func):
            qn:str = func.__qualname__
            cog_cls = ".".join(qn.split(".")[:-1])
            cmd_name = func.__name__ if name is None else name
            if cog_cls not in cls._slash_cmds:
                cls._slash_cmds[cog_cls] = {}
            s = cls._slash_cmds[cog_cls]
            s[cmd_name] = func.__name__
            return func
        return decorator

class ServerCogGroup(Cog):
    def __init__(self, cog_type: Type[ServerCog], bot: Bot):
        super().__init__()
        self.cog_type = cog_type
        self.__cog_name__ = cog_type.__name__
        self.bot = bot
        self.servers = {}
        for event_name in EVENT_NAMES:
            # why isn't there just a try-else
            try:
                # Check if the entry exists in the dictionary
                # (there won't be an error if it does)
                _ = cog_type._listeners[event_name][cog_type.__name__]
            except KeyError:
                pass
            else:
                print("listening", event_name)
                bot.listen(event_name)(self.handle_event(event_name))
        
        if cog_type.__name__ in ServerCog._slash_cmds:
            cmds = ServerCog._slash_cmds[cog_type.__name__]
            for name, func_name in cmds.items():
                # Get an instance of the base command so func can wrap it
                base_func = getattr(cog_type(bot, DMS, True), func_name)

                # Create func that calls the appropriate cog's 
                @wraps(base_func)
                async def func(ctx, *args, **kwargs):
                    server_func = getattr(self.servers[ctx.guild.id], func_name)
                    return await server_func(ctx, *args, **kwargs)
                bot.add_application_command(slash_command(name=name)(func))
    
    @Cog.listener()
    async def on_ready(self):
        self.servers = {
            guild.id: self.cog_type(self.bot, guild) for guild in self.bot.guilds
        }
        self.servers[DMS] = self.cog_type(self.bot, DMS, True)
        if self.cog_type.__name__ in ServerCog._listeners["on_ready"]:
            await self.handle_event("on_ready", True)()
    
    @Cog.listener()
    async def on_guild_join(self, guild):
        self.servers[guild.id] = self.cog_type(self.bot, guild)
        if self.cog_type.__name__ in ServerCog._listeners["on_guild_join"]:
            await self.handle_event("on_guild_join", True)(guild)
    
    @Cog.listener()
    async def on_guild_remove(self, guild):
        del self.servers[guild.id]
        if self.cog_type.__name__ in ServerCog._listeners["on_guild_remove"]:
            await self.handle_event("on_guild_remove", True)(guild)
    
    def handle_event(self, name, force=False):
        disallowed_names = ["on_ready", "on_guild_join", "on_guild_remove"]
        if name in disallowed_names and not force:
            async def wrapped_none(*args):
                return None if not args else args[0]
            return wrapped_none
        # Wrapper for the function so we can choose the name synchronously
        if name in UNIVERSAL_EVENT_NAMES: # then run it in all cogs that have one
            async def wrapped(*args):
                # Find the name of the required function and run it with the args
                func_name = ServerCog._listeners[name][self.cog_type.__name__]
                for s in self.servers.values():
                    func = getattr(s, func_name)
                    await func(*args)
        else: # otherwise run it only for the guild's specific cog
            async def wrapped(*args):
                guild = find_guild(args)
                gid = DMS if guild==DMS else guild.id
                # Find the name of the required function and run it with the args
                func_name = ServerCog._listeners[name][self.cog_type.__name__]
                func = getattr(self.servers[gid], func_name)
                return await func(*args)
        return wrapped