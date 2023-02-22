from render_engine.hookspecs import hook_impl
from .youtube_embed import replace_youtube_links_with_embeds

class YouTubeEmbed:
    @hook_impl
    def pre_build_collection_pages(self, page: "Page") -> None:
        if hasattr(page, "raw_content"):
            content = replace_youtube_links_with_embeds(page.content)    
            if content != page.content:
                print(f"replacing youtube links in {page} with embeds")
                page.content = content

    @hook_impl
    def render_content(self, Page: "Page") -> None:
        Page.content= replace_youtube_links_with_embeds(getattr(Page, "markup", Page.content))