from playwright.sync_api import Page, expect
import pytest

# Tests for your routes go here
# TESTS FOR MUSIC APP

"""
Create a new album
"""
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    db_connection.seed("seeds/music_html_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')

"""
The page returned by GET /albums should contain a link for each album listed. 
It should link to /albums/<id>, where <id> is the corresponding album's id. 
That page should then show information about the specific album.
"""
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Title: Surfa Rosa'")
    release_year_tag = page.locator(".t-release_year")
    expect(release_year_tag).to_have_text("Released: 1988")

"""
When we request GET /albums/1
We can find one album by the album id. 
"""
def test_get_one_album_from_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    title_p = page.locator(".t-title") # the dot is important! Shows there is an element with a class, rather than a tag. 
    expect(title_p).to_have_text("Title: Doolittle") 
    release_p =page.locator(".t-release_year")
    expect(release_p).to_have_text("Released: 1989") 

"""
When we visit /albums
We see a list of albums and their release_year as per seed data. 
"""
# @pytest.mark.skip
def test_get_album_all(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")

    heading_tags = page.locator("h3")
    expect(heading_tags).to_have_text([ 
        "Title: Doolittle", 
        "Title: Surfa Rosa", 
        "Title: Waterloo",
        "Title: Super Trouper",
        "Title: Bossanova",
        "Title: Lover",
        "Title: Folklore",
        "Title: I Put a Spell on You",
        "Title: Baltimore",
        "Title: Here Comes the Sun",
        "Title: Fodder on My Wings",
        "Title: Ring Ring"
    ])

"""
When we visit /albums
The page will form with the right heading. 
"""
def test_get_album_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("Albums")  

# === Example Code Below ===
"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")
    # We look at the <strong> tag
    strong_tag = page.locator("strong")
    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
