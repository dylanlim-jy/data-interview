"""
Q1a. Extract the 'characters' in `json_str` into a list of dictionaries
Q1b. For each dictionary in the list:
        i) Split the 'name' values into 'fname' and 'lname'
        ii) Add 10 to the age of characters who are younger than 40 years old
        iii) Convert the list of dictionaries into three lists, `fname`, `lname`, and `ages`
"""

from ..data.objects import json_str
import json 

response = json.loads(json_str)
char_dict = response['characters']

fname, lname, age = ([] for _ in range(3))

for character in char_dict:
    character['fname'] = character['name'].split(' ')[0]
    character['lname'] = character['name'].split(' ')[1]
    character['age'] = character['age'] + 10 if character['age'] < 40 else character['age']

    fname.append(character['fname'])
    lname.append(character['lname'])
    age.append(character['age'])
