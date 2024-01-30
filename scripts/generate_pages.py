import json

with open("content.json", "r") as f:
    urls: list[dict] = json.load(f)


def get_id(link: str):
    SEPERATORS = ["part", "chapter", "front-matter", "back-matter"]

    for page in urls:
        for sep in SEPERATORS:
            if sep in page["link"]:
                page["id"] = page["link"].split(sep)[-1].strip("/")
                break

    if "chapters" in page.keys():
        for chapter in page["chapters"]:
            for sep in SEPERATORS:
                if sep in chapter["link"]:
                    chapter["id"] = chapter["link"].split(sep)[-1].strip("/")
                    break




with open("content.json", "w") as f:
    json.dump(urls, f, indent=4)
