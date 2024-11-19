import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_search(query , num_results=10):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; ×64) AppleWebKit/537.36 (KHTML, 11ke Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    params= {
        "q":query,
        "num":num_results

    }

    response = requests.get(base_url,headers=headers , params=params)

    if response.status_code!=200:
        print("failed to retrive result")
        return[]
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for result in soup.select ('.tF2Cxc'):
        title = result.select_one('h3')
        link = result.select_one('a')
        descriptions = result.select_one('.VwiC3b')

        if title and link and descriptions:
            result.append(
                {
                    "title": title.get_text(),
                    "link":link["href"],
                    "description": descriptions.get_text()
                }
            )
            if not results:
                print("no results found")
            return results
        print("enter the query")

        query = input()
        results = google_search (query,num_results=10)

        for idx, results in enumerate(results , start =1 ):
            print(f"{idx}.{result['title']}")
            print(f" Link:{result['Link']}")
            print(f"Description: {result['title']}")