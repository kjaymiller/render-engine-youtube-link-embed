import typing
import re
from urllib.parse import urlsplit

import logging
import itertools


def extract_youtube_id(url: str) -> str:
    """
    Extract the video id from a youtube url
    """

    # split the url from the query string
    url = re.sub(r'\<\/{0,1}p\>', '', url)
    url = urlsplit(url)
    
    # check for v in the query string
    if 'v' in url.query:
        return url.query.split('=')[-1]

    else:
        return url.path.split('/')[-1]




def get_all_links(content: str) -> typing.Generator[str, None, None]:
    """get all youtube link types"""

    youtube_links = r'^ *<p>https://www.youtube.com/watch\?v=[\w\d_]+</p> *$'
    youtube_slash_links = r'^ *<p>https://www.youtube.com/watch\/[\w\d_]+</p> *$'
    youtube_shortlinks = r'^ *<p>https://youtu.be/[\w\d_]+</p> *$'
    youtube_shorts = r'^ *<p>https://www.youtube.com/shorts/[\w\d_]+</p> *$'

    links = [youtube_links, youtube_slash_links, youtube_shortlinks, youtube_shorts]
    link_groups = [re.findall(link_type, content, re.MULTILINE) for link_type in links]

    return itertools.chain(*link_groups)

def replace_youtube_links_with_embeds(content: str) -> str:
    """replace them with embeds"""

    links = get_all_links(content)

    for link in links:
        youtube_id = extract_youtube_id(link)
        logging.info(f"replacing youtube_id: {youtube_id}")

        # replace the link with the embed
        embed = f"<iframe width='560' height='315' src='https://www.youtube.com/embed/{youtube_id}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media;' allowfullscreen></iframe>"
        content = content.replace(link, embed)
    
    return content