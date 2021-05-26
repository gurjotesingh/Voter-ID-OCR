#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract")

def get_info(v):
    '''Input the file path for the image'''
    voter=pytesseract.image_to_string(Image.open(v))
    
    text1 = []

    lines = voter.split('\n')
    for lin in lines:
        s = lin.strip()
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)
    
    text1 = list(
        filter(None, text1))
    d={}
    name=None
    fname=None
    age=None
    for i in text1:
        if re.search(r"(Electors Name|Elector's Name|ELECTORS NAME|ELECTOR'S NAME|FATHER'S NAME|FATHERS NAME)",i):
            name=i.rsplit(': ',1)[1]
        if re.search(r"(Age|Date of Birth)",i):
            age=i.rsplit(': ',1)[1]
        if re.search(r"(Fathers Name|Father's Name)",i):
            fname=i.rsplit(': ',1)[1]
    d["Elector's Name: "]=name
    d["Age: "]=age
    d["Father's Name: "]=fname
    return d


# In[ ]:




