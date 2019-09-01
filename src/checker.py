# 2019 Emir Erbasan (humanova)

import requests
import codecs

def check_cw_website():
    r = requests.get("https://cubeworld.com")
    
    curr_html = r.text
    prev_html = codecs.open("website.txt", "r", "utf-8").read()

    if not len(curr_html) == len(prev_html):
        change_text = f"Change detected!\n\nOld/New char count : {len(prev_html)} - {len(curr_html)}\nNew html :\n```{curr_html}```"
        codecs.open("website.txt", "w+", "utf-8").write(curr_html)

        return (True, change_text)

    change_text = "There is no changes on the website."
    
    return (False, change_text)

