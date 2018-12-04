import os
from page_objects import PageObject
import pages


# clears the screen for windows or linux/uni
def clearScreen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


#function to inititate game
def main():
    # dictionary containing all our page objects stored by their PAGE_INDEX
    # pageDict = dict()
    pageDict: dict = pages.getPages()

   

    playing: bool = True  # we play till we aren't
    currentPage: str = "START"  # have to start somewhere, why not the "start" =P

    while playing:  # we play till we aren'tb

        clearScreen()
        thisPage: PageObject = pageDict.get(currentPage)
        print(thisPage.scene)
        # thisPage.get_scene()

        # Get user input as uppercase to make things easy on usb

        userInput: str = input("> ").upper()

        # test user input against special hard commands like 'quit' before comaring to the pages commands
        if userInput == "Q":
            playing = False
        elif userInput in thisPage.commands:
            currentPage = thisPage.commands.get(userInput)

    print("\r\nGoodbye!\r\n")

if __name__ == "__main__":
    main()
