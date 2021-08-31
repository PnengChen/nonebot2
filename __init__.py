from nonebot import on_command
import requests, re, json
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.plugin import export
from nonebot.adapters.cqhttp import Bot, MessageEvent, Message, Event, GroupMessageEvent
from nonebot.rule import Rule
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from .get_imge import get_express_img



# list填入你图片的名称，例如摩尔1.jpg的话，list=['摩尔1']
list = []


async def _checker(bot: Bot, event: Event, state: T_State) -> bool:
    return isinstance(event, MessageEvent)


expression = on_command('生成表情',priority=46,rule=Rule(_checker))


@expression.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["expression"] = args


@expression.got("expression", prompt="生成表情包类型及语句(例如:奥奇1/给我爬)？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    msg = state["expression"]
    s = str.split(msg, "/")
    if str(len(s)) != "2":
        await expression.finish("输入格式有误，若要生成表情请参照格式Ov<")
    else:
        if int(len(s[1])) >= 13:
            await expression.finish("输入字数过多，效果不佳，建议重试Ov<")
        else:
            if str(s[0]) in list:
                get_express_img(str(s[0]), str(s[1]))
                img_path = f'/home/xiaochen/database/image_express/output.jpg'
                img = MessageSegment.image(f'file://{img_path}')
                await expression.send(img)
            else:
                await expression.finish("生成表情范围有限Ov<")

