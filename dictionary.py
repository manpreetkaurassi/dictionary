import json
from difflib import get_close_matches
data = json.load(open("data.json"))
store_word = ""

def search(w):
    w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #if user entered "USA" this will check for "USA" as well.
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8)) >0:
        yn =  input("Did you mean %s instead?(Y/N)"%get_close_matches(w,data.keys(),cutoff=0.8)[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =="N":
            return "The word doesn't exist in the dictionary. Pkease double check"
        else:
            return "We didnt understant your entry"
    else:
        return "Please recheck the word"
   

word = input("Which word's definition would you like to know ")
value = search(word)

if(type(value)==list):
    for item in value:
        print(item)
else:
    print(value)



