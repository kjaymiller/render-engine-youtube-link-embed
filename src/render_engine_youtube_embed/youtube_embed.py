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
    youtube_links = r'^[ \t]*https://(?:www.){0,1}youtube.com/watch\?v=[\w\d_\-]+\s*$'
    youtube_slash_links = r'^[ \t]*https://(?:www.){0,1}youtube.com/watch\/[\w\d_\-]+\s*$'
    youtube_shortlinks = r'^[ \t]*https://(?:www.){0,1}youtu.be/[\w\d_\-]+\s*$'
    youtube_shorts = r'^[ \t]*https://(?:www.){0,1}youtube.com/shorts/[\w\d_\-]+\s*$'
    youtube_links_with_p = r'^[ \t]*<p>https://(?:www.){0,1}youtube.com/watch\?v=[\w\d_\-]+</p>\s*$' 
    youtube_slash_links_with_p = r'^[ \t]*<p>https://(?:www.){0,1}youtube.com/watch\/[\w\d_\-]+</p>\s*$'
    youtube_shortlinks_with_p = r'^[ \t]*<p>https://(?:www.){0,1}youtu.be/[\w\d_\-]+</p>\s*$'
    youtube_shorts_with_p = r'^[ \t]*<p>https://(?:www.){0,1}youtube.com/shorts/[\w\d_\-]+</p>\s*$'

    links = (
        youtube_links, 
        youtube_slash_links,
        youtube_shortlinks,
        youtube_shorts,
        youtube_links_with_p,
        youtube_slash_links_with_p,
        youtube_shortlinks_with_p,
        youtube_shorts_with_p,
        )
    link_groups = [re.findall(link_type, content, re.MULTILINE) for link_type in links]

    return itertools.chain(*link_groups)

def replace_youtube_links_with_embeds(content: str) -> str:
    """replace them with embeds"""

    links = get_all_links(content)

    for link in links:
        youtube_id = extract_youtube_id(link)
        logging.info(f"replacing youtube_id: {youtube_id}")

        # replace the link with the embed
        embed = f"<iframe aria-label='youtube-embed' title='YouTube Video Player' width='560' height='315' src='https://www.youtube.com/embed/{youtube_id}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media;' allowfullscreen></iframe>"
        content = content.replace(link, embed)
    
    return content