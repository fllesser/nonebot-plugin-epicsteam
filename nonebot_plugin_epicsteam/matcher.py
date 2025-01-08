from nonebot import require
from nonebot.log import logger

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import on_alconna
from arclet.alconna import (
    Alconna,
    Args,
    Subcommand, 
    Option
)


range_args = Args["range", ".there|.global", ".there"]
sid_args = Args["sid", "re:\d{10}", None]

add_cmd = Subcommand(".add", alias=["绑定", "添加"], sid_args)
del_cmd = Subcommand(".del", alias=["解绑", "删除"], sid_args)
refresh_cmd = Subcommand(".rfrs", alias=["刷新"], sid_args)
list_cmd = Subcommand(".list", alias=["列表"]),
on_cmd = Subcommand(".on", alias=["开启"], range_arg)
off_cmd = Subcommand(".off", alias=["关闭"], range_arg)

# 创建Alconna实例并添加子命令
epic_alc = Alconna(
    "epic",
    add_cmd,
    del_cmd,
    refresh_cmd,
    list_cmd,
    on_cmd,
    off_cmd
)

steam_alc = Alconna(
    "steam",
    add_cmd,
    del_cmd,
    refresh_cmd,
    list_cmd,
    on_cmd,
    off_cmd
)

epicsteam = on_alconna(
    command = epic_alc | steam_alc
)