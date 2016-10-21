# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:12:13 2016

@author: neeziv
"""

def create_board():
    board= []    
    for i in range(11):
        # First Row Should Be lettering of Each Column 
        if i == 0:
            board.append(["  ", "A","B", "C","D", "E","F", "G","H", "I","J"])
        else:
            board.append(["O"]*11)
    for i in range(len(board)):
        # First Element in Each Column To Be Numbered After First row
        if i >0:
            if i !=10:
                #Formatting
                board[i][0] =" "+str(i)
            else:
                board[i][0] =str(i)

    return board

def print_board(board):
    for row in range(len(board)):
        print ("  ".join(board[row]))


def in_range(aList,shipLen):

    
    aList = aList.copy()
    print_board(aList)

    index = 0
    origin = 0
    rOrigin = 0
    cOrigin = 0

    lowRange = shipLen -1
    highRange = shipLen-1

    furthestUp = 0
    furthestDown = 0

    upDown = False
    leftRight = False

    shipPlotPoints = []    

    while index < shipLen:

        #after initial input
        if index > 0:

            #make sure we are getting int input
            try:
                row = int(input('Pick a row: '))
                col = int(input('Pick a col: '))

            #if not int input    
            except ValueError:
                print("Not valid input, use int")

            #if try is valid and it is int input    
            else:
                
                if aList[row][col] != 'O':
                    print("Invalid Spot or Spot Taken")

                #if row is greater than the given range left or right from original point or outside of range of list
                elif (row > (rOrigin+highRange)) or (row < (rOrigin-lowRange)) or (row < 0 or row > len(aList)-1 ):
                    print('Out of Range')

                elif (col > (cOrigin+highRange)) or (col < (cOrigin-lowRange)) or (col < 0 or col > len(aList)-1 ):
                    print('Out of Range')                    

                elif row != shipPlotPoints[0][0] and col != shipPlotPoints[0][1]:
                    print("Not in Same Row or Column")   

                else:

                    if row == shipPlotPoints[0][0] and index == 1:
                        print("Planting in Left and Right Direction")
                        leftRight = True
                        furthestUp = furthestDown = origin = cOrigin
                        
 
                    if col == shipPlotPoints[0][1] and index == 1:
                        print("Planting in Up and Down Direction")                      
                        upDown = True
                        furthestUp = furthestDown = origin = rOrigin
                      
                    
                    if leftRight:
                        pos = col
                    if upDown:
                        pos = row
                         
                                      
       
     
                    
                    #if new row is greater than the original position (going right) and the position is further than gone before
                    #row > furthestUp stops from redundant reducing of range. i.e. origin is 5, next point is 7, 6 shouldnt
                    #reduce the distance left we can go
                    if pos > origin and pos > furthestUp:

                        #decrease left range by how far right we went
                        lowRange = lowRange - (pos - furthestUp)
                        furthestUp = pos

                    #if new row is lower than the original position (going left) and the position is lower than gone before 
                    #row < furthestDown stops from redundant reducing of range. i.e. origin is 5, next point is 3, 4 shouldnt
                    #reduce the distance right we can go                 
                    if pos < origin and pos < furthestDown:

                        #decrease right range by how far left we went 
                        highRange = highRange - abs(pos - furthestDown)
                        furthestDown = pos

                    if (row == shipPlotPoints[0][0] and upDown) or (col == shipPlotPoints[0][1] and leftRight):
                        print("Can't Change Directions")
                        

                    else:                
                    #if the spot isnt already taken and valid                       
                        aList[row][col] = 'X'
                        index += 1
                        shipPlotPoints.append([row,col])
                        print(shipPlotPoints)
                       
            print('h',highRange) #checking whats ammount of right range
            print('l',lowRange) #checking whats ammount of left range


        #if this is our first input        
        else:

            #make sure we are getting int input
            try:
                row = int(input('Pick a row: '))
                col = int(input('Pick a col: '))

            #if we dont get int input
            except ValueError:
                print("Not Valid Input, use int")

            #if we are getting int input    
            else:

                #if we are out of range of list 
                if row < 0 or row > len(aList)-1:
                    print('Not In Range of List')


                #if we are in range of list    
                elif aList[row][col] != "O":
                        print("Invalid Spot")
                else:    
                    aList[row][col] = 'X'
                    index += 1
                    rOrigin = row
                    cOrigin = col
                    shipPlotPoints.append([row,col])

        print_board(aList)


        

aList = create_board()
in_range(aList,4)