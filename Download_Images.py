def Download_Images(url, dir):
 ab = fake_Browser()
 ab.faked()
 page = ab.open(url)
 soup = BeautifulSoup(html, 'html.parser')
 images = soup.findAll('img')
 
 for image in images:
  img_file = image['src'].lstrip('http://')
  img_file = os.path.join(dir,\
  img_file.replace('/', '_'))
  print ('[+] Saving ' + str(filename))
  data = ab.open(image['src']).read()
  ab.back()
  save = open(filename, 'wb')
  save.write(data)
  save.close()
