from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event, MessageSegment, GroupMessageEvent, MessageEvent
from nonebot.rule import Rule
from nonebot.plugin import export
from aiocqhttp.exceptions import Error as CQHttpError
import time
import requests
import urllib.parse
import re
from lxml import etree # 导入xpath
from urllib import request
from .tieba_gl import get_tieba_data
from src.service.group_manage import group_range
import sys
import io
import requests

export = export()
export.name = '贴吧攻略查找'
export.usage = '/攻略'

group_l = group_range()
group_limits = group_l[export.name]


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    if isinstance(event, GroupMessageEvent):
        group = str(event.group_id)
        # 群聊黑名单
        if group in group_limits:
            x = False
        else:
            x = True
    else:
        x = True
    return x


introduction = on_command("攻略", priority=47, rule=Rule(_checker))


@introduction.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["introduction"] = args


@introduction.got("introduction", prompt="现在可以开始查询贴吧攻略了，请输入要查询的内容")
async def handle_city(bot: Bot, event: Event, state: T_State):
    msg = state["introduction"]
    res = await get_tieba_data(msg)
    try:
        await introduction.send('请稍等，正在努力寻找，请稍等...')
        time.sleep(0.5)
        await introduction.finish(Message(str(res)))
    except CQHttpError:
        pass



