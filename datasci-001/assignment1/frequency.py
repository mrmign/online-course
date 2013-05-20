import sys
import json

def main():
    twe_file = open(sys.argv[1])
    terms_dict = {}
    terms_cnt = 0
    for line in twe_file:
        entity = json.loads(line)
        if 'text' in entity:
            text = entity['text']
            terms = text.split()
            terms_cnt += len(terms)
            for t in terms:
                if t in terms_dict:
                    terms_dict[t] += 1
                else:
                    terms_dict[t] = 1

    for k,v in terms_dict.items():
        print "%s %.3f" %(k, float(v)/terms_cnt)




if __name__ == '__main__':
    main()