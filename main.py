import requests
import streamlit as st
import swisseph as swe
from datetime import datetime
from platformdirs import user_cache_path
from zoneinfo import ZoneInfo

dt = datetime.now()
local_tz = ZoneInfo("Asia/Taipei")
local_dt = dt.replace(tzinfo=local_tz)
utc_dt = local_dt.astimezone(ZoneInfo("UTC"))
julian_day = swe.date_conversion(
    utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60
)[1]

bodies = [
    swe.SUN,
    swe.MOON,
    swe.MERCURY,
    swe.VENUS,
    swe.MARS,
    swe.JUPITER,
    swe.SATURN,
    swe.URANUS,
    swe.NEPTUNE,
    swe.PLUTO,
    swe.MEAN_NODE,
    swe.CHIRON,
    swe.PHOLUS,
    swe.CERES,
    swe.PALLAS,
    swe.JUNO,
    swe.VESTA,
]

# Get cache directory for the app
cache_dir = user_cache_path("swe")
cache_dir.mkdir(parents=True, exist_ok=True)
output_file = cache_dir / "seas_18.se1"

# URL of the file
url = "https://github.com/hoishing/natal/raw/refs/heads/main/natal/data/seas_18.se1"


# Download and save the file
def download_file():
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    output_file.write_bytes(response.content)
    return output_file


# Execute download
file_path = download_file()

swe.set_ephe_path(str(file_path.parent))

for body in bodies:
    try:
        ((lon, _, _, speed, *_), _) = swe.calc_ut(julian_day, body)
        st.write(body, lon, speed)
    except Exception as e:
        st.write(body, e)


st.write(f"File downloaded to: {file_path}")
