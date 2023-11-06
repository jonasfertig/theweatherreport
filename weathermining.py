import requests
import time

# The URL of the website you want to fetch
url = ["https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/deutschland/leinfelden/flughafen-stuttgart-str/DE0010287023.html",
       "https://www.wetter.de/wetter/n/3221999879",
       "https://www.wetteronline.de/wetter/stuttgart",
       "https://www.agrarheute.com/wetter/deutschland/baden-wuerttemberg/stuttgart-flughafen-70629",
       "https://www.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/deutschland/leinfelden/flughafen-stuttgart-str/DE0010287023.html",
       "https://www.dwd.de/EN/weather/weather_climate_local/baden-wuerttemberg/stuttgart/_node.html",
       "https://www.accuweather.com/en/de/stuttgart-airport/70794/daily-weather-forecast/2683_poi",
       "https://weather.com/de-DE/wetter/10tage/l/cf8b97bb5f7948879445bf57fb4e94e4b73f3bc37c16f2596f5cef257021af11",
       "https://weather.com/de-DE/wetter/stundlich/l/cf8b97bb5f7948879445bf57fb4e94e4b73f3bc37c16f2596f5cef257021af11"
    ]

# Directory where you want to save the website content
save_directory = "./"

def fetch_and_save_website(url, save_directory):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)

        if response.status_code == 200:
            # Construct a unique filename based on the current timestamp
            current_time = time.strftime("%Y%m%d%H%M%S")
            filename = f"{current_time}_website.html"

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
            fetch_and_save_website(site, save_directory)
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
