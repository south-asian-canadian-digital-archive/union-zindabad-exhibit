import json
from bs4 import BeautifulSoup

import requests


def get_content():
    with open("urls.json", "r") as f:
        urls: list[dict] = json.load(f)

    for page in urls:

        html = requests.get(page["link"])
        soup = BeautifulSoup(html.text, "html.parser")

        page["content"] = str(soup.find("div", {"id": "content"}))

        if "chapters" in page.keys():
            for chapter in page["chapters"]:
                html = requests.get(chapter["link"])
                soup = BeautifulSoup(html.text, "html.parser")

                chapter["content"] = str(soup.find("div", {"id": "content"}))

    with open("content.json", "w") as f:
        json.dump(urls, f, indent=4)


def get_images():
    with open("content.json", "r") as f:
        urls: list[dict] = json.load(f)

    for page in urls:
        if "content" in page.keys():
            soup = BeautifulSoup(page["content"], "html.parser")
            images = soup.find_all("img")
            for i, img in enumerate(images):
                print(f"Downloading {page['name']} image {i}...")
                img_url = img["src"]
                img_name = f"{page['id']}_img_{i}.jpg"
                img_data = requests.get(img_url).content
                with open(f"images/{img_name}", "wb") as handler:
                    handler.write(img_data)
                img["src"] = f"../images/{img_name}"

                img["srcset"] = ""

            page["content"] = str(soup)

        if "chapters" in page.keys():
            for chapter in page["chapters"]:
                soup = BeautifulSoup(chapter["content"], "html.parser")
                images = soup.find_all("img")
                for i, img in enumerate(images):
                    print(f"Downloading {page['name']} {chapter['name']} image {i}...")
                    img_url = img["src"]
                    img_name = f"{page['id']}_{chapter['id']}_img_{i}.jpg"
                    img_data = requests.get(img_url).content
                    with open(f"images/{img_name}", "wb") as handler:
                        handler.write(img_data)
                    img["src"] = f"../images/{img_name}"
                    img["srcset"] = ""
                chapter["content"] = str(soup)

    with open("content_img.json", "w") as f:
        json.dump(urls, f, indent=4)


def get_slugs():
    final = []
    with open("content.json", "r") as file:
        data = json.load(file)
        for i in data:
            print(json.dumps({"id": i["id"]}, indent=4))
            final.append({"id": i["id"]})
            if "chapters" in i.keys():
                for j in i["chapters"]:
                    print(json.dumps({"id": j["id"]}, indent=4))
                    final.append({"id": j["id"]})
    with open("slugs.json", "w") as file:
        json.dump(final, file, indent=4)


if __name__ == "__main__":
    # get_images()
    get_slugs()
