import json
from typing import List

with open("content_test.json", "r") as f:
    # urls: List[dict] = json.load(f)
    urls: str = f.read()


def get_id(link: str):
    # needs urls: List[dict] ??? i think
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


def change_content():

    for idxl in range(len(lines:=urls.splitlines())):
        if lines[idxl].lstrip().startswith("\"content"):
            # print(lines[idxl][:30], "...", lines[idxl][-20:])
            replaced = lines[idxl].replace("\": \"", "\": `").replace(">\",", ">`,")
            print(replaced[:30], "...", replaced[-20:])
            lines[idxl] = replaced

    with open("content_test.txt", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    # get_id(urls)
    change_content()
    # with open("content.txt", "w") as f:
    #     json.dump(urls, f, indent=4)
