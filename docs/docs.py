from render_engine import Site, Page
from render_engine.parsers.markdown import MarkdownPageParser

app = Site()
app.site_vars.update ({
    "SITE_TITLE": "Kjaymiller Render Engine Theme",
    "SITE_URL": "https://kjaymiller.github.io/render_engine_theme_kjaymiller/",
    "SITE_AUTHOR": {
        "name": "kjaymiller",
        "email": "kjaymiller@gmail.com",
    },
    "NAVIGATION": [
        {
            "test": "GitHub",
            "url": "https://github.com/kjaymiller/render-engine-youtube-link-embed",
            "icon": "fa-brands fa-github",
        }    
    ],
    "theme": {
        "title_size": "small",
        "colors": {
            "main": "red-600",
        },
        "social": {
            "github": "https://github.com/kjaymiller/render-engine-youtube-link-embed",
            "x-twitter": "https://twitter.com/kjaymiller",
            "linkedin": "https://www.linkedin.com/in/kjaymiller/",
            "mastodon": "https://mastodon.social/@kjaymiller",
        },
        "fontawesome": "94d9a219ee"
    }
})
app.register_themes(kjaymiller)

@app.page
class Index(Page):
    template = "index.html"
    content_path = "../README.md"