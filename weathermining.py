import requests
import time

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# The URL of the website you want to fetch
url = [
    #Wetter.com
    ["wetter_com","str_hourly", "https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/deutschland/leinfelden/flughafen-stuttgart-str/DE0010287023.html"],
    ["wetter_com","str_days", "https://www.wetter.com/brasilien/deutschland/leinfelden/flughafen-stuttgart-str/DE0010287023.html"],
    ["wetter_com","man_hourly", "https://www.wetter.com/brasilien/manaus/BRXY00004.html"],
    ["wetter_com","man_days", "https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/brasilien/manaus/BRXY00004.html"],
    ["wetter_com","jun_hourly", "https://www.wetter.com/vereinigte-staaten/juneau/US5554072.html"],
    ["wetter_com","jun_days", "https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/vereinigte-staaten/juneau/US5554072.html"],
    
    #Weather.com
    ["weather_com","str_days", "https://weather.com/de-DE/wetter/10tage/l/cf8b97bb5f7948879445bf57fb4e94e4b73f3bc37c16f2596f5cef257021af11"],
    ["weather_com","str_hourly", "https://weather.com/de-DE/wetter/stundlich/l/cf8b97bb5f7948879445bf57fb4e94e4b73f3bc37c16f2596f5cef257021af11"],
    ["weather_com","man_hourly", "https://weather.com/de-DE/wetter/stundlich/l/33d99f263f7578a2e6008f2093fec568d0e3ede655b252fcc66574642c8bcda1"],
    ["weather_com","man_days", "https://weather.com/de-DE/wetter/10tage/l/33d99f263f7578a2e6008f2093fec568d0e3ede655b252fcc66574642c8bcda1"],
    ["weather_com","jun_days", "https://weather.com/de-DE/wetter/10tage/l/bc6c6d8f7cfb302a9347c9936e52c2118b582c1b2c177cae22673d9f9853f4e0"],
    ["weather_com","jun_hourly", "https://weather.com/de-DE/wetter/stundlich/l/bc6c6d8f7cfb302a9347c9936e52c2118b582c1b2c177cae22673d9f9853f4e0"],
    
    #Wetteronline.de
    ["accuweather_com","str_hourly", "https://www.accuweather.com/en/de/stuttgart-airport/70794/hourly-weather-forecast/2683_poi"],
    ["accuweather_com","jun_hourly", "https://www.accuweather.com/en/us/juneau/99801/hourly-weather-forecast/331728"],
    ["accuweather_com","man_hourly", "https://www.accuweather.com/en/br/manaus/42471/hourly-weather-forecast/42471"],
    ["accuweather_com","str_days", "https://www.accuweather.com/en/de/stuttgart-airport/70794/daily-weather-forecast/2683_poi"],
    ["accuweather_com","jun_days", "https://www.accuweather.com/en/us/juneau/99801/daily-weather-forecast/331728"],
    ["accuweather_com","man_days", "https://www.accuweather.com/en/br/manaus/42471/daily-weather-forecast/42471"]
    ]

# Directory where you want to save the website content
save_directory = "./"

def fetch_and_save_website(url, save_directory, website, namecode):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            # Construct a unique filename based on the current timestamp
            current_time = time.strftime("%Y%m%d%H%M%S")
            filename = f"{current_time}_{website}_{namecode}.html"

            # Save the website content to a file
            with open(f"{save_directory}/{filename}", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Website saved to {filename}")
        else:
            print(f"Failed to fetch website. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        for site in url:
            fetch_and_save_website(site[2], save_directory, site[1], site[0])
        print("download done")
        time.sleep(43180)  # Sleep for 12 hours minus 20 seconds
