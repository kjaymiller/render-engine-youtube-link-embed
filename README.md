# Render Engine YouTube Link Embed Plugin

> ***Note:*** This plugin is in the early development stage. It is not yet ready for production use.


This plugin allows you to quickly embed a Youtube video into your page by adding the youtube link to the page on its own line.

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

This also works for YouTube short links (e.g. `https://youtu.be/QH2-TGUlwu4`).

***Note:***
It does not work for playlists or channels.

## Installation

Install the package using pip:

```bash
pip install render-engine-youtube-link-embed
```

## TODO:

- [ ] Add support for site settings (Not yet implemented in render engine yet)
