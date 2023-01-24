import pytest
from render_engine_youtube_embed.youtube_embed import (
    extract_youtube_id,
    replace_youtube_links_with_embeds,
)

def test_youtube_links_found():
    """Test that youtube links are found"""
    test_url = "http://www.youtube.com/watch?v=5qap5aO4i9A"
    assert extract_youtube_id(test_url) == "5qap5aO4i9A"

def test_youtube_shortlinks_found():
    """Test that youtube shortlinks are found"""
    test_url = "http://youtu.be/5qap5aO4i9A"
    assert extract_youtube_id(test_url) == "5qap5aO4i9A"

def test_youtube_link_replaced_with_embed():
    """Tests that youtube links are replaced with embeds"""
    test_url = "http://www.youtube.com/watch?v=5qap5aO4i9A"
    expected_text = f'<iframe width="560" height="315" src="http://www.youtube.com/embed/5qap5aO4i9A" frameborder="0" allowfullscreen></iframe>'
    assert replace_youtube_links_with_embeds(test_url) == expected_text