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
    embed = replace_youtube_links_with_embeds(test_url) 

    assert 'https://www.youtube.com/embed/5qap5aO4i9A' in embed
    assert "aria-label='youtube-embed'" in embed
    assert "title='YouTube Video Player'" in embed

def test_multiple_text():

    text = """
    <div class="">
    <p>This new setting in VS Code allows you to auto-add f-strings</p>

        <p>https://www.youtube.com/shorts/ds6LG_N0Irw</p>

    </div>
    """

    replaced_text = replace_youtube_links_with_embeds(text)
    assert 'https://www.youtube.com/embed/ds6LG_N0Irw' in replaced_text
    assert "aria-label='youtube-embed'" in replaced_text
    assert "title='YouTube Video Player'" in replaced_text