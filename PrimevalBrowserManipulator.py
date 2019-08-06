import asyncio
from pyppeteer import launch

async def main1():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://translate.google.com.br/?hl=pt-BR', timeout= 0) #timeout = 0 serve para impossibilitar erro por timeout
    dimensions = await page.evaluate('''() => {
        return {
            "width": document.documentElement.clientWidth,
            "height": document.documentElement.clientHeight
        }
    }''')
    await page.setViewport(dimensions)
    await page.click('.tlid-open-source-language-list', button='left')
    await page.screenshot({'path': r'C:\Users\Windows 7\Desktop\yes1.png'})
    await browser.close()

async def main2(a):
    exec(f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in a.split('\n'))
    )
    return await locals()['__ex']()

c=r"""browser = await launch()
page = await browser.newPage()
await page.goto('https://translate.google.com.br/?hl=pt-BR', timeout= 0)
dimensions = await page.evaluate('''() => {
    return {
        "width": document.documentElement.clientWidth,
        "height": document.documentElement.clientHeight
    }
}''')
await page.setViewport(dimensions)
await page.click('.tlid-open-source-language-list', button='left')
await page.screenshot({'path': r'C:\Users\Windows 7\Desktop\yes2.png'})
await browser.close()
"""

asyncio.get_event_loop().run_until_complete(main1())

asyncio.get_event_loop().run_until_complete(main2(c))