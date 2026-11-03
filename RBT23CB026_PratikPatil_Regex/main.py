"""
Design and implement regular expressions to identify patterns such as email IDs , phone numbers , dates , and named entities from a text.
Simulate a finite state automaton (FSA) fr simple word recognition tasks.
"""

import re

text = """
Contact : Pratik at patil@gmail.com
Phone : 8788748590
Date : 03/11/2026
Entities : Google
"""

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
print("Emails :", emails)

phone = re.findall(r'\b\d{10}\b', text)
print("Phone No :", phone)

dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print("Dates:", dates)

entities = re.findall(r'\b[A-Z][a-z]+\b', text)
print("Entities:", entities)


def fsa(word):
    state = 0

    transitions = {
        (0, 'c'): 1,
        (1, 'a'): 2,
        (2, 't'): 3
    }

    for ch in word.lower():
        state = transitions.get((state, ch), -1)

        if state == -1:
            return False

    return state == 3


for word in ["cat", "ca", "bat", "car"]:
    print(word, "Accepted" if fsa(word) else "Rejected")
    
    
    
    
 """
 Output:
 
 osl@osl-OptiPlex-3090:~$ python RBT23CB026_NLP_Practical.py 
Emails: ['patil@gmail.com']
Phone No: ['8788748590']
Dates: ['03/11/2026']
Entities: ['Contact', 'Pratik', 'Phone', 'Date', 'Entities', 'Google']
cat Accepted
ca Rejected
bat Rejected
car Rejected
osl@osl-OptiPlex-3090:~$ 

 """

