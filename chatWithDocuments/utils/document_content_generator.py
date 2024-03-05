from typing import Any

import requests
import json
#from PyPDF2 import PdfReader

def get_api_response_content():
    # Base URL of your Confluence instance
    base_url = " https://randomuser.me/api/"

    # API endpoint to get content of a page
    api_endpoint = "https://baconipsum.com/api/?type=all-meat&paras=1"

    # Headers with basic authentication
    headers = {
        "Content-Type": "text/html"
    }


    # Make GET request to random API
    response = requests.get(api_endpoint, headers=headers)
    print(response)

    # Check if request was successful
    if response.status_code == 200:
            # Get the raw content from the JSON response
            #content_json = response.json()
            return response.text

#def get_pdf_text(pdf_docs):
 #   text = ""
 #   for pdf in pdf_docs:
 #       pdf_reader = PdfReader(pdf)
 #       for page in pdf_reader.pages:
 #           text += page.extract_text()
 #   return text



