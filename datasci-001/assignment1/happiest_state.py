import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # sent_file = open("AFINN-111.txt")
    # tweet_file = open("submit_1.txt")
    sent_scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        sent_scores[term] = int(score)

    sent_keys = sent_scores.keys()
    max_score = 0
    max_st = ""
    for li in tweet_file:
        entity = json.loads(li)
        # calculate tweet sentiment score
        t_score = 0;
        if 'text' in entity:
            text = entity['text']
            terms = text.split()
            for t in terms:
                if t.encode("utf-8") in sent_keys:
                    t_score += sent_scores[t.encode("utf-8")]

        if t_score > max_score:
            if entity["place"]:
                place = entity["place"]
                if place["country_code"] == "US":
                    full_name = place["full_name"]
                    max_st = full_name.split()[-1]

    # print max_score, max_st
    print max_st


if __name__ == '__main__':
    main()