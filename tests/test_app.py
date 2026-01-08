from playwright.sync_api import Page, expect

# Tests for your routes go here
# TESTS FOR MUSIC APP

"""
When we visit /albums
We see a list of albums and their release_year as per seed data. 
"""
def test_get_album_all(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_html_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    heading_tags = page.locator("h2")
    expect(heading_tags).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
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
def test_get_album_all(page, test_web_address):
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
