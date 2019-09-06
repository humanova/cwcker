# 2019 Emir Erbasan (humanova)

import requests
import codecs


def check_cw_website(check_list):

    results = []
    i = 0
    for url in check_list:
        r = requests.get(url)

        curr_html = r.text
        prev_html = codecs.open(f"save/{i}.txt", "r", "utf-8").read()

        if not len(curr_html) == len(prev_html):
            change_text = f"Change detected @ `{url}`\n\nOld/New char count : {len(prev_html)} - {len(curr_html)}\nNew html :\n```{curr_html}```"
            codecs.open(f"save/{i}.txt", "w+", "utf-8").write(curr_html)

            results.append((True, change_text))

        change_text = f"There are no changes on the website. (`{url}`)"
        i += 1

        results.append((False, change_text))

    return results
