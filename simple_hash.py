# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:42:08 2025

@author: chenl

基本公式:index = hash(key) % capacity
当哈希表容量固定时, 哈希算法hash()决定了输出值,进而决定了键值对在哈希表中的分布情况.
设计好的哈希函数,可以降低哈希冲突发生的概率.
用大质数作为模数,可以最大化保证哈希值的均匀分布.
"""

def add_hash(key:str)->int:
    '''加法哈希'''
    hash = 0 
    modulus = 1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus

def mul_hash(key:str)->int:
    '''乘法哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash += 31*hash +ord(c)
    return hash % modulus

def xor_hash(key:str):
    '''异或哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus

def rot_hash(key:str):
    '''旋转哈希'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus

if __name__=='__main__':
    key = 'dcds'
    print(add_hash(key))
    print(mul_hash(key))
    print(xor_hash(key))
    print(rot_hash(key))
    
'''
414
3381491
16
402739
'''