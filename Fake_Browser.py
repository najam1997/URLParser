import mechanize, http.cookiejar, random

class fake_Browser(mechanize.Browser):
 
 def __init__(self, user_agents = []):
  mechanize.Browser.__init__(self)
  self.set_handle_robots(False)
  self.user_agents = user_agents + ['Mozilla/5.0 ',\
  'FireFox/41.0','Gecko/20100101', 'Safari/537.36']
  self.cookie_jar = http.cookiejar.LWPCookieJar()
  self.set_cookiejar(self.cookie_jar)
  self.anonymize()
 
 def clean_cookies(self):
  self.cookie_jar = http.cookiejar.LWPCookieJar()
  self.set_cookiejar(self.cookie_jar)
 
 def fake_user_agent(self):
  index = random.randrange(0, len(self.user_agents))
  self.addheaders = [('User-agent', \
  (self.user_agents[index]))]
 
 def faked(self, sleep = False):
  self.clean_cookies()
  self.fake_user_agent()
  if sleep:
   time.sleep(60)
