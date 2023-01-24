import re


def extract_youtube_id(url: str) -> str:
    """
    Extract the video id from a youtube url
    """
    if url.startswith('http://www.youtube.com/watch?v='):
        return url.split('=')[-1]

    elif url.startswith('http://youtu.be/'):
        return url.split('/')[-1]


def replace_youtube_links_with_embeds(text):
    """
    get all youtube links on their own line and replace them with embeds
    """

    # find all youtube links
    youtube_links = re.findall(r'http://www.youtube.com/watch\?v=[a-zA-Z0-9_-]+', text)
    youtube_shortlinks = re.findall(r'http://youtu.be/[a-zA-Z0-9_-]+', text)

    
    for link in [*youtube_links, *youtube_shortlinks]:
        youtube_id = extract_youtube_id(link)
        text = re.sub(text, link, f'<iframe width="560" height="315" src="http://www.youtube.com/embed/{youtube_id}" frameborder="0" allowfullscreen></iframe>')

    return text