
# Importing libraries for use in the project
from __future__ import print_function
from bs4 import BeautifulSoup
import requests

def printPage():
    request = "https://www.ebay.com/b/Ambrotypes/13704?LH_Auction=1&Photo%2520Type=Ambrotype&rt=nc&_from=R40&_ipg=25&_nkw=&_pgn=1&_sop=10"
    # Scrape the images from the DOM
    print("Scraping images... ", end="")
    response = requests.get(request)
    soup = BeautifulSoup(response.text, "html.parser")

    containers = soup.findAll('li',{'class':'s-item'})

    length = len(containers)

    def get_listings(start, stop, containers, tag):
        listings = []
        for i in range(start, stop):
            container = containers[i]
            single = container.div.div.div.div.img[tag]
            listings.append(single)
        return listings

    list1 = get_listings(0, 7, containers, 'src')
    list2 = get_listings(7, len(containers), containers, 'data-src')

    # target_divs = soup.find_all("div", {"class": "enrichedContentElement"})
    # # Scrape the title from the DOM
    # title = soup.find("div", {"class": "displayElementText INITIAL_TITLE_SRCH"})
    # # Scrape the picture from the DOM
    # picture_link = soup.find("img", {"id": "detailCover0"})
    # # removing garbage from the image link (might not be consistent)
    # picture_link = str(picture_link).replace("amp;", "")        
    # # Get the reviews
    # review_list = []
    # for div in target_divs:
    #     # Only get items with "Review" in the header
    #     if "Review</h3>" in str(div):
    #         review_list.append(str(div))
    # print("done")
    # Write the HTML!
    print("Generating HTML file... ", end="")
    f = open("review.html", "w")
    # # Write the book title here
    # f.write(str(title))
    # # Write the picture here
    # f.write(picture_link)
    # Write the reviews
    for listing in list1:
        f.write('<img src="' + str(listing) + '"/>')
        f.write(str(listing))
        f.write("<br/>")
    for listing in list2:
        f.write(str(listing))
        f.write("<br/>")
    
    f.close()
    print("done")

printPage()