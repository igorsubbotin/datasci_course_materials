import json
import sys
import re

def main():
    tweet_file = open(sys.argv[1])
    hashTags = {}
    for line in tweet_file:
        data = json.loads(line)
        if "entities" in data:
            for hashtag in data["entities"]["hashtags"]:
                ht = hashtag["text"]
                if ht not in hashTags:
                    hashTags[ht] = 0
                hashTags[ht] += 1
    for it in sorted(hashTags, key=hashTags.get, reverse=True)[0:10]:
        print it + " " + str(hashTags[it])

if __name__ == '__main__':
    main()
