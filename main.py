#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import glob
import yaml
import datetime
from PIL import Image

filename = "./config.yml"

try:
    with open(filename, "r") as config:
        data = yaml.load(config)
        print(data)
    # return data
except:
    raise Exception("設定ファイルを見直してください")

def get_image_resize(width, height):
    ret = {}
    ret["width"] = width
    ret["height"] = height
    if( ret["width"] > data['resize']['width'] ):
        resize_gain = ret["width"] / data["resize"]["width"]
        ret["width"] /= resize_gain
        ret["height"] /= resize_gain
    if( ret["height"] > data["resize"]["height"] ):
        resize_gain = ret["height"] / data["resize"]["height"]
        ret["width"] /= resize_gain
        ret["height"] /= resize_gain
    return ret

if __name__ == "__main__":
    # readconfig("./config.yml")
    files = glob.glob('./target/*')
    date_dir = '{0:%Y%m%d%H%M%S}/'.format(datetime.datetime.now())
    if not os.path.exists('./convert/' + date_dir):
        os.mkdir('./convert/' + date_dir)
    for f in files:
        img = Image.open(f)
        # img_resize = img.resize((256, 256))
        resize = get_image_resize(img.width, img.height)
        print(resize)
        img.thumbnail((resize["width"], resize["height"]), Image.ANTIALIAS)

        # img_resize = img.resize((int(resize["width"]), int(resize["height"])))
        dir_name = os.path.dirname(f).replace('/target','/convert/')
        # dir_name = dir_name + date_dir
        # backup_dir_name = dir_name.replace('/convert/','/backup/')
        filename = os.path.basename(f)
        # ftitle, fext = os.path.splitext(f)
        img.save('./convert/' + date_dir + filename)
        # shutil.move('', dir_name + ftitle + fext)