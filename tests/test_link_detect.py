from pathlib import Path

import pytest
from render_engine.page import Page
from render_engine.collection import Collection

from render_engine_youtube_embed.youtube_embed import (
    extract_youtube_id,
    replace_youtube_links_with_embeds,
)

test_urls = (
        "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch/5qap5aO4i9A",
        "https://www.youtube.com/shorts/5qap5aO4i9A",
        "https://youtu.be/5qap5aO4i9A",
        "<p>https://www.youtube.com/watch?v=5qap5aO4i9A</p>",
        "<p>https://www.youtube.com/watch/5qap5aO4i9A</p>",
        "<p>https://www.youtube.com/shorts/5qap5aO4i9A</p>",
        "<p>https://youtu.be/5qap5aO4i9A</p>",
)

@pytest.mark.parametrize(
    "test_url",
    [
        ("<p>https://www.youtube.com/watch?v=5qap5aO4i9A</p>"),
        ("<p>https://www.youtube.com/watch/5qap5aO4i9A</p>"),
        ("<p>https://www.youtube.com/shorts/5qap5aO4i9A</p>"),
        ("<p>https://youtu.be/5qap5aO4i9A<p>"),
    ]
)
def test_youtube_links_found(test_url):
    """Test that youtube links are found"""
    assert extract_youtube_id(test_url) == "5qap5aO4i9A"

@pytest.mark.parametrize(
        "test_url",
        [
        "https://www.youtube.com/watch?v=FRnKY-5TqOM",
        "https://www.youtube.com/watch/FRnKY-5TqOM",
        "https://www.youtube.com/shorts/FRnKY-5TqOM",
        "https://youtu.be/FRnKY-5TqOM",
        "<p>https://www.youtube.com/watch?v=FRnKY-5TqOM</p>",
        "<p>https://www.youtube.com/watch/FRnKY-5TqOM</p>",
        "<p>https://www.youtube.com/shorts/FRnKY-5TqOM</p>",
        "<p>https://youtu.be/FRnKY-5TqOM</p>",
        ])
def test_youtube_links_with_hyphens(test_url):
    """Test that youtube links with hyphens are found"""
    assert extract_youtube_id(test_url) == "FRnKY-5TqOM"

@pytest.mark.parametrize("test_url", test_urls)
def test_youtube_link_replaced_with_embed(test_url):
    """Tests that youtube links are replaced with embeds"""
    embed = replace_youtube_links_with_embeds(test_url) 

    assert 'https://www.youtube.com/embed/5qap5aO4i9A' in embed
    assert "aria-label='youtube-embed'" in embed
    assert "title='YouTube Video Player'" in embed

def test_multiple_text():

    text = """
    This new setting in VS Code allows you to auto-add f-strings

    https://www.youtube.com/shorts/ds6LG_N0Irw
    """

    replaced_text = replace_youtube_links_with_embeds(text)
    assert 'https://www.youtube.com/embed/ds6LG_N0Irw' in replaced_text
    assert "aria-label='youtube-embed'" in replaced_text
    assert "title='YouTube Video Player'" in replaced_text


@pytest.mark.parametrize("test_url", test_urls)
def test_replace_in_page(site, test_url, tmp_path_factory):
    """Tests the rendering with render engine"""
    @site.page
    class TestPage(Page):
        content=test_url

    site.render()

    output = tmp_path_factory.getbasetemp().joinpath("output/testpage.html")
    assert "youtube-embed" in output.read_text()


@pytest.mark.parametrize("test_url", test_urls)
def test_replace_in_collection_page(site, test_url, tmp_path_factory):
    """Tests the rendering with render engine"""
    Path(tmp_path_factory.getbasetemp() / "content").mkdir(parents=True, exist_ok=True)
    Path(tmp_path_factory.getbasetemp() / "content/testcontentpage.md").write_text(f"---\ntitle:test_collection_page\n---\n\n{test_url}")
    @site.collection
    class TestCollection(Collection):
        content_path = tmp_path_factory.getbasetemp()/ "content"
        routes = ["testcontentpage"]
        has_archive = True

    site.render()

    output = tmp_path_factory.getbasetemp().joinpath("output/testcontentpage/page.html")
    assert "youtube-embed" in output.read_text()


@pytest.mark.parametrize("test_url", test_urls)
def test_replace_in_collection_page(site, test_url, tmp_path_factory):
    """Tests the rendering with render engine archive pages should also be updated"""
    Path(tmp_path_factory.getbasetemp() / "content").mkdir(parents=True, exist_ok=True)
    Path(tmp_path_factory.getbasetemp() / "content/testcontentpage.md").write_text(f"---\ntitle:test_collection_page\n---\n\n{test_url}")
    @site.collection
    class TestCollection(Collection):
        content_path = tmp_path_factory.getbasetemp()/ "content"
        routes = ["testcontentpage"]
        has_archive = True

    site.render()

    output = tmp_path_factory.getbasetemp().joinpath("output/testcontentpage/page.html")
    assert "youtube-embed" in output.read_text()