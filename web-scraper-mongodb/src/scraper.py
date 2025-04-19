
import nltk
nltk.download('punkt')

import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['web_scraper_db']
collection = db['scrape_results']

def scrape_and_summarize(url, num_sentences=5):
    # Store input URL
    result_doc = {'input_url': url}
    
    # Fetch the web page
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        error_msg = f"Error fetching the URL: {e}"
        print(error_msg)
        result_doc['error'] = error_msg
        collection.insert_one(result_doc)
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from all paragraphs
    paragraphs = soup.find_all('p')
    content = "\n".join([para.get_text() for para in paragraphs if para.get_text()])
    
    if not content:
        error_msg = "No text content found on the page."
        print(error_msg)
        result_doc['error'] = error_msg
        collection.insert_one(result_doc)
        return

    # Summarize the content using Sumy
    parser = PlaintextParser.from_string(content, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    # Get summary sentences
    summary = []
    print("\n--- Summary ---\n")
    for sentence in summarizer(parser.document, num_sentences):
        print(sentence)
        summary.append(str(sentence))
    
    # Store results in MongoDB
    result_doc.update({
        'original_content': content,
        'summary': summary
    })
    collection.insert_one(result_doc)

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_and_summarize(url, num_sentences=7)