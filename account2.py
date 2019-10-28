import collections
import re

patt = re.compile('\w+')
counter = collections.Counter(patt.findall(
    open('a.txt','rt').read()
))

#top 10
for word, times in counter.most_common(10):
    print (word, times)

#find word
counter_dict = dict(counter.most_common(10))
tobefind = 'hello'
print (tobefind, counter_dict.get(tobefind, 0))