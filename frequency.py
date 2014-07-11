import sys
import json

def read_tweet(tweet_line):
	""" convert json line to tweet text """
	tweet = json.loads(tweet_line)
	try:
		tweet_text = tweet['text']
	except:
		tweet_text = ""
	return tweet_text.encode('utf-8') 
	
def normalize_dictionary(word_dictionary,word_count):
	""" normalize each element of the dictionary """
	for key in word_dictionary.keys():
		word_dictionary[key] = 1.*word_dictionary[key]/word_count
	return word_dictionary
	
def print_dictionary(word_dictionary):
	for key in word_dictionary.keys():
		print key," ",word_dictionary[key]


def main():
	tweet_file = open(sys.argv[1])
	word_dictionary = {}
	word_count = 0
	for line in tweet_file.readlines():
		tweet = read_tweet(line)
		for word in tweet.split():
			word_count += 1
			if word in word_dictionary.keys():
				word_dictionary[word]+=1
			else:
				word_dictionary[word]=1
	word_dictionary = normalize_dictionary(word_dictionary,word_count)
	print_dictionary(word_dictionary)

if __name__ == '__main__':
    main()
