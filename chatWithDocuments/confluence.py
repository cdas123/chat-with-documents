import requests


def get_confluence_page_content():
    # Base URL of your Confluence instance
    base_url = " https://randomuser.me/api/"

    # API endpoint to get content of a page
    api_endpoint = "https://baconipsum.com/api/?type=all-meat&paras=1"

    # Headers with basic authentication
    headers = {
        "Content-Type": "text/html"
    }

    # Add basic authentication
    #auth = (username, api_token)

    try:
        # Make GET request to Confluence API
        print(api_endpoint)
        print(requests.get(api_endpoint).headers)

        response = requests.get(api_endpoint, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            # Get the raw content from the JSON response
            content_json = response.json()
            return content_json
        else:
            # Print error message if request fails
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Print any exceptions that occur
        print(f"An error occurred: {str(e)}")
        return None


if __name__ == "__main__":

    content = get_confluence_page_content()

    if content:
        print("Raw Content:")
        print(content)

