from render_engine.hookspecs import hook_impl

class YouTubeEmbed:
    @hook_impl
    def pre_build_site(site):
        for page in pages:
            page.content = page.content.replace(
                "https://www.youtube.com/watch?v=5qap5aO4i9A",
                "{% youtube 5qap5aO4i9A %}",
            )