#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from opencc import OpenCC


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print('Require Python3 to run')
        sys.exit(0)

    words_t = '家庭 规模 缩小 是 其中 最 大 的 改变 。 现在 一 个 中国 家庭 平均 人数 不到 四 人 ， 过去 三代同堂 的 家庭 已经 很 少见 ， 取代 传统 家庭 的 是 只有 父母 跟 孩子 住 在 一起 的 核心 家庭 。 这 可能 是 因为 政府 的 鼓励 政策 ； 可能 是 因为 城市 工作 机会 多 ， 很 少 人 愿意 回 乡下 住 。'
    words_s = '家庭 规模 缩小 是 其中 最 大 的 改变 。 现在 一 个 中国 家庭 平均 人数 不到 四 人 ， 过去 三代同堂 的 家庭 已经 很 少见 ， 取代 传统 家庭 的 是 只有 父母 跟 孩子 住 在 一起 的 核心 家庭 。 这 可能 是 因为 政府 的 鼓励 政策 ； 可能 是 因为 城市 工作 机会 多 ， 很 少 人 愿意 回 乡下 住 。'
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
