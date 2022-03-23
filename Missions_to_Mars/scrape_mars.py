from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def scrape():
    url = "https://redplanetscience.com/"

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA Mars News Scrape
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    latest_article = soup.select_one("div.list_text")
    news_title = latest_article.find('div', class_='content_title').text
    news_desc = latest_article.find('div', class_='article_teaser_body').text

    # Mars Featured Image Scrape
    mars_images_url = "https://spaceimages-mars.com/"
    browser.visit(mars_images_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find('img', class_='headerimage')
    source = results['src']
    featured_image_url = f'https://spaceimages-mars.com/{source}'

    # Mars Facts Scrape
    mars_facts_url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(mars_facts_url)
    facts_df = pd.DataFrame(tables[0])
    facts_df.rename(columns={0: 'Mars - Earth Comparison', 
                         1: 'Mars', 
                         2: 'Earth'}, inplace=True)

    # Mars Hemispheres Scrape
    browser.visit("https://marshemispheres.com/")
    html = browser.html
    soup = bs(html, 'html.parser')
    products = soup.body.find_all('div', class_='description')

    click_links = []
    products = soup.body.find_all('div', class_='description')
    for product in products:
        link_name = product.h3.text
        click_links.append(link_name)

    hemisphere_image_urls = []

    for x in range(0, len(click_links)):
        browser.links.find_by_partial_text(click_links[x]).click()
        
        html = browser.html
        soup = bs(html, 'html.parser')
        
        image = soup.find('img', class_='wide-image')['src']
        hemisphere = click_links[x][:-9]
        
        hemisphere_dict = {}
        hemisphere_dict['title'] = hemisphere
        hemisphere_dict['img_url'] = f'https://marshemispheres.com/{image}'
        hemisphere_image_urls.append(hemisphere_dict)
        
        browser.visit("https://marshemispheres.com/")

    browser.quit()

    return hemisphere_image_urls, featured_image_url, news_title, news_desc