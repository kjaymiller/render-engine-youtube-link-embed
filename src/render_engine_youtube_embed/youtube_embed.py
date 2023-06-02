import typing
import re

import logging
import itertools


def extract_youtube_id(url: str) -> str:
    """
    Extract the video id from a youtube url
    """

    matches = (
        ('https://www.youtube.com/watch?v=', '='),
        ('https://www.youtube.com/watch/', '/'),
        ('https://www.youtube.com/shorts/', '/'),
        ('https://youtu.be/', '/'),
    )

    for matcher, splitter in matches:
        if url.startswith(matcher):
            return url.split(splitter)[-1]


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