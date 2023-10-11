import pytest
from render_engine.site import Site
from render_engine_youtube_embed.plugins import YouTubeEmbed

@pytest.fixture(scope="session")
def site(tmp_path_factory):
    """Returns a Site object"""
    class TestSite(Site):
        output_path = tmp_path_factory.getbasetemp()/ "output"

    app = TestSite()
    app.register_plugins(YouTubeEmbed)
    return app