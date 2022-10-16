from fake_browser import *
from bs4 import BeautifulSoup
import os
import optparse
import re

def printLinks(url):
 ab = fake_browser()
 ab.faked()
 page = ab.open(url)
 html = page.read()
 
 try:
  print ('List of links using Regex.')
  reg = re.compile('href="(.*?)"')
  links = reg.findall(html)
  for link in links:
   print (link)
 except:
  pass
 try:
  print ('\n List of links using BeautifulSoup.')
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.findAll(name = 'a')
  for link in links:
   if link.has_key('href'):
    print (link['href'])
 except:
  pass

def main():
 parser = optparse.OptionParser()
 parser.add_option('-u', dest='URL', type='string')
 (options, args) = parser.parse_args()
 url = options.URL
 if url == None:
  print ("Retry")
  exit(0)
 else:
  printLinks(url)

if __name__ == '__main__':
 main()
