import requests
from bs4 import BeautifulSoup

def check_availability(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text()
    return "პრაიმი" in page_text

def check_location(location_name, urls):
    for flavor, url in urls.items():
        if check_availability(url):
            return f"{flavor} is available in {location_name}"
    return f"Not available in {location_name}"

def main():
    locations = {
        "Chitaia": {
            "Blue": "https://wolt.com/en/geo/tbilisi/venue/spar-chitaia/matonizirebeli-sasmeli-lurji-zholo-praimi-500ml-x-12ts-q-itemid-659e9983b3f05adb4ce27ac2",
            "Green": "https://wolt.com/en/geo/tbilisi/venue/spar-chitaia/matonizirebeli-sasmeli-tropikuli-punshi-praimi-500ml-x-12ts-q-itemid-65ae73bf6bba10da0a9deaac"
        },
        "Gldani": {
            "Blue": "https://wolt.com/en/geo/tbilisi/venue/spar-bochorishvili/matonizirebeli-sasmeli-lurji-zholo-praimi-500ml-x-12ts-q-itemid-65ae71e80034b8a119ec83ab"
        },
        "Kostava": {
            "Green": "https://wolt.com/en/geo/tbilisi/venue/spar-kostava/matonizirebeli-sasmeli-tropikuli-punshi-praimi-500ml-x-12ts-q-itemid-65ae73b5b5a7884c21ca4d10",
            "Paraguay": "https://wolt.com/en/geo/tbilisi/venue/spar-kostava/matonizirebeli-sasmeli-ice-pop-praimi-500ml-x-12ts-q-itemid-65ae73b5b5a7884c21ca4d11"
        },
        "Avlabari": {
            "Green": "https://wolt.com/en/geo/tbilisi/venue/spar-irbakhi/matonizirebeli-sasmeli-tropikuli-punshi-praimi-500ml-x-12ts-q-itemid-65ae73c1b5a7884c21ca890b"
        },
        "Mukhiani": {
            "Paraguay": "https://wolt.com/en/geo/tbilisi/venue/spar-mukhiani/matonizirebeli-sasmeli-ice-pop-praimi-500ml-x-12ts-q-itemid-65ae73bfb5a7884c21ca7d0d"  
        },
        "Kipshidze": {
            "Green": "https://wolt.com/en/geo/tbilisi/venue/spar-kipshidze/matonizirebeli-sasmeli-tropikuli-punshi-praimi-500ml-x-12ts-q-itemid-65ae73b83c8d38a00812d80b",
            "Paraguay": "https://wolt.com/en/geo/tbilisi/venue/spar-kipshidze/matonizirebeli-sasmeli-ice-pop-praimi-500ml-x-12ts-q-itemid-65ae73b83c8d38a00812d80c"
        },
        "Isani": {
            "Green": "https://wolt.com/en/geo/tbilisi/venue/spar-isani/matonizirebeli-sasmeli-tropikuli-punshi-praimi-500ml-x-12ts-q-itemid-65ae73ba3c8d38a00812e40a"
        },
        "Vazha-Pshavela": {
            "Blue": "https://wolt.com/en/geo/tbilisi/venue/spar-vazhapshavela/matonizirebeli-sasmeli-lurji-zholo-praimi-500ml-x-12ts-q-itemid-65ae73bc6bba10da0a9ddeac"
        }
    }
    
    for location_name, location_urls in locations.items():
        print(check_location(location_name, location_urls))

main()
