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

sid_arg = Args["sid", int, None]

alc = Alconna(
    "steam",
    Subcommand(
        ".add",
        alias=["绑定", "添加"],
        sid_arg,
        
        Option("-r|--requirement", Args["file", str]),
        Option("-i|--index-url", Args["url", str]),
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
)
