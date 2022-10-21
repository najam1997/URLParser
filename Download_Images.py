def Download_Images(url, dir):
 ab = fake_Browser()
 ab.faked()
 page = ab.open(url)
 soup = BeautifulSoup(html, 'html.parser')
 images = soup.findAll('img')
 
 for image in images:
  img_file = image['src'].lstrip('/')
  img_file = os.path.join(dir, img_file.replace('/', '_'))
  print ('Saving ' + str(filename))
  data = ab.open(image['src']).read()
  ab.back()
  save = open(img_file, 'ab')
  save.write(data)
  save.close()

def main():
 parser = optparse.OptionParser()
 parser.add_option("-u", "--url",
                  dest = "url",
                  help = "-u http://example.com")
 parser.add_option("-d", "--directory",
                  dest = "directory",
                  help = "-d /tmp/")
 (options, args) = parser.parse_args()
 url = options.url
 directory = options.directory
 if url == None or dir == None:
  print (parser.usage)
  exit(0)
 else:
  try:
    Download_Images(url, directory)
  except (Exception, e):
   print ('Error Downloadimg Images.')
   print (str(e))
  
if __name__ == '__main__':
 main()
