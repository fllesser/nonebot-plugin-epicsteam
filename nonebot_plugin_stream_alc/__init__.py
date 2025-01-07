from nonebot import (
    require,
    get_driver, # @get_driver().on_startup 装饰启动时运行函数
    get_bots    # dict[str, BaseBot]
)
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

from .matcher import alc

__plugin_meta__ = PluginMetadata(
    name="Steam游戏状态广播",
    description="播报群友的Steam游戏状态",
    usage="""首先获取自己的Steam ID，
        获取方法：
            获取Steam ID 64
                Steam 桌面网站或桌面客户端：点开右上角昵称下拉菜单，点击账户明细，即可看到 Steam ID
                Steam 应用：点击右上角头像，点击账户明细，即可看到 Steam ID
            获取Steam好友代码
                Steam 桌面网站或桌面客户端：点开导航栏 好友 选项卡，点击添加好友，即可看到 Steam 好友代码
                Steam 应用：点击右上角头像，点击好友，点击添加好友，即可看到 Steam 好友代码
        (如果有命令前缀，需要加上，一般为 / )    
        
        绑定方法：
            steam绑定/steam添加/steam.add [个人ID数值] 
            
        删除方法：
            steam解绑/steam删除/steam.del [个人ID数值] 
            
        管理员命令：
            steam列表/steam绑定列表 	    
            steam播报开启/steam播报打开  
            steam播报关闭/steam播报停止 
            steam屏蔽 xx/steam恢复 xx
            steam排除列表	
    """,
    type="application",
    config=Config,
    homepage="https://github.com/fllesser/nonebot-plugin-steam-alc",
    supported_adapters={"~onebot.v11"},
    extra={
        "author":"fllesser",
        "version":__version__,
        "priority":config_dev.steam_command_priority
    }
)

