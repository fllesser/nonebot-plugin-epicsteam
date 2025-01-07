from nonebot import require
from nonebot.log import logger
from nonebot.rule import Rule

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import on_alconna
from arclet.alconna import (
    Alconna,
    Args,
    Subcommand, 
    Option
)

sid_arg = Args["sid", "re:\d{10}", None]
range_arg = Args["range", ".there|.global", ".there"]

alc = Alconna(
    "steam",
    Subcommand(
        ".add",
        alias=["绑定", "添加"],
        sid_arg
    ),
    Subcommand(
        ".del",
        alias=["解绑", "删除"],
        sid_arg
    ),
    Subcommand(
        ".rfrs",
        alias=["刷新"],
        sid_arg
    ),
    Subcommand(
        ".list",
        alias=["列表"]
    ),
    Subcommand(
        ".on",
        alias=["开启"],
        range_arg
    ),
    Subcommand(
        ".off",
        alias=["关闭"],
        range_arg
    )
    
)
