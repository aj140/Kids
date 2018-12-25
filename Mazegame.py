'''

This is a maze game that I'll keep trying to make better!

'''

# Global variables
debug = False
gameDifficulty = 0
currRoom = 0
currRoomObj = None
roomList = [ None ]
lastRoom = 0

# Global word definitions
wall = 0
door = 1

# Definition of a Room 
class Room:
    def __init__( self, roomNum, up, down, left, right ):
        self.roomNum = roomNum
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        if ( debug ):
            print ( ">> Created room number %d" % (roomNum) )


# Initialization function for the game
def gameInitialize( startingRoom ):
    
    global lastRoom
    
    if ( debug ):
        print ( ">> Debug mode is on! Starting game initialization..." )
    
    # This will initialize a very simple test maze
    if ( gameDifficulty == 0 ):
        room1 = Room( 1, 2, 0, 0, 3 )
        room2 = Room( 2, 4, 1, 0, 0 )
        room3 = Room( 3, 0, 0, 1, 0 )
        room4 = Room( 4, 0, 2, 0, 5 )
        room5 = Room( 5, 0, 0, 4, 0 )

        roomList.append( room1 )
        roomList.append( room2 )
        roomList.append( room3 )
        roomList.append( room4 )
        roomList.append( room5 )
        lastRoom = 5
    
    elif ( gameDifficulty == 1 ):
        room1 = Room( 1, 2, 0, 0, 0 )
        room2 = Room( 2, 0, 1, 4, 3 )
        room3 = Room( 3, 10, 0, 2, 0 )
        room4 = Room( 4, 5, 0, 0, 2 )
        room5 = Room( 5, 6, 4, 0, 0 )
        room6 = Room( 6, 0, 5, 7, 8 )
        room7 = Room( 7, 0, 0, 0, 6 )
        room8 = Room( 8, 11, 0, 6, 9 )
        room9 = Room( 9, 0, 10, 8, 0 )
        room10 = Room( 10, 9, 3, 0, 0 )
        room11 = Room( 11, 0, 8, 0, 0 )
        
        roomList.append( room1 )
        roomList.append( room2 )
        roomList.append( room3 )
        roomList.append( room4 )
        roomList.append( room5 )
        roomList.append( room6 )
        roomList.append( room7 )
        roomList.append( room8 )
        roomList.append( room9 )
        roomList.append( room10 )
        roomList.append( room11 )
        lastRoom = 11

    elif ( gameDifficulty == 2 ):
        room1 = Room( 1, 0, 4, 0, 2 )
        room2 = Room( 2, 0, 3, 1, 0 )
        room3 = Room( 3, 2, 0, 4, 5 )
        room4 = Room( 4, 1, 0, 0, 3 )
        room5 = Room( 5, 0, 0, 3, 6 )
        room6 = Room( 6, 7, 13, 5, 0 )
        room7 = Room( 7, 0, 6, 0, 8 )
        room8 = Room( 8, 0, 0, 7, 9 )
        room9 = Room( 9, 0, 10, 8, 0 )
        room10 = Room( 10, 9, 11, 0, 0 )
        room11 = Room( 11, 10, 0, 12, 0 )
        room12 = Room( 12, 0, 0, 13, 11 )
        room13 = Room( 13, 6, 14, 0, 12 )
        room14 = Room( 14, 13, 16, 15, 0 )
        room15 = Room( 15, 0, 0, 0, 14 )
        room16 = Room( 16, 14, 0, 0, 17 )
        room17 = Room( 17, 0, 20, 16, 18 )
        room18 = Room( 18, 0, 19, 17, 0 )
        room19 = Room( 19, 18, 21, 20, 0 )
        room20 = Room( 20, 17, 0, 0, 19 )
        room21 = Room( 21, 19, 0, 0, 0 )
        
        roomList.append( room1 )
        roomList.append( room2 )
        roomList.append( room3 )
        roomList.append( room4 )
        roomList.append( room5 )
        roomList.append( room6 )
        roomList.append( room7 )
        roomList.append( room8 )
        roomList.append( room9 )
        roomList.append( room10 )
        roomList.append( room11 )
        roomList.append( room12 )
        roomList.append( room13 )
        roomList.append( room14 )
        roomList.append( room15 )
        roomList.append( room16 )
        roomList.append( room17 )
        roomList.append( room18 )
        roomList.append( room19 )
        roomList.append( room20 )
        roomList.append( room21 )
        lastRoom = 21

    else:
        print( "!! ERROR: Unknown game difficult level ")
    
    moveRoom( startingRoom )

