#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LINEリッチメニュー画像(2500x1686・2x2カテゴリ)を生成する。
出退勤 / 各種申請 / 出勤簿を見る / 連絡・会議。白極太ゴシック(NotoSansJP-Black)。
出力: richmenu.png
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 2500, 1686
GAP = 12
CW, CH = (W - GAP) // 2, (H - GAP) // 2
FONT = "/Users/kisinomasasi/projects/_clients/nexus/brazil-taisou/assets/fonts/NotoSansJP-Black.ttf"

# (ラベル, 英語, 背景色, x, y)
CELLS = [
    ("出退勤",     "CLOCK",      (21, 101, 192),  0,         0),
    ("各種申請",   "REQUESTS",   (57, 73, 171),   CW + GAP,  0),
    ("出勤簿を見る", "ATTENDANCE", (0, 137, 123),   0,         CH + GAP),
    ("連絡・会議",  "CONTACT",    (84, 110, 122),  CW + GAP,  CH + GAP),
]

img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)
f_sub = ImageFont.truetype(FONT, 62)


def fit_font(text, max_w):
    size = 230
    while size > 80:
        f = ImageFont.truetype(FONT, size)
        l, t, r, b = d.textbbox((0, 0), text, font=f)
        if (r - l) <= max_w:
            return f
        size -= 10
    return ImageFont.truetype(FONT, 80)


def center(cx, cy, text, font, fill):
    l, t, r, b = d.textbbox((0, 0), text, font=font)
    d.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=font, fill=fill)


for label, en, color, x, y in CELLS:
    d.rectangle([x, y, x + CW, y + CH], fill=color)
    cx, cy = x + CW / 2, y + CH / 2
    center(cx, cy - 45, label, fit_font(label, CW - 150), (255, 255, 255))
    center(cx, cy + 150, en, f_sub, (255, 255, 255))

img.save("/Users/kisinomasasi/projects/_clients/higashimatsuyama-gakudo/kintai-liff-site/richmenu.png", "PNG")
print("richmenu.png written", img.size)
