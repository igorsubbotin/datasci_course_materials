import json
import sys
import re

def main():
    tweet_file = open(sys.argv[1])
    freq = {}
    for line in tweet_file:
        data = json.loads(line)
        if "text" in data:
            text = data["text"]
            words = re.findall(r"[\w']+", text)
            for word in words:
                word = word.lower()
                if word not in freq:
                    freq[word] = 0
                freq[word] += 1
    total = sum(freq.values())
    for key in freq:
        print key + " " + str(round(freq[key]/float(total), 2))
if __name__ == '__main__':
    main()
