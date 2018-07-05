from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.ebay.com/sch/13704/i.html?_from=R40&_nkw=&Photo%2520Type=Ambrotype&LH_Complete=1&LH_Auction=1&_ipg=25&_pgn=1'

# opening connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

#grabs each product
containers = page_soup.findAll('li',{'class':'s-item'})

for container in containers:
    listing = container.div.div.div.div.img['src']
    print 'Unique listing: %s' % listing