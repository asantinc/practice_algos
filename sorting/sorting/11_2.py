from collections import defaultdict

'''
11.2 Sort an array of strings so that all anagrams are next to each other 
'''

def sort_anagrams(word_list):
    #sort each of the words
    #use a hash: O(n) time, where n is the number of letters
    hash_list = defaultdict(list)
    for w in word_list:
        #sort the letters
        key = ''.join(sorted(w))
        #append to hash
        hash_list[key].append(w)

    anagram_list = list()
    for key, values in hash_list.iteritems():
        for v in values:
            anagram_list.append(v)
    return anagram_list


if __name__ == '__main__':
    word_lists = [['abc', 'dfg', 'hik', 'bca', 'ihk', 'cba']
                ,[]
                ,['aaa','aaa']
                ,['asdfasdf', '-1234f', 'ffff', 'asdfasfd']
                 ]

    for word_list in word_lists:
        sorted_anagrams = sort_anagrams(word_list)
        print sorted_anagrams
       







    
