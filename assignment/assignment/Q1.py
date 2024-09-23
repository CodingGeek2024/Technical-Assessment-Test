import requests
from bs4 import BeautifulSoup

def scrape_cnn_articles():
    # URL of CNN's homepage
    url = "https://www.cnn.com"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article elements
        articles = soup.find_all('article', class_='card')
        
        # List to store article information
        article_info = []
        
        # Extract title and URL for each article
        for article in articles:
            title_element = article.find('span', class_='card-title__text')
            link_element = article.find('a', class_='card-content__link')
            
            if title_element and link_element:
                title = title_element.text.strip()
                url = 'https://www.cnn.com' + link_element['href']
                article_info.append({'title': title, 'url': url})
        
        return article_info
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Run the scraper and print the results
if __name__ == "__main__":
    articles = scrape_cnn_articles()
    if articles:
        for i, article in enumerate(articles, 1):
            print(f"{i}. Title: {article['title']}")
            print(f"   URL: {article['url']}")
            print()
