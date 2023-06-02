import pytest

from render_engine_youtube_embed.youtube_embed import (
    extract_youtube_id,
    replace_youtube_links_with_embeds,
)

@pytest.mark.parametrize(
    "test_url, expected_id",
    [
        ("<p>https://www.youtube.com/watch?v=5qap5aO4i9A</p>", "5qap5aO4i9A"),
        ("<p>https://www.youtube.com/watch/5qap5aO4i9A</p>", "5qap5aO4i9A"),
        ("<p>https://www.youtube.com/shorts/5qap5aO4i9A</p>", "5qap5aO4i9A"),
        ("<p>https://youtu.be/5qap5aO4i9A<p>", "5qap5aO4i9A"),
    ]
)
def test_youtube_links_found(test_url, expected_id):
    """Test that youtube links are found"""
    assert extract_youtube_id(test_url) == expected_id

def test_youtube_link_replaced_with_embed():
    """Tests that youtube links are replaced with embeds"""
    test_url = "<p>https://www.youtube.com/watch?v=5qap5aO4i9A</p>"
    expected_text = "<iframe width='560' height='315' src='https://www.youtube.com/embed/5qap5aO4i9A' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media;' allowfullscreen></iframe>"
    assert replace_youtube_links_with_embeds(test_url) == expected_text