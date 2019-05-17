# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:35:10 2019

@author: KIIT
"""

import re
words_dict={}
def Calculate_words(filename):
    s=''
    try:
        with open(filename,encoding ='utf-8') as fp:
            s =fp.read().lower()
        words = re.findall(r'[a-z0-9]+',s)
        # Length of words
        words_dict[filename] = len(words)
        words_dict[filename] = (len(set(words)))
    except IOError:
        print('IOError')
    except Exception:
        print('Exception occurs')
    finally:
        print('Processed')
novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']
for i in novels:
    Calculate_words(i)

    
    # Searching these words
    """search = ["the", "while", "good", "bad", "ireland", "irish"]
    for word in search:
        print('Number of occurences {}--{}'.format(word,words.count(word)))
        
    #Number of different words
    '''d = {}
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word] = 1'''
    # Length of Unique words
    particular_words = set(words)
    print(len(particular_words))"""
    
        