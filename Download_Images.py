def Download_Images(url, dir):
 ab = fake_Browser()
 ab.faked()
 page = ab.open(url)
 soup = BeautifulSoup(html, 'html.parser')
 images = soup.findAll('img')
