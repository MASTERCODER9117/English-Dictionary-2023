import json
from difflib import get_close_matches
data=json.load(open('dictionary.json'))
def translate(word):
    word=word.lower()
    if word in data :
        return data [word]
    elif len(get_close_matches(word,data.keys()))>0:
        y=input('Did You Mean %s instead? Enter Y for yes and N for no:'% get_close_matches(word,data.keys())[0])
        y=y.lower()
        if y=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif y=='n':
            return "The word dosen't exist please double check."
        else:
            return "We did not understand your entry, please press y/n"
    else:
        return "The word dosen't exist please double check."
d=(input(" Please write the words whos meaning you want.")) 
output=translate(d)
if type(output)==list:
    for item in output:
        print(item)
else : 
   
     print (output)        