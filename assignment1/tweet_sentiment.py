import json
import sys
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        data = json.loads(line)
        if "text" in data:
            text = data["text"]
            score = 0
            for word in re.findall(r"[\w']+", text):
                word = word.lower()
                if word in scores:
                    score += scores[word]
            print str(score)

if __name__ == '__main__':
    main()
