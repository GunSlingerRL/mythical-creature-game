from page_objects import PageObject
from instances import ghoul







def getPages():

    pagesDict = dict()

    thisDesc = """
    You wake up in a small village. Everything is different here.
    You get up and walk to the closest exit.
    Upon exiting you encounter a creature resembling a person, but it reeks of death.
    A = Attack
    B = Run"""
    thisCmds = {"A": "ATTACK", "B": "RUN"}
    pagesDict["START"] = PageObject(thisDesc, thisCmds)

    

    thisDesc = "next text\r\nnext more text\r\ntype F to FOOBAR\r\ntype Q to bail on this party\r\n"
    thisCmds = {"F": "FOOBAR", "Q": "QUIT"}
    pagesDict["NEXT"] = PageObject(thisDesc, thisCmds)

    pagesDict["FOOBAR"] = PageObject("Bar is Foo teext, Q to Quit.\r\n", {"Q":"QUIT"})
    pagesDict["RUN"] = PageObject("""
    No response...
                    
                    Press Q to leave.""",
                    {"Q":"QUIT"})

    # thisDesc = ""
    # thisCmds = {"":""}
    # pagesDict[""] = PageObject(thisDesc, thisCmds)

    return pagesDict

