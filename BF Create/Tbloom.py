# #!/usr/bin/python3
# encoding=utf8
# -*- coding: utf-8 -*-
from bloomfilter import BloomFilter

file_bf = ['btc.bf','cash.bf','sv.bf','dash.bf','doge.bf','eth.bf','ltc.bf']
file_rezult = 'rezult.txt'

def save_rezult(header,text):
    f_rez = open(file_rezult,'a')
    f_rez.write(header+' -> ')
    f_rez.write(text+'\n')
    f_rez.close


def bloom_filter():
    print('============== START =================')
    global bf_btc, bf_abc, bf_sv, bf_dash, bf_dogecoin, bf_eth, bf_ltc

    with open(file_bf[0], "rb") as fp:
        bf_btc = BloomFilter.load(fp)

    with open(file_bf[1], "rb") as fp:
        bf_abc = BloomFilter.load(fp)

    with open(file_bf[2], "rb") as fp:
        bf_sv = BloomFilter.load(fp)

    with open(file_bf[3], "rb") as fp:
        bf_dash = BloomFilter.load(fp)

    with open(file_bf[4], "rb") as fp:
        bf_dogecoin = BloomFilter.load(fp)

    with open(file_bf[5], "rb") as fp:
        bf_eth = BloomFilter.load(fp)

    with open(file_bf[6], "rb") as fp:
            bf_ltc = BloomFilter.load(fp)

def find_bf(addr, link_bf):
    print('============== Find =================')
    if addr in link_bf:
        save_rezult(addr,'TRUE')
        print(f'"{addr}" TRUE')
        return True
    else:
        save_rezult(addr,'False')
        print(f'"{addr}" FALSE')
        return False


def main():
    bloom_filter()
    find_bf('1111111111111111111141MmnWZ', bf_btc) #
    find_bf('1K84KfbFi8K9UGrbJZfh4sPcV9iLLi9v', bf_btc) #
    find_bf('19uQ7hJwFavF92V6fsWGNRk8RKoBCwiEeb', bf_btc) #
    find_bf('1111111111111111111141MmnWZ', bf_abc) # false
    find_bf('qzftxpv7xu5l673q3jacjy9q0962kxqdsv55fhu4h3', bf_abc) #true
    find_bf('1ATbs66QvSZCLvctZCuUhuEDBMe3WQ2DG1', bf_sv) # true
    find_bf('1111111111111111111141MmnWZ', bf_sv) # false
    find_bf('1111111111111111111141MmnWZ', bf_dash) # false
    find_bf('7Z1GDr2zuVHsokSvdg4BiGAZv1X9KJnwmc', bf_dash) # true
    find_bf('1111111111111111111141MmnWZ', bf_eth) #
    find_bf('1111111111111111111141MmnWZ', bf_eth) #
    find_bf('ltc1qhg3zap7ntlrmcklh432mja6yvj50thn39w9yu3', bf_ltc) #
    find_bf('LVTV1ZE5iQJvLatWobTY1SGyfnE8CUr5RC', bf_ltc) #


if __name__== "__main__":
    main()