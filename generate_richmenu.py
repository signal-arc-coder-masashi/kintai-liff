#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LINEリッチメニュー画像(2500x1686)を生成する。
上段(大): 出勤 / 退勤   下段: 休憩開始 / 休憩終了 / 出勤簿を見る
白極太ゴシック(NotoSansJP-Black)。出力: richmenu.png
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 2500, 1686
GAP = 12
TOP_H = 1000
BOT_H = H - TOP_H  # 686
FONT = "/Users/kisinomasasi/projects/_clients/nexus/brazil-taisou/assets/fonts/NotoSansJP-Black.ttf"

img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)
f_big = ImageFont.truetype(FONT, 260)
f_mid = ImageFont.truetype(FONT, 130)
f_sub = ImageFont.truetype(FONT, 60)
f_sub2 = ImageFont.truetype(FONT, 46)


def center(cx, cy, text, font, fill):
    l, t, r, b = d.textbbox((0, 0), text, font=font)
    d.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=font, fill=fill)


# 上段: 出勤 / 退勤
top = [
    ("出勤", "CLOCK IN", (21, 101, 192), 0, 1250),
    ("退勤", "CLOCK OUT", (57, 73, 171), 1250 + GAP, 1250 - GAP),
]
for label, en, color, x, w in top:
    d.rectangle([x, 0, x + w, TOP_H - GAP // 2], fill=color)
    cx, cy = x + w / 2, TOP_H / 2
    center(cx, cy - 55, label, f_big, (255, 255, 255))
    center(cx, cy + 165, en, f_sub, (255, 255, 255))

# 下段: 休憩開始 / 休憩終了 / 出勤簿を見る
bw = (W - GAP * 2) // 3
bot = [
    ("休憩開始", "BREAK START", (96, 125, 139), 0),
    ("休憩終了", "BREAK END", (84, 110, 122), bw + GAP),
    ("出勤簿を見る", "ATTENDANCE", (0, 137, 123), (bw + GAP) * 2),
]
by = TOP_H + GAP // 2
for label, en, color, x in bot:
    d.rectangle([x, by, x + bw, H], fill=color)
    cx, cy = x + bw / 2, by + BOT_H / 2
    center(cx, cy - 40, label, f_mid, (255, 255, 255))
    center(cx, cy + 115, en, f_sub2, (255, 255, 255))

img.save("/Users/kisinomasasi/projects/_clients/higashimatsuyama-gakudo/kintai-liff-site/richmenu.png", "PNG")
print("richmenu.png written", img.size)
