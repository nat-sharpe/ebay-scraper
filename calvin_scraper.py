
# Importing libraries for use in the project
from __future__ import print_function
from bs4 import BeautifulSoup
import requests

unique_listings = {
    "https://i.ebayimg.com/thumbs/images/g/FDAAAOSw0F9bntMB/s-l225.jpg" : {'title': '1/6 Plate Ambrotype In Case Cross—eyed Woman', 'listingURL': 'https://www.ebay.com/itm/1-6-Plate-Ambrotype-In-Case-Cross-eyed-Woman/202439561494?hash=item2f22569116:g:FDAAAOSw0F9bntMB', 'imgURL': 'https://i.ebayimg.com/thumbs/images/g/FDAAAOSw0F9bntMB/s-l225.jpg', 'price': '$49.95'},
    'https://i.ebayimg.com/thumbs/images/g/OOwAAOSwWxNYzs7m/s-l225.jpg' : {'title': 'Antique Ambrotype Photo, Gentleman', 'listingURL': 'https://www.ebay.com/itm/Antique-Ambrotype-Photo-Gentleman/332808350434?hash=item4d7cec6ae2:g:OOwAAOSwWxNYzs7m', 'imgURL': 'https://i.ebayimg.com/thumbs/images/g/OOwAAOSwWxNYzs7m/s-l225.jpg', 'price': '$60.00'}
}

def write_page():
    request = "https://www.ebay.com/b/Ambrotypes/13704?LH_Auction=1&Photo%2520Type=Ambrotype&rt=nc&_from=R40&_ipg=25&_nkw=&_pgn=1&_sop=10"

    # Scrape the images from the DOM
    print("Scraping images... ", end="")
    response = requests.get(request)
    soup = BeautifulSoup(response.text, "html.parser")

    containers = soup.findAll('li',{'class':'s-item'})

    def get_listings(start, stop, containers, tag):
        all_fresh = []
        for i in range(start, stop):
            container = containers[i]
            key = str(container.div.div.div.div.img[tag])
            if key not in unique_listings:
                single_fresh = {}
                single_fresh["title"] = str(container.div.div.div.div.img['alt'])
                single_fresh["listingURL"] = str(container.div.div.a['href'])
                single_fresh["imgURL"] = key
                single_fresh["price"] = str(container.div.find("div", {"class" : "s-item__info clearfix"}).find("div", {"class" : "s-item__details clearfix"}).div.span)

                all_fresh.append(single_fresh)
                unique_listings[key] = single_fresh

        return all_fresh

    list1 = get_listings(0, 7, containers, "src")
    list2 = get_listings(7, len(containers), containers, "data-src")

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
    f = open("index.html", "w")
    # # Write the book title here
    # f.write(str(title))
    # # Write the picture here
    # f.write(picture_link)
    # Write the reviews
    for listing in list1:
        # f.write('<img src="' + str(listing) + '"/>')
        f.write(str(listing))
        f.write("<br/>")
    for listing in list2:
        f.write(str(listing))
        f.write("<br/>")
    
    f.close()
    print("done")

write_page()