from render_engine.hookspecs import hook_impl
from .youtube_embed import replace_youtube_links_with_embeds

class YouTubeEmbed:
    @hook_impl
    def pre_build_collection_pages(page: "Page") -> None:
        if hasattr(page, "content"):
            page.content = replace_youtube_links_with_embeds(page.content)    



    @hook_impl
    def pre_build_page(page: "Page") -> None:
        print(f"pre_build_page: {page}")
        if hasattr(page, "content"):
            page.content = replace_youtube_links_with_embeds(page.content)