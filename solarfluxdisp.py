import time
import requests
from bs4 import BeautifulSoup

print("Program to read and display the solar flux value from www.spaceweather.gc.ca")

url = "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-4-en.php"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

start = time.perf_counter()

try:
    with requests.Session() as session:
        # (connect_timeout, read_timeout) in seconds
        response = session.get(url, headers=headers, timeout=(5, 10))
        response.raise_for_status()
except requests.Timeout:
    print(f"Timed out after {time.perf_counter() - start:.2f}s while contacting the server.")
    raise SystemExit(1)
except requests.RequestException as exc:
    print(f"Failed to retrieve the webpage ({time.perf_counter() - start:.2f}s): {exc}")
    raise SystemExit(1)

soup = BeautifulSoup(response.content, "html.parser")

content_section = soup.find(
    string=lambda text: text and "Flux Density Values in sfu" in text
)

date, time_str = "Date not found", "Time not found"
if content_section and "for" in content_section:
    date_time_info = content_section.split("for", 1)[1].strip()
    if "at" in date_time_info:
        raw_date, raw_time = date_time_info.split("at", 1)
        date = raw_date.strip()
        time_str = raw_time.strip()
    else:
        date = date_time_info

flux_label = soup.find(string=lambda text: text and "Observed Flux Density" in text)
flux_target = flux_label.find_next() if flux_label else None
if flux_target and flux_target.string:
    observed_flux_density = flux_target.string.strip()
elif flux_target:
    observed_flux_density = flux_target.get_text(strip=True)
else:
    observed_flux_density = "Flux Density not found"

elapsed = time.perf_counter() - start
print(f"Date: {date}\nTime: {time_str}\nObserved Flux Density: {observed_flux_density} sfu")
print(f"(Completed in {elapsed:.2f}s)")