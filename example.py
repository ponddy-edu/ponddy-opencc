#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from opencc import OpenCC


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('Require Python3 to run')
        sys.exit(0)

    words_t = '後臺砲有個很醜的人，他開車從南迴到台東，中途遇到一隻羊，捲了一卷煙給羊抽，他看了看手錶，發現時間差不多，就驅車前往萬里長城吃麵條配雲吞湯，然後什麼事情都沒幹就回家睡覺了。'
    words_s = '后台炮有个很丑的人，他开车从南回到台东，中途遇到一只羊，卷了一卷烟给羊抽，他看了看手表，发现时间差不多，就驱车前往万里长城吃面条配云吞汤，然后什么事情都没干就回家睡觉了。'
    openCC_ponddy_t2s = OpenCC('ponddy_t2s')
    tword_ponddy_t2s_result = openCC_ponddy_t2s.convert(words_t)
    sword_ponddy_t2s_result = openCC_ponddy_t2s.convert(words_s)

    openCC_t2s = OpenCC('t2s')
    tword_t2s_result = openCC_t2s.convert(words_t)
    sword_t2s_result = openCC_t2s.convert(words_s)

    openCC_ponddy_s2t = OpenCC('ponddy_s2t')
    tword_ponddy_s2t_result = openCC_ponddy_s2t.convert(words_t)
    sword_ponddy_s2t_result = openCC_ponddy_s2t.convert(words_s)

    openCC_s2t = OpenCC('s2t')
    tword_s2t_result = openCC_s2t.convert(words_t)
    sword_s2t_result = openCC_s2t.convert(words_s)

    print("\n\n**original trad:{}\n-o_t2s:{}\n-p_t2s:{}\n\n-o_s2t:{}\n-p_s2t:{}".format(words_t, tword_t2s_result, tword_ponddy_t2s_result, tword_s2t_result, tword_ponddy_s2t_result))
    print("\n\n**original simp:{}\n-o_t2s:{}\n-p_t2s:{}\n\n-o_s2t:{}\n-p_s2t:{}".format(words_s, sword_t2s_result, sword_ponddy_t2s_result, sword_s2t_result, sword_ponddy_s2t_result))
