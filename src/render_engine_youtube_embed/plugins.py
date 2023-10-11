import logging
from render_engine.hookspecs import hook_impl
from .youtube_embed import replace_youtube_links_with_embeds

class YouTubeEmbed:
    # @hook_impl
    # def pre_build_collection(
    #     ,
    #     ) -> None:
    #     if hasattr(page, "content"):
    #         content = replace_youtube_links_with_embeds(page.content)    
    #         page.content = content

    @hook_impl
    def render_content(
        page: "Page",
        settings: {},
    ):
        if page._content:
            content = replace_youtube_links_with_embeds(page.content)    
            page.content= content