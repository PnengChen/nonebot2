import os
from PIL import Image, ImageDraw, ImageFont
import time
import urllib.parse


# 使用图片拼接在下方
def get_express_img(keys,text):
    keys=urllib.parse.quote(keys)
    path = f'/home/xiaochen/database/image/{keys}.jpg'
    
    im = Image.open(path)
    w, h = im.size
    font = ImageFont.truetype(f'/home/xiaochen/database/Fronts/msyh.ttc', 25)  # 终端
    # 计算使用该字体占据的空间
    # 返回一个 tuple (width, height)
    # 分别代表这行字占据的宽和高
    t_w, t_h = font.getsize(text)
    # print(t_w, t_h)
    text_size = (w, t_h + 20)
    bg = Image.new('RGB', text_size, color='white')
    draw = ImageDraw.Draw(bg)
    text_coordinate = ((w - t_w) / 2, 10)
    draw.text(text_coordinate, text, (0, 0, 0), font=font)

    f_size = (w, h + t_h)
    f = Image.new('RGB', f_size, color='white')
    f.paste(im, (0, 0))
    f.paste(bg, (0, (h - t_h)))
    # 引入时间区分文件名
    # x = time.localtime(time.time())
    # y = time.strftime('%Y%m%d%H%M%S', x)
    #img_path = f'{os.getcwd()}/src/plugins/make_express/database/image_express/{keys}{y}.jpg'
    # out_path = f'/home/xiaochen/src/plugins/make_express/database/image_express/output.jpg'
    out_path = f'/home/xiaochen/database/image_express/output.jpg'
    f.save(str(out_path))
    

