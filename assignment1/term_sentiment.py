import json
import sys
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    my_scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        data = json.loads(line)
        if "text" in data:
            text = data["text"]
            score = 0
            words = re.findall(r"[\w']+", text)
            for word in words:
                word = word.lower()
                if word in scores:
                    score += scores[word]
            for word in words:
                word = word.lower()
                if word not in my_scores:
                    my_scores[word] = 0.0
                my_scores[word] += score/float(len(words))*10
    for key in my_scores.keys():
        print key + " " + str(round(my_scores[key], 2))

if __name__ == '__main__':
    main()
