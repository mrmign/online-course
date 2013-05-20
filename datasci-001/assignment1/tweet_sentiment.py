import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # sent_file = open("AFINN-111.txt")
    # tweet_file = open("output.txt")
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    sent_scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        sent_scores[term] = int(score)

    sent_keys = sent_scores.keys()

    for li in tweet_file:
        entity = json.loads(li)
        if 'text' in entity:
            text = entity['text']
            terms = text.split()
            t_score = 0;
            for t in terms:
                if t in sent_keys:
                    t_score += sent_scores[t]

            print"%0.2f" %t_score



if __name__ == '__main__':
    main()