# Function to move to a new room
def moveRoom( moveToRoom ):
    global currRoom
    currRoom = moveToRoom
    if ( debug ):
        print ( ">> You are now in room %d" % (currRoom) )
    
# Function to describe the current room the player is in
def descCurrRoom():
    global currRoomObj
    currRoomObj = roomList[ currRoom ]

    if ( debug ):
        print( ">> You are currently in room %d." % (currRoomObj.roomNum) )
    
    if ( currRoomObj.up > 0 ):
        print( "In front of you is a door" )
    if ( currRoomObj.down > 0 ):
        print( "To the back of you is a door" )
    if ( currRoomObj.left > 0 ):
        print( "To the left of you is a door" )
    if ( currRoomObj.right > 0 ):
        print( "To the right of you is a door" )
    
# Function to ask the user which room to move to and then make that move        
def askMoveInput():
    global currRoomObj
    global currRoom
    currRoomObj = roomList[ currRoom ]
    
    upArr = ["up", "forward", "front", "forwards"]
    downArr = ["down", "back", "backwards", "backward" ,"behind"]
    leftArr = ["left"]
    rightArr = ["right"]
    
    inputUnderstood = False
    
    while inputUnderstood != True:
        
        dirToMoveInput = input( "\n# Which direction do you want to move in?\n" )
        dirToMoveInput = dirToMoveInput.lower()
        
        if dirToMoveInput in upArr:
            if currRoomObj.up > 0:
                print( "\nOk, let's move %s!" % dirToMoveInput )
                currRoom = currRoomObj.up
                inputUnderstood = True
            else:
                print( "\n!! You can't walk into a wall, you silly!" )
                inputUnderstood = False
                
        elif dirToMoveInput in downArr:
            if currRoomObj.down > 0:
                print( "\nOk, let's move %s!" % dirToMoveInput )
                currRoom = currRoomObj.down
                inputUnderstood = True
            else:
                print( "\n!! Did you just try walking backwards into a wall?" )
                inputUnderstood = False
        
        elif dirToMoveInput in leftArr:
            if currRoomObj.left > 0:
                print( "\nOk, let's move %s!" % dirToMoveInput )
                currRoom = currRoomObj.left
                inputUnderstood = True
            else:
                print( "\n!! Try using a door, maybe." )
                inputUnderstood = False
            
        elif dirToMoveInput in rightArr:
            if currRoomObj.right > 0:
                print( "\nOk, let's move %s!" % dirToMoveInput )
                currRoom = currRoomObj.right
                inputUnderstood = True
            else:
                print( "\n!! Walking into a wall doesn't seem like a great idea!" )
                inputUnderstood = False
        
        else: print( "\n!! Sorry, I'm not sure what direction you mean. Try forward, backward, left, or right." )
        
# Function to set the game difficulty
def setGameDifficulty():
    global gameDifficulty
    
    difficultySet = False
    
    while difficultySet != True:
        gameDifficulty = int( input( "\nHow difficult do you want the game to be? Answer 0-2\n") )
        if gameDifficulty in [0,1,2]:
            print ( "Ok, no problem - good luck!" )
            difficultySet = True
        else:
            print ( "Try again with a number 0-2" )

#
#
# Actual game starts here
#
#

print ( "WELCOME TO THE MAZE GAME!\n" )

# ask the user how tough they want the maze to be
setGameDifficulty()

# first initialize the game by creating all the rooms and starting the player in a room
gameInitialize( 1 )

print ( "\nYou are at the start of the maze. Let's have a look around, shall we?\n" )

while ( currRoom < lastRoom ):
    descCurrRoom()
    askMoveInput()

print ( "\nWELL DONE!! YOU FOUND THE MAZE EXIT!!" )


