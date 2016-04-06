import re
s="uapvwtaadldgasxpbpaitgpixcvqtilttchtepgpidghiopccdnetdeat"
s="bdrzrzq"
# flag{hello_world-i_am-alterating_between-separators_t0-annoy_people!!!}
alph = "abcdefghijklmnopqrstuvwxyz"
new=''
for i in s:
    new+=alph[(alph.find(i)+11)%len(alph)]
print new
