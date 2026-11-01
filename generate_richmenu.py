#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LINEリッチメニュー画像(2500x1686・2x2)を生成する。
出勤/退勤/休憩開始/休憩終了の4ボタン。白極太ゴシック(NotoSansJP-Black)。
出力: richmenu.png（GitHub Pagesで配信→GASがfetchしてLINEへアップロード）。
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 2500, 1686
GAP = 12
CW, CH = (W - GAP) // 2, (H - GAP) // 2

FONT = "/Users/kisinomasasi/projects/_clients/nexus/brazil-taisou/assets/fonts/NotoSansJP-Black.ttf"

# 4象限: (ラベル, 英語, 背景色, 左上x, 左上y)
CELLS = [
    ("出勤",   "CLOCK IN",    (21, 101, 192),  0,         0),          # blue
    ("退勤",   "CLOCK OUT",   (57, 73, 171),   CW + GAP,  0),          # indigo
    ("休憩開始", "BREAK START", (96, 125, 139),  0,         CH + GAP),   # blue-gray
    ("休憩終了", "BREAK END",   (84, 110, 122),  CW + GAP,  CH + GAP),   # darker gray
]

img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

f_main = ImageFont.truetype(FONT, 230)
f_sub = ImageFont.truetype(FONT, 66)


def center(draw, cx, cy, text, font, fill):
    l, t, r, b = draw.textbbox((0, 0), text, font=font)
    draw.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=font, fill=fill)


for label, en, color, x, y in CELLS:
    d.rectangle([x, y, x + CW, y + CH], fill=color)
    cx, cy = x + CW / 2, y + CH / 2
    center(d, cx, cy - 40, label, f_main, (255, 255, 255))
    center(d, cx, cy + 150, en, f_sub, (255, 255, 255, 180))

img.save("/Users/kisinomasasi/projects/_clients/higashimatsuyama-gakudo/kintai-liff-site/richmenu.png", "PNG")
print("richmenu.png written", img.size)
