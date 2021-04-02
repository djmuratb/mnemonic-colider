# mnemonic-colider

Зависимости:
Python 3.7 и выше

https://github.com/dnanhkhoa/simple-bloom-filter
sudo pip3 install simplebloomfilter

https://github.com/trezor/python-mnemonic
sudo pip3 install mnemonic

sudo apt-get install libgmp-dev
sudo apt-get install libmpfr-dev
sudo apt-get install libmpc-dev
sudo pip3 install --user gmpy2==2.1.0a2
sudo pip3 install ecdsa[gmpy2]

Windows
https://www.lfd.uci.edu/~gohlke/pythonlibs/
gmpy2‑2.0.8‑cp38‑cp38‑win_amd64.whl
pip3 install gmpy2-2.0.8-cp38-cp38-win_amd64.whl

https://github.com/ebellocchia/bip_utils
sudo pip3 install bip_utils

создайте BloobFilter (BF create\Cbloom.py)
пример:
python Cbloom.py <in file> <outfile>
  in file - текстовый файл с адресами (один адрес на одну срочку)
  out file - файл блюм фильтра

используйте программу
  python main.py -b <BIP 32 или 44> -d <директория с файлами блюм фильтра>
 
файлы с адресами брать здесь
https://gz.blockchair.com/

или на моем ресурсе
https://drive.google.com/drive/folders/1yKvE6YsAzQdk2gCzRWR8Zyn74Ai3_S0v?usp=sharing
