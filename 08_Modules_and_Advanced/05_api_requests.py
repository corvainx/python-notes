# Lesson 05: HTTP Networking and REST API Consumption (requests / urllib)
import json
import urllib.request
import urllib.error

def fetch_pokemon(pokemon_name: str):
    """Fetches real-time REST API data using standard library urllib."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}"
    print(f"Requesting data from: {url}")

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "PythonJournalClient/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                raw_data = response.read().decode("utf-8")
                data = json.loads(raw_data)

                name = data.get("name").capitalize()
                height = data.get("height")
                weight = data.get("weight")
                types = [t["type"]["name"] for t in data.get("types", [])]

                print(f"\n--- Pokemon Card: {name} ---")
                print(f"  Height: {height} | Weight: {weight}")
                print(f"  Types: {', '.join(types)}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: Status {e.code} ({e.reason})")
    except urllib.error.URLError as e:
        print(f"Network Error: Connection failed ({e.reason})")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    fetch_pokemon("pikachu")
