'''
Sort letters in one word by order they occur in another in linear time 
'''

from collections import defaultdict


def main(word1, word2):
	counts = defaultdict(int)
	for char in word2:
		counts[char] += 1
	output = list()

	for char in word1:
		if char in counts:
			for x in range(counts[char]):
				output.append(char)
	return ''.join(output)



if __name__ == '__main__':
	word1, word2 = 'apetxgriubncvl', 'angela'
	print main(word1, word2)

	word1, word2 = 'apetxgriubncvl', ''
	print main(word1, word2)

	word1, word2 = 'apetxgriubncvl', 'xxxx'
	print main(word1, word2)

	word1, word2 = 'apetxgriubncvl', 'ts'
	print main(word1, word2)