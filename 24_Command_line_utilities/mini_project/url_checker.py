import argparse
import requests

def check_url_status(url):
    try:
        response = requests.head(url)
        print(f"✅ {url} is reachable. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ {url} is not reachable. Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the status of a URL")
    parser.add_argument("url", help="The URL to check")
    args = parser.parse_args()

    check_url_status(args.url)
