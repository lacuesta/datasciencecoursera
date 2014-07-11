import sys
import json


 # initialize an empty dictionary
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def build_sentiment_dict(afinnfile):
	""" Build the sentiment dictionary from text file """
	scores = {}
	for line in afinnfile.readlines():
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores
	
	

def read_tweet(tweet_line):
	""" convert json line to tweet text """
	tweet = json.loads(tweet_line)
	try:
		tweet_text = tweet['text']
	except:
		tweet_text = ""
	return tweet_text.encode('utf-8')
	
def calculate_tweet_score(tweet,scores):
	""" Calculate tweet total sentiment """
	tweet = tweet.split(" ")
	tweet_score = 0
	for word in tweet:
		tweet_score += scores.get(word,0)
	return tweet_score



	
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = build_sentiment_dict(sent_file)
    for line in tweet_file.readlines():
    	tweet = read_tweet(line)
    	if len(tweet)>0:
	    	tweet_score = calculate_tweet_score(tweet,scores)
	    	print tweet_score

if __name__ == '__main__':
    main()
