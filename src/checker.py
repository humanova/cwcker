# 2019 Emir Erbasan (humanova)

import requests

def check_cw_website():
    r = requests.get("https://cubeworld.com")
    
    curr_html = r.text
    prev_html = open("website.txt", "r").read()

    if not len(curr_html) == len(prev_html):
        change_text = f"Change detected!\n\nOld/New char count : {len(prev_html)} - {len(curr_html)}\nNew html :\n```{curr_html}```"
        open("website.txt", "w+").write(curr_html)

        return (True, change_text)

    change_text = "There is no changes on the website."
    
    return (False, change_text)

