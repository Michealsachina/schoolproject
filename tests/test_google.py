from playwright.sync_api import sync_playwright

def test_add_student():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://127.0.0.1:8000/students/add/")
        page.fill("input[name='name']", "Rahul")
        page.fill("input[name='age']", "20")
        page.click("button[type='submit']")

        assert "Rahul" in page.content()

        browser.close()