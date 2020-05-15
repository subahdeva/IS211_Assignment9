#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib2
from bs4 import BeautifulSoup
import soupsieve
import ssl
context = ssl._create_unverified_context()
html = urllib2.urlopen("https://www.nasdaq.com/symbol/aapl/historical", context=context)
bsObj = BeautifulSoup(html)

stock_data = bsObj.findAll('tr')

def main():
    print "Apple Inc. (AAPL) Daily Closing Prices:"
    for i in stock_data:
        t_data = i.findAll('td', {"class":"yfnc_tabledata1"})
        if len(t_data) is 7:
            date = t_data[0].contents[0]
            close = t_data[6].contents[0]
            print ("Date: {}, Closing Price: {}").format(date, close)

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




