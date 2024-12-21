import requests
from platformdirs import user_cache_path

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
if not output_file.exists():
    download_file()
    print(f"File downloaded to: {output_file}")
