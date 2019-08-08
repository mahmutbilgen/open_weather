'''
json load,loads, dump, dumps Tutorial


'''

import json

jvalue_str = """
    {"title": "Tron: Legacy",
    "composer": "Daft Punk",
    "release_year" :  2010,
    "budget": 1700000000,
     "actors":null,
     "won_orcar":false
     }"""

tron_dic = json.loads(jvalue_str)   # json.loads fuction convert STRING value to DICTIONARY value

print(f"Tron Dict Value : {tron_dic}")

str_movie = json.dumps(tron_dic)

str_movie = json.dumps(tron_dic,ensure_ascii=False) # to avoid NON-ascii character write as is


print(f"Movie String  Value : {str_movie}")

movie2 = {}
movie2["title"] = "Minorty Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell","Samantha Morton","Max von Sydow"]
movie2["is_awesome"]=True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

jfile= open("./json_file_sample2.json","w",encoding="utf-8")
json.dump(movie2, jfile, ensure_ascii=False)
jfile.close()