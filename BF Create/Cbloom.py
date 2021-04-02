#!/usr/bin/python
# -*- coding: utf-8 -*-
from bloomfilter import BloomFilter
import sys


def count_lines(file):
	return sum(1 for line in open(file, 'r'))


def add_to_bf(file, nom, bf_filter):
    i = 0
    line_10 = 100000
    f = open(file)
    while i < nom:
        if line_10 == i:
            print("Total line ->" + str(line_10), end='\r')
            line_10 += 100000
        text = f.readline().strip()
        bf_filter.add(text)
        i += 1
    f.close()


def bloom_filter():
    print("========== Bloom Filter START==========")
    print("===========File input -> " + file_txt)
    print("===========File output -> " + file_bf)
    bf = BloomFilter(size=line_count, fp_prob=1e-9)

    print("========== ADD Bloom Filter ==========")
    add_to_bf(file_txt, line_count, bf)

    # Print several statistics of the filter
    print("========== Bloom Filter Statistic ==========")
    print(
        "+ Capacity: {} item(s)".format(bf.size),
        "+ Number of inserted items: {}".format(len(bf)),
        "+ Filter size: {} bit(s)".format(bf.filter_size),
        "+ False Positive probability: {}".format(bf.fp_prob),
        "+ Number of hash functions: {}".format(bf.num_hashes),
        "+ Input file: {}".format(file_txt),
        "+ Output file: {}".format(file_bf),
        sep="\n",
        end="\n\n",
    )

    # Save to file
    print("========== Bloom Filter Start Save File ==========")
    with open(file_bf, "wb") as fp:
        bf.save(fp)
    print("========== Bloom Filter END Save File ==========")


if __name__ == "__main__":

    if len (sys.argv) < 3:
        print ("Ошибка. Слишком мало параметров.")
        sys.exit (1)

    if len (sys.argv) > 3:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    file_txt = sys.argv[1]
    file_bf = sys.argv[2]

    line_count = count_lines(file_txt)
    print("all lines -> " + str(line_count))
    bloom_filter()
