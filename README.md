# Render Engine YouTube Link Embed Plugin

This plugin allows you to quickly embed a Youtube video into your page by adding the youtube link to the page on its own line.

***

```markdown
---
slug: new-youtube-video
---

Check out this new video!

https://www.youtube.com/watch?v=QH2-TGUlwu4

```

This extension will change the content to 

```markdown
---
slug: new-youtube-video
---

Check out this new video!

<iframe src="https://www.youtube.com/embed/QH2-TGUlwu4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```

This also works for the following YouTube links:
- Long Links with video ID in query string - `https://www.youtube.com/watch?v=QH2-TGUlwu4`
- Long Links with video ID in path - `https://www.youtube.com/watch/QH2-TGUlwu4`
- Youtube Shorts Links - `https://www.youtube.com/shorts/QH2-TGUlwu4`
- YouTube short links - `https://youtu.be/QH2-TGUlwu4`

***Note:***
It does not work for playlists or channels.

## Installation

Install the package using pip:

```bash
pip install render-engine-youtube-link-embed
```

## TODO:

- [ ] Add support for site settings (Not yet implemented in render engine yet)
