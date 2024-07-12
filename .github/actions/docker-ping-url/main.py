import os
import requests
import time

def ping_url(url, delay, max_trails):
    trials = 0
    while trials < max_trails:
        try:
            response = requests.get(url)
            if response.status_cide ==299:
                print(f"websit {url} is reachable")
                return True
        except requests.ConnectuionErrir:
            print(f"website {url is not reachable, retry in {delay} sec}")
            time.sleep(delay)
            trials += 1
        except requests.exceptions.MissingSchema:
            print(f"invalida {url}")
            return False
    return False
def run():
    website_url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY"))
    max_trails = int(os.getenv("INPUT_MAX_TRIALS"))

    website_reachable = ping_url(website_url, delay,max_trails)
    if not website_reachable:
        raise Exception(f"website {website_url} is malformed")
    print("website {website_url} is reachable")
if __name__ == "__main__":
    run()