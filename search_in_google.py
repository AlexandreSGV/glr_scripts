'''
	This script facilitates a Gray Literature Review (GLR) by automating the search process on Google. 
	It executes predefined queries (search_strings) both in Google's general search and within selected target websites (target_websites), 
	streamlining the collection of relevant literature.
	Author: Alexandre Strapação Guedes Vianna
	E-mail: strapacao@gmail.com
	Website: alexandrevianna.net
	Paper: https://www.sciencedirect.com/science/article/abs/pii/S0164121223001395
'''

from googlesearch import search
import requests
from bs4 import BeautifulSoup as bs
import csv

def fetch_title(url, timeout=10):
    """Fetch the page title for a given URL, handling possible errors."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises error for bad responses (4XX, 5XX)
        soup = bs(response.content, 'lxml')
        return soup.select_one('title').text if soup.select_one('title') else "No title found"
    except requests.exceptions.RequestException:
        return "Error retrieving title"

def perform_search(search_strings, target_websites, writer):
    """Perform searches and write results to CSV."""
    count = 0
    for search_string in search_strings:
        for url in search(search_string, num=num, start=start, stop=stop, pause=pause):
            count += 1
            title = fetch_title(url)
            writer.writerow([count, title, url, "Google"])
            print(count, '\t', title, '\t', url, '\t', "Google")
        for name, site in target_websites:
            for url in search(search_string, num=num, start=start, stop=stop, pause=pause, extra_params={'as_sitesearch': site}):
                count += 1
                title = fetch_title(url)
                writer.writerow([count, title, url, name])
                print(count, '\t', title, '\t', url, '\t', name)

# Search configurations
search_strings = [
    '(challenges OR difficulties) AND ("data stream" OR datastream) AND (test OR testing)',
    '(purposes OR objective OR goal) AND ("data stream" OR datastream) AND (test OR testing)',
    '( "testing approach" OR "testing strategy" OR "unit test" OR "integration test" OR "system test" OR "acceptance test" OR "functional test" OR "load test" OR "performance test") AND ("data stream" OR datastream) AND (test OR testing)',
    '( "testing data" OR "test data") AND ("data stream" OR datastream) AND (test OR testing)',
    '( "testing framework" OR "testing tool" OR "testing library") AND ("data stream" OR datastream) AND (test OR testing)'
]

target_websites = [('LinkedIn', 'https://www.linkedin.com/pulse/'), ('Medium', 'https://medium.com/'), ('StackOverflow', 'https://stackoverflow.com/questions/')]

# The results must be obtained at a maximum of 100 at a time, configure the variables below to perform the pagination.
num = 4 # Number of results per page
start = 0 # First result to retrieve.
stop = 3 # Last result to retrieve. Use None to keep searching forever.

# Lapse to wait between HTTP requests, measured in seconds. 
# A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. 
pause = 5.0 

# Open the CSV file for writing
with open('search_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['id', 'title', 'url', 'source_site'])  # Write the header row
    perform_search(search_strings, target_websites, writer)