import requests

# Define the URL you want to access
url = "https://www.olx.com.pk"

# Define headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.olx.com.pk/sindh_g2003007/mobiles_c1411',
    'Cache-Control': 'max-age=0',
}

# Make the GET request with headers
try:
    response = requests.get(url, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        print("Access successful!")
        print(headers)  # Print the first 500 characters of the response content
    else:
        print(f"Access failed. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
