#!/usr/bin/env python

import re

html_doc = '''
870 Brock Road South
Pickering, Ontario
Canada
L1W 1Z8
+086-18603029402
Toll Free: 1.800.465.7051
Local: 905.839.1138
Fax: 905.839.9108
Fx: 887-2236670,23366810
0755-86381920
mobile:13528762177
668-8910-7731
HubbellInfo@hubbell.ca
call me:(800)321-2547
(400)-65512123
tell(899)14223565
89860619050018936103
'''

'''
def find_email(text):
    regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
    mails = re.findall(regex, text)
    return mails
'''

def find_phone(text):
    # "^($$\d{3,4}-)|\d{3.4}-)?\d{7,8}$"
    regex = re.compile(r"[(\+\d+)\+.-]+\d{3,8}\b", re.IGNORECASE)
    phones = re.findall(regex, text)
    return phones

def init():
    data = find_phone(html_doc)
    print(data)

if __name__ == "__main__":
    init()