import re


def extract_youtube_id(url: str) -> str:
    """
    Extract the video id from a youtube url
    """
    if url.startswith('https://www.youtube.com/watch?v='):
        return url.split('=')[-1]

    elif url.startswith('https://youtu.be/'):
        return url.split('/')[-1]


def replace_youtube_links_with_embeds(text):
    """
    get all youtube links on their own line and replace them with embeds
    """
    # find all youtube links
    youtube_links = re.findall(r'^ *https://www.youtube.com/watch\?v=[\w\d_-]+ *$', text, re.MULTILINE)
    youtube_shortlinks = re.findall(r'^ *https://youtu.be/[a-zA-Z0-9_-]+ *$', text, re.MULTILINE)

    
    for link in [*youtube_links, *youtube_shortlinks]:
        youtube_id = extract_youtube_id(link)
        print(f"replacing youtube_id: {youtube_id}")

        # replace the link with the embed
        embed = f"<iframe width='560' height='315' src='https://www.youtube.com/embed/{youtube_id}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media;' allowfullscreen></iframe>"
        text = text.replace(link, embed)

    return text