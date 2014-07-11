import sys
import json

# US states dictionary
states = {
		'AK': 'Alaska',
		'AL': 'Alabama',
		'AR': 'Arkansas',
		'AS': 'American Samoa',
		'AZ': 'Arizona',
		'CA': 'California',
		'CO': 'Colorado',
		'CT': 'Connecticut',
		'DC': 'District of Columbia',
		'DE': 'Delaware',
		'FL': 'Florida',
		'GA': 'Georgia',
		'GU': 'Guam',
		'HI': 'Hawaii',
		'IA': 'Iowa',
		'ID': 'Idaho',
		'IL': 'Illinois',
		'IN': 'Indiana',
		'KS': 'Kansas',
		'KY': 'Kentucky',
		'LA': 'Louisiana',
		'MA': 'Massachusetts',
		'MD': 'Maryland',
		'ME': 'Maine',
		'MI': 'Michigan',
		'MN': 'Minnesota',
		'MO': 'Missouri',
		'MP': 'Northern Mariana Islands',
		'MS': 'Mississippi',
		'MT': 'Montana',
		'NA': 'National',
		'NC': 'North Carolina',
		'ND': 'North Dakota',
		'NE': 'Nebraska',
		'NH': 'New Hampshire',
		'NJ': 'New Jersey',
		'NM': 'New Mexico',
		'NV': 'Nevada',
		'NY': 'New York',
		'OH': 'Ohio',
		'OK': 'Oklahoma',
		'OR': 'Oregon',
		'PA': 'Pennsylvania',
		'PR': 'Puerto Rico',
		'RI': 'Rhode Island',
		'SC': 'South Carolina',
		'SD': 'South Dakota',
		'TN': 'Tennessee',
		'TX': 'Texas',
		'UT': 'Utah',
		'VA': 'Virginia',
		'VI': 'Virgin Islands',
		'VT': 'Vermont',
		'WA': 'Washington',
		'WI': 'Wisconsin',
		'WV': 'West Virginia',
		'WY': 'Wyoming'
}
states_inv = {v.lower():k for k, v in states.items()}

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
	#get text 
	try:
		tweet_text = tweet['text']
	except:
		return ""
	# get only tweets in english
	if 	tweet['lang'] != 'en':
		return ""
	return tweet_text.encode('utf-8')
	
def calculate_tweet_score(tweet,scores):
	""" Calculate tweet total sentiment """
	tweet = tweet.split(" ")
	tweet_score = 0
	for word in tweet:
		tweet_score += scores.get(word,0)
	return tweet_score
	
def calculate_tweet_state(tweet_line):
	""" get tweet state """
	tweet = json.loads(tweet_line)
	location = tweet['user']['location']
	state = get_state(location)
	return state

def get_state(location):
	""" calculate state from the location """
	names = location.split(',')	
	for name in names:
		name = name.strip()
		if name in states.keys():
			return name
		if name.lower() in states_inv.keys():
			return states_inv[name.lower()]
	return ""

def calculate_avg_score(state_score,state_count):
	""" divide each score by the number of tweets in each state"""
	for state in state_score.keys():
		state_score[state] = 1.*state_score[state]/state_count[state]
	return state_score

def find_happiest_state(state_score):
	""" Calculate happiest state from the dictionary """
	max_happiness = -10000
	happiest_state = ""
	for state in state_score.keys():
		if max_happiness<state_score[state]:
			max_happiness = state_score[state]
			happiest_state = state
	return state
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = build_sentiment_dict(sent_file)
	state_score = {}
	state_count = {}
	for line in tweet_file.readlines():
		tweet = read_tweet(line)
		if len(tweet)>0:
			tweet_score = calculate_tweet_score(tweet,scores)
			tweet_state = calculate_tweet_state(line)
			if len(tweet_state)>0:
				if tweet_state not in state_score.keys():
					state_score[tweet_state] = tweet_score
					state_count[tweet_state] = 1
				else:
					state_score[tweet_state] += tweet_score
					state_count[tweet_state] += 1
	state_score = calculate_avg_score(state_score,state_count)
	happiest_state = find_happiest_state(state_score)
	print happiest_state
if __name__ == '__main__':
	main()
