import http.client
import json

def get_unsplash_images(search_query):
    conn = http.client.HTTPSConnection("api.unsplash.com")

    endpoint = f"/search/photos?query={search_query}"

    conn.request("GET", endpoint)

    response = conn.getresponse()
    data = response.read().decode()

    if response.status == 200:
        data = json.loads(data)
        image_urls = [result["urls"]["regular"] for result in data["results"]]
        return image_urls
    else:
        print(f"Failed to fetch images. Status code: {response.status}")
        return []
    
search_query = "New+York+City"  # Replace this with the desired search query

image_urls = get_unsplash_images(search_query)

if image_urls:
    for idx, url in enumerate(image_urls, 1):
        print(f"Image {idx}: {url}")
else:
    print("No images found.")