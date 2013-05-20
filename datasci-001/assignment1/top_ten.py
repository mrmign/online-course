import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    hashtags = {}
    for line in tweet_file:
        obj = json.loads(line)
        if 'entities' in obj:
            ent = obj['entities']
            if ent['hashtags']:
                for h in ent['hashtags']:
                    # print h , type(h)
                    if h['text'] in hashtags.keys():
                        hashtags[h['text']] += 1
                    else:
                        hashtags[h['text']] = 1


    res = sorted(hashtags, key = hashtags.get, reverse=True)
    for r in res[:10]:
        print "%s %.1f" %(r, hashtags[r])


if __name__ == '__main__':
    main()