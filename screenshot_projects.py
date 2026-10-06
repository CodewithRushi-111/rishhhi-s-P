import asyncio
from playwright.async_api import async_playwright

async def main():
    projects = [
        {"url": "https://layerflow.dev/", "file": "proj1.png"},
        {"url": "https://pharma-care-wine.vercel.app/", "file": "proj2.png"},
        {"url": "https://microworks.impiclabs.com/", "file": "proj3.png"}
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for proj in projects:
            print(f"Taking screenshot of {proj['url']}...")
            try:
                page = await browser.new_page(viewport={"width": 1280, "height": 800})
                await page.goto(proj["url"], wait_until="networkidle", timeout=60000)
                await page.screenshot(path=f"c:/Users/rishi/Desktop/rishhhi/{proj['file']}")
                print(f"Saved {proj['file']}")
                await page.close()
            except Exception as e:
                print(f"Failed to screenshot {proj['url']}: {e}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
