import requests

def download_report(download_url):
    response = requests.get(download_url)
    response.raise_for_status()
    return response.content