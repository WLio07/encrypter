#this program takes a screenshot of google translator after opening the drop-down menu of languages, using two different methods
import asyncio #it uses the pyppeteer package
from pyppeteer import launchasync #by rewriting the code, it can be repurposed to many different tasks, most commands are already here
#as usually there is little needed beyond typing and clicking, omission of main1 (comment it out) in favour of main2 is adviced
def main1(): #this method executes the program directly
    browser = await launch() #launches hidden browser
    page = await browser.newPage() #opens page (tab)
    await page.goto('https://translate.google.com/', timeout= 0) #timeout = 0 is to avoid Error: timeout
    dimensions = await page.evaluate('''() => { #evaluate code in the console that will take the width and height of the page
        return {
            "width": document.documentElement.clientWidth,
            "height": document.documentElement.clientHeight
        }
    }''')
    await page.setViewport(dimensions) #sets the viewport as the widths and heights that were taken
    await page.click('.tlid-open-source-language-list', button='left') #clicks elements with the class .tlid...
    await page.screenshot({'path': r'C:\path\yes1.png'}) #takes a screenshot and saves it in path as yes1.png
    await browser.close() #closes browser so it doesn't keep running (and using CPU) in the background

async def main2(a): #this program executes the program with exec() of a multi-line string containing the code, it helps avoiding errors
    exec(f'async def __ex(): ' + #this exec of a string helps avoiding some erros in some cases
        ''.join(f'\n {l}' for l in a.split('\n')) #after struggling with that error, I found a solution somewhere in the internet
    ) #I don't know how it solves the problem; it just works
    return await locals()['__ex']() #it is a safer approach, but a less straigthforward one

c=r"""browser = await launch() #this is the string that will be executed by main2(a), 'a' being the string as parameter
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

asyncio.get_event_loop().run_until_complete(main1()) #runs first method

asyncio.get_event_loop().run_until_complete(main2(c)) #runs second method
