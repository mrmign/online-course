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
    # tweet_file = open("submit_1.txt")
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    sent_scores = {}
    new_sent = {}
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
                if t.encode("utf-8") in sent_keys:
                    t_score += sent_scores[t.encode("utf-8")]

            for t in terms:
                if t.encode("utf-8") not in sent_keys:
                    if t.encode("utf-8") in new_sent.keys():
                        new_sent[t.encode("utf-8")].append(t_score)
                    else:
                        new_sent[t.encode("utf-8")] = [t_score]

    for k,v in new_sent.items():
        score = float(sum(v))/len(v)
        print "%s %.3f" %(k, score)

if __name__ == '__main__':
    main()
