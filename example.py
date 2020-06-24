#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from opencc import OpenCC


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('Require Python3 to run')
        sys.exit(0)

    words_t = '這裡有個著名的話，胡同和胡同之間不知道那是什麼了。'
    words_s = '這裡有個著名的話，胡同和胡同之間不知道那是什麼了。'
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
