from page_objects import PageObject

def getPages():
    pagesDict = dict()

    thisDesc = """This is your start page
    A = Yellout
    B = Next"""
    thisCmds = {"A": "YELLOUT", "B": "NEXT"}
    pagesDict["START"] = PageObject(thisDesc, thisCmds)

    thisDesc = "next text\r\nnext more text\r\ntype F to FOOBAR\r\ntype Q to bail on this party\r\n"
    thisCmds = {"F": "FOOBAR", "Q": "QUIT"}
    pagesDict["NEXT"] = PageObject(thisDesc, thisCmds)

    pagesDict["FOOBAR"] = PageObject("Bar is Foo teext, Q to Quit.\r\n", {"Q":"QUIT"})
    pagesDict["YELLOUT"] = PageObject("""
    No response...
                    
                    Press Q to leave.""",
                    {"Q":"QUIT"})

    # thisDesc = ""
    # thisCmds = {"":""}
    # pagesDict[""] = PageObject(thisDesc, thisCmds)

    return pagesDict

