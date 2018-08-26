from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

my_url = 'https://www.ebay.com/sch/13704/i.html?_from=R40&_nkw=&Photo%2520Type=Ambrotype&LH_Complete=1&LH_Auction=1&_ipg=25&_pgn=1'

# browser = webdriver.Safari()
# browser.get(my_url)
# element = browser.find_element_by_tag_name('html')
# containers = browser.find_element_by_tag_name('li',{'class':'s-item'})
# print containers

# element.send_keys(Keys.END)
# time.sleep(8)
# element.send_keys(Keys.HOME)
# browser.close()


# opening connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

item_count = page_soup.findAll('h1',{'class':'srp-controls__count-heading'})
count_number = item_count[0].text

print count_number

# #grabs each product

containers = page_soup.findAll('li',{'class':'s-item'})

length = len(containers)

for i in range(0, 7):
    container = containers[i]
    listing1 = container.div.div.div.div.img['src']
    print 'first listing: %s' % listing1

for i in range(7, length):
    container = containers[i]
    listing2 = container.div.div.div.div.img['data-src']
    print 'next listing: %s' % listing2

# same results as above loops but in single function
def get_listings(start, stop, containers, tag):
    listings = []
    for i in range(start, stop):
        container = containers[i]
        single = container.div.div.div.div.img['tag']
        single.append[listing]
    return listings

get_listings(0, 7, containers, 'src')
get_listings(7, len(containers), containers, 'data-src')