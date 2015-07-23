import urllib2
import string
from bs4 import BeautifulSoup 

def alphanumeric_list():
   list = []
   for n in range(48, 58):
      list.append(chr(n))
   for a in range(97, 123):
      list.append(chr(a))
   for A in range(65, 91):
      list.append(chr(A))

   return list

ALPHA_NUM = alphanumeric_list()

def get_url(key):
   return "http://www.donotlink.com/"+key

def get_title(url):
   try:
      return BeautifulSoup(urllib2.urlopen(url)).title.string
   except:
      return None

def get_website_name(title):
   words = title.split(' ')
   for word in words:
      if "." in word:
         return word

def convert(number):
   fromdigits = "0123456789"
   todigits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

   if str(number)[0]=='-':
      number = str(number)[1:]
      neg=1
   else:
      neg=0

   x=long(0)

   for digit in str(number):
      x = x*len(fromdigits) + fromdigits.index(digit)
   
   res=""
   while x>0:
      digit = x % len(todigits)
   if neg:
      res = "-"+res
   return res
   
def get_website_from_key(key):
   url = get_url(key)
   title = get_title(url)
   if title is not None:
      website = get_website_name(title)
      return website
   else:
      return "!"

def get_all():
   key = 0
   while True:
      key += 1
      c_key = convert(key)
      print(c_key+", "+get_website_from_key(c_key))

get_all()
