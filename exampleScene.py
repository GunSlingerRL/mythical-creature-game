pageDict["START"] = PageObject("""
    It's pitch black, damp and cold.
        The eery smell of rotting flesh is in the air.
            You see a silhouette of a tall figure ahead of you.
    
    What do you do?
                    a) run away
                    b) yell out to the figure
                    c) approach""",
                    {"A": "RUNAWAY", "B": "YELLOUT", "C": "APPROACH"})
    
pageDict["RUNAWAY"] = PageObject("""
    You got away safely, but the figure yells out to you.
        "I won't hurt you. I am alone.
    
                    What's your name?"
                    """,
                    {"A":"GOTAWAY"})
    
pageDict["YELLOUT"] = PageObject("""
    No response...
                    
                    Press Q to leave.""",
                    {"Q":"QUIT"})



###Attack the man
pageDict["ATTACKTHEMAN"] = """
You grab the Louisville Slugger by your door and approach the man. Something's not quite right about this guy.
He's not talking or yelling at the woman, but growling. It almost seems as if he's rabid.
"Hey, buddy, what's going on here!"
The man turns his attention to you. His eyes are pitch black!
His clothes are soaked with fresh crimson blood and his right arm looks to be disclocated.

He turns and begins to drunkingly walk towards you.
"Hey, man, I don't want any trouble. Just leave the poor girl alone."
The man ignores you and looks as if he wants to take a chunk out of you.
"Im warning you. I will knock your teeth out."
The man begins to pick up speed. You clinch the base of the bat and start to wind up a swing.
**BANG**
A gunshot goes off from behind you, leaving you a little dazed and your ears fill with high-pitched ringing.
You turn around and a man in a military uniform is standing clutching a pistol.
You hear a thud and turn to the man that was about to attack.
He's laying on the ground with blood pooling around his head.

**-a) "What the fuck man!"**
**-b) Drop the bat and raise your arms.**""",






# Example File on Disk

$START
%It's pitch black, damp and cold.
    The eery smell of rotting flesh is in the air.
        You see a silhouette of a tall figure ahead of you.
    
    What do you do?
                    a) run away
                    b) yell out to the figure
                    c) approach
%
&A=RUNAWAY
B=YELLOUT
C=APPROACH
&


KeyReadFromFile = "Start"
someStringReadInFromFile = "B=YELLOUT"

ListOfThatString = someStringReadInFromFile.split("=")
CommandDictionary[ListOfThatString[0]] = ListOfThatString[1]

PagesDict[KeyReadFromFile] = PageObject(DESCRIPTIONSTRINGHERE, CommandDictionary)


