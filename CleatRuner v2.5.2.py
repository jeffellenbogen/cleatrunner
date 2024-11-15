# ********* State functions *********

def state0_init():
    global snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakePositionOfHead, snakeDirection, snakeScore, snakeTrack, snakeIsAlive, endTimeOfCurrentStatems, stateOfGame
    snakeLength = [5, 8, 8]
    snakeCanScoreLeft = [1, 1, 1]
    snakeCanScoreRight = [1, 1, 1]
    snakePositionOfHead = [0, 0, 0]
    snakeDirection = [0, 0, 0]
    snakeScore = [1, 1, 1]
    snakeTrack = []
    snakeIsAlive = [1, 1, 1]
    for index9 in range(3):
        snakeColor: List[number] = []
        snakeColor.append(index9)
        snakeTrack.append(index9)
        spawnSnake(index9)
    for index4 in range(3):
        showSnake(index4)
    endTimeOfCurrentStatems = input.running_time() + 1000 * preRoundTimerLengthsecs
    stateOfGame = 0

def state1_init():
    global stateOfGame, resetGame
    basic.clear_screen()
    strip0.clear()
    strip1.clear()
    strip2.clear()
    strip0.show_rainbow(290, 350)
    strip1.show_rainbow(20, 80)
    strip2.show_rainbow(180, 240)
    stateOfGame = -1
    resetGame = False   

def state1_init2():
    snakeIcon()

def state2_init():
    global snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakeTrack, snakeIsAlive, stateOfGame
    snakeIcon()
    snakeLength = [8, 8, 5]
    snakeCanScoreLeft = [1, 1, 1]
    snakeCanScoreRight = [1, 1, 1]
    snakeTrack = [1, 2, 0]
    snakeIsAlive = [1, 1, 1]
    for index7 in range(3):
        spawnSnake(index7)
        showSnake(index7)
    stateOfGame = 2    

def state3_init():
    global snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakeTrack, snakeIsAlive, stateOfGame
    snakeIcon()
    snakeLength = [8, 5, 8]
    snakeCanScoreLeft = [1, 1, 1]
    snakeCanScoreRight = [1, 1, 1]
    snakeTrack = [2, 0, 1]
    snakeIsAlive = [1, 1, 1]
    for index5 in range(3):
        spawnSnake(index5)
        showSnake(index5)
    stateOfGame = 3

def state45_init():
    global lastRoundedSecOnCountdownTimersecs, endTimeOfCurrentStatems
    lastRoundedSecOnCountdownTimersecs = 1000 * (roundWinnerFlashTimesecs + interRoundTimerLengthsecs)
    endTimeOfCurrentStatems = input.running_time() + lastRoundedSecOnCountdownTimersecs

def state9_init():
    global scoreTotal, endTimeOfCurrentStatems, scoreProportionSnake0, scoreProportionSnake1, scoreProportionSnake2, rangeSnake0Proportion, rangeSnake1Proportion, rangeSnake2Proportion, stateOfGame
    scoreTotal = 0
    setTotalScore()
    endTimeOfCurrentStatems = input.running_time() + 2000
    scoreProportionSnake0 = Math.ceil(snakeScore[0] / scoreTotal * trackLengths[0])
    scoreProportionSnake1 = Math.ceil(snakeScore[1] / scoreTotal * trackLengths[0])
    scoreProportionSnake2 = Math.ceil(snakeScore[2] / scoreTotal * trackLengths[0])
    rangeSnake0Proportion = strip0.range(0, scoreProportionSnake0)
    basic.show_number(getWinner())
    rangeSnake1Proportion = strip0.range(scoreProportionSnake0, scoreProportionSnake1)
    rangeSnake2Proportion = strip0.range(scoreProportionSnake0 + scoreProportionSnake1,
        scoreProportionSnake2)
    stateOfGame = 9
    strip0.show_color(neopixel.colors(NeoPixelColors.BLACK))
    strip1.show_color(neopixel.colors(NeoPixelColors.BLACK))
    strip2.show_color(neopixel.colors(NeoPixelColors.BLACK))    

def state0_run():
    global countdownTimeRemainingms, stateOfGame
    countdownTimeRemainingms = endTimeOfCurrentStatems - input.running_time()
    if countdownTimeRemainingms >= 0:
        showCountdownTimer()
    else:
        basic.clear_screen()
        state1_init2()
        stateOfGame = 1

def state1_run():
    strip0.rotate(1)
    strip1.rotate(-1)
    strip2.rotate(1)
    strip0.show()
    strip1.show()
    strip2.show()

def state1_run2():
    global stateOfGame
    if currentTotalSnakesAlive() <= 1:
        state45_init()
        stateOfGame = 4
     

def state2_run():
    global stateOfGame
    if currentTotalSnakesAlive() <= 1:
        state45_init()
        stateOfGame = 5

def state3_run():
    if currentTotalSnakesAlive() <= 1:
        state9_init()
 
def state4_run():
    global countdownTimeRemainingms, stateOfGame
    countdownTimeRemainingms = endTimeOfCurrentStatems - input.running_time()
    if countdownTimeRemainingms > interRoundTimerLengthsecs * 1000:
        flashWinningSnake()
    elif countdownTimeRemainingms >= 0:
        showCountdownTimer()
    else:
        basic.clear_screen()
        state2_init()
        stateOfGame = 2

def state5_run():
    global countdownTimeRemainingms, stateOfGame
    countdownTimeRemainingms = endTimeOfCurrentStatems - input.running_time()
    if countdownTimeRemainingms > interRoundTimerLengthsecs * 1000:
        flashWinningSnake()
    elif countdownTimeRemainingms >= 0:
        showCountdownTimer()
    else:
        basic.clear_screen()
        state3_init()
        stateOfGame = 3

def state9_run():
    if resetGame:
        state1_init()
    else:
        if int(input.running_time() / flashStatePeriodms) % numFlashStates >= 1:
            rangeSnake0Proportion.show_color(returnSnakeBodyColor(0))
            rangeSnake1Proportion.show_color(returnSnakeBodyColor(1))
            rangeSnake2Proportion.show_color(returnSnakeBodyColor(2))
        else:
            if winningSnake == 0:
                rangeSnake0Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))
            elif winningSnake == 1:
                rangeSnake1Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))
            elif winningSnake == 2:
                rangeSnake2Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))

# ********* Utility Functions *********
def snakeIcon():
    basic.show_leds("""
        . # # # #
        # # . # #
        # . . . .
        # # . . #
        . # # # .
        """)

def displaySnakesScore(snakeIndex: number):
    global range2
    range2 = strip0.range(0, snakeScore[snakeIndex])
    range2.show_color(returnSnakeBodyColor(snakeIndex))
    basic.show_number(snakeScore[snakeIndex])

# This function determines whichSnake is on a given track that is passed as the trackNum parameter.
# 
# Loop through snakeTrack0, 1, 2 and see which snake is currently on the passed trackNum.
# 
# Return the snake(0, 1, or 2) for the given track
# 
# Error handling, returns -1 if somehow there is no snake on the track in question. NOTE - This might be helpful if there is no snake on a given track because the snake previously occupying a given track has already died in the current round.
def whichSnakeOnTrack(trackNum: number):
    for tempSnakeIndex in range(3):
        # Gets track position for each snake in order...
        # For example 
        # In round 2
        # Snake 0 -> 2
        # Snake 1 -> 0
        # Snake 2 -> 1
        if snakeTrack[tempSnakeIndex] == trackNum:
            if snakeIsAlive[tempSnakeIndex] != 0:
                return tempSnakeIndex
    return -1

def returnSnakeHeadColor(snakeIndex2: number):
    if snakeIndex2 == 0:
        return neopixel.rgb(255, 0, 0)
    elif snakeIndex2 == 1:
        return neopixel.rgb(0, 200, 50)
    else:
        return neopixel.rgb(100, 0, 255)

def setTotalScore():
    global scoreTotal
    scoreTotal = 0
    for index2 in range(3):
        scoreTotal += snakeScore[index2]

def showSnake(snakeIndex22: number):
    global tempTrack, currentPixel
    tempTrack = snakeTrack[snakeIndex22]
    stripArray[tempTrack].show_color(neopixel.colors(NeoPixelColors.BLACK))
    if snakeIsAlive[snakeIndex22] != 0:
        currentPixel = snakePositionOfHead[snakeIndex22]
        # Sets the current snake's head color
        stripArray[tempTrack].set_pixel_color(currentPixel, returnSnakeHeadColor(snakeIndex22))
        for index in range(snakeLength[snakeIndex22] - 1):
            # If you are moving left, snakeDirection is negative, but we want to be moving to the pixels to the right, so we invert the direction.
            # 
            # If you are moving right, snakeDirection is positive, but we want to be moving to the pixels to the left, so we also invert the direction.
            currentPixel = currentPixel + -1 * snakeDirection[snakeIndex22]
            # set the current snake's body segments to the body color
            stripArray[tempTrack].set_pixel_color(currentPixel, returnSnakeBodyColor(snakeIndex22))
        stripArray[tempTrack].show()

def flashWinningSnake():
    global numFlashStates, flashStatePeriodms
    numFlashStates = 3
    flashStatePeriodms = 150
    if int(input.running_time() / flashStatePeriodms) % numFlashStates < 2:
        showSnake(getRoundWinner())
    else:
        stripArray[snakeTrack[getRoundWinner()]].show_color(neopixel.colors(NeoPixelColors.BLACK))

# This function checks whether the current snake that has been sent a command (and therefore passed into this function as a parameter).
# 
# For the given snake we need to see if the snake is on Track 0, 1, or 2. The if/else statements are run based on the track of the current snake being evaluated.
# 
# We set currentIntersectionIndex to the index of the intersection that the snakePositionOfHead is touch for the current snake. The "find index of" block will either return the position in the appropriate intersections array where the head is currently located, or return -1 if the head isn't in an intersection on their current track.
# 
# IF the currentIntersectionsIndex DOES NOT = -1 (head is at an intersection) we continue...
# 
# ____________________
# Return values
# -1 -> not blocked at this pixel
# 0 -> blocked by snake 0
# 1 -> blocked by snake 1
# 2 -> blocked by snake 2
def isPixelBlocked(candPixel: number, candTrack: number):
    global currentIntersectionIndex, blockingSnakeIndex
    if candTrack == 0:
        currentIntersectionIndex = Track01Intersections.index_of(candPixel)
        if currentIntersectionIndex != -1:
            # temp variable blockingSnakeIndex is set to the return value for the snake on the other track for this intersection.
            # Here we are working on intersections of Track0 which crosses only Track1.
            # 
            # call whichSnakeOnTrack1 will return the snake on that track and store it in the temp variable blockingSnakeIndex.
            blockingSnakeIndex = whichSnakeOnTrack(1)
            if snakeIsAlive[blockingSnakeIndex] == 0:
                return -1
            # We use blockingSnakeIndex to get the direction of the snake that is potentially in the intersection.
            # If the direction = 1, the blocking Snake is facing RIGHT and we use compound AND statements to determine if the blocking snake is in the intersection (based on the positionOfHead and snakeLength).
            # 
            # If the direction = -1. we are moving LEFT, the math is slightly different, so it has a separate set of conditional statements to determine if the snake is blocking that intersection.
            if snakeDirection[blockingSnakeIndex] == 1:
                if snakePositionOfHead[blockingSnakeIndex] >= Track10Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - 1) <= Track10Intersections[currentIntersectionIndex]:
                    return blockingSnakeIndex
            elif snakePositionOfHead[blockingSnakeIndex] <= Track10Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - 1) >= Track10Intersections[currentIntersectionIndex]:
                return blockingSnakeIndex
    elif candTrack == 2:
        # Same concept as above...
        # We are looking at snake on Track 2 and see if it is block at an intersection onf Track
        currentIntersectionIndex = Track21Intersections.index_of(candPixel)
        # If the currentSnake's headPosition is at an intersection on this track....
        # 
        # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection
        if currentIntersectionIndex != -1:
            blockingSnakeIndex = whichSnakeOnTrack(1)
            if snakeIsAlive[blockingSnakeIndex] == 0:
                return -1
            if snakeDirection[blockingSnakeIndex] == 1:
                if snakePositionOfHead[blockingSnakeIndex] >= Track12Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - 1) <= Track12Intersections[currentIntersectionIndex]:
                    return blockingSnakeIndex
            elif snakePositionOfHead[blockingSnakeIndex] <= Track12Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - 1) >= Track12Intersections[currentIntersectionIndex]:
                return blockingSnakeIndex
    else:
        # Same concept as above...
        # We are looking at snake on Track 1 and see if it is block at an intersection on Track 0.
        # 
        # NOTE: Track 1 intersects with Track 0 and Track 2, which is why this section of code happens here and below.
        currentIntersectionIndex = Track10Intersections.index_of(candPixel)
        # If the currentSnake's headPosition is at an intersection on this track....
        # 
        # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection
        if currentIntersectionIndex != -1:
            blockingSnakeIndex = whichSnakeOnTrack(0)
            if snakeIsAlive[blockingSnakeIndex] == 0:
                return -1
            if snakeDirection[blockingSnakeIndex] == 1:
                if snakePositionOfHead[blockingSnakeIndex] >= Track01Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - 1) <= Track01Intersections[currentIntersectionIndex]:
                    return blockingSnakeIndex
            elif snakePositionOfHead[blockingSnakeIndex] <= Track01Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - 1) >= Track01Intersections[currentIntersectionIndex]:
                return blockingSnakeIndex
        # Same concept as above...
        # We are looking at snake on Track 1 and see if it is block at an intersection on Track 2.
        # 
        # NOTE: Track 1 intersects with Track 0 and Track 2, which is why this section of code happens here and above.
        currentIntersectionIndex = Track12Intersections.index_of(candPixel)
        # If the currentSnake's headPosition is at an intersection on this track....
        # 
        # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection
        if currentIntersectionIndex != -1:
            blockingSnakeIndex = whichSnakeOnTrack(2)
            if snakeIsAlive[blockingSnakeIndex] == 0:
                return -1
            if snakeDirection[blockingSnakeIndex] == 1:
                if snakePositionOfHead[blockingSnakeIndex] >= Track21Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - 1) <= Track21Intersections[currentIntersectionIndex]:
                    return blockingSnakeIndex
            elif snakePositionOfHead[blockingSnakeIndex] <= Track21Intersections[currentIntersectionIndex] and snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - 1) >= Track21Intersections[currentIntersectionIndex]:
                return blockingSnakeIndex
    return -1

def returnSnakeBodyColor(snakeIndex3: number):
    if snakeIndex3 == 0:
        return neopixel.rgb(200, 0, 200)
    elif snakeIndex3 == 1:
        return neopixel.rgb(120, 160, 0)
    else:
        return neopixel.rgb(0, 100, 255)

def showCountdownTimer():
    global currentRoundedSecOnCountdownTimersecs, lastRoundedSecOnCountdownTimersecs
    currentRoundedSecOnCountdownTimersecs = Math.round(countdownTimeRemainingms / 1000)
    if currentRoundedSecOnCountdownTimersecs != lastRoundedSecOnCountdownTimersecs:
        basic.show_number(currentRoundedSecOnCountdownTimersecs)
        lastRoundedSecOnCountdownTimersecs = currentRoundedSecOnCountdownTimersecs

def initLEDs():
    global strip0, strip1, strip2, stripArray
    strip0 = neopixel.create(DigitalPin.P2, trackLengths[0], NeoPixelMode.RGB)
    strip1 = neopixel.create(DigitalPin.P0, trackLengths[1], NeoPixelMode.RGB)
    strip2 = neopixel.create(DigitalPin.P1, trackLengths[2], NeoPixelMode.RGB)
    stripArray = [strip0, strip1, strip2]

def growSnake(snakeIndex4: number):
    # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track
    # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track
    # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track
    # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track
    snakeScore[snakeIndex4] = snakeScore[snakeIndex4] + 3
    snakeLength[snakeIndex4] = snakeLength[snakeIndex4] + 1
# When using the spawnSnake function, you MUST already set snakeTrack and snakeLength, otherwise things will not work properly.

def spawnSnake(snakeIndex5: number):
    global spawnSuccess, tempTrack, tempDirection, leftEdgeOfSnake, rightEdgeOfSnake, snakeIsBlocked, index52, tempPixel
    spawnSuccess = False
    while not (spawnSuccess):
        tempTrack = snakeTrack[snakeIndex5]
        snakePositionOfHead[snakeIndex5] = randint(snakeLength[snakeIndex5],
            trackLengths[tempTrack] - (snakeLength[snakeIndex5] - 1))
        tempDirection = randint(0, 1)
        if tempDirection == 0:
            snakeDirection[snakeIndex5] = -1
        else:
            snakeDirection[snakeIndex5] = 1
        if snakeDirection[snakeIndex5] == -1:
            leftEdgeOfSnake = snakePositionOfHead[snakeIndex5]
            rightEdgeOfSnake = snakePositionOfHead[snakeIndex5] + snakeLength[snakeIndex5] - 1
        else:
            rightEdgeOfSnake = snakePositionOfHead[snakeIndex5]
            leftEdgeOfSnake = snakePositionOfHead[snakeIndex5] - snakeLength[snakeIndex5] + 1
        snakeIsBlocked = False
        index52 = 0
        while index52 <= snakeLength[snakeIndex5]:
            tempPixel = leftEdgeOfSnake + index52
            if isPixelBlocked(tempPixel, snakeTrack[snakeIndex5]) != -1:
                snakeIsBlocked = True
                break
            index52 += 1
        if not (snakeIsBlocked):
            spawnSuccess = True

# This helper function is used to alter positionOfHead for the passed snakeIndex (0,1,or 2).
def moveSnake(snakeIndex6: number):
    # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.
    # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.
    # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.
    # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.
    snakePositionOfHead[snakeIndex6] = snakePositionOfHead[snakeIndex6] + snakeDirection[snakeIndex6]

def getRoundWinner():
    for index3 in range(3):
        if snakeIsAlive[index3] == 1:
            return index3
    return -1

# Need to deal with potential tie scores for 1st place
def getWinner():
    global winningSnake
    winningSnake = 0
    for index6 in range(3):
        if snakeScore[index6] > snakeScore[winningSnake]:
            winningSnake = index6
    return winningSnake

def currentTotalSnakesAlive():
    return snakeIsAlive[0] + (snakeIsAlive[1] + snakeIsAlive[2])

def snakeFuneral(deadSnakeIndex: number):
    global jumpingSnakeIndex
    showSnake(deadSnakeIndex)
    if snakeTrack[deadSnakeIndex] == 1:
        jumpingSnakeIndex = whichSnakeOnTrack(0)
        snakeIsAlive[jumpingSnakeIndex] = 0
        showSnake(jumpingSnakeIndex)
        snakeIsAlive[jumpingSnakeIndex] = 1
        snakeLength[jumpingSnakeIndex] = 2 * snakeLength[jumpingSnakeIndex]
        snakeTrack[jumpingSnakeIndex] = 1
        spawnSnake(jumpingSnakeIndex)
        showSnake(jumpingSnakeIndex)

def on_received_value(name, value):
    if stateOfGame >= 1 and stateOfGame <= 3:
        if value != 0:
            onCommandReceived(parse_float(name), value)
radio.on_received_value(on_received_value)

# This function sets all information about each track....
# 
# trackLengths array stores the number of Pixels for Track 0,1,2
# 
# trackFrictionCoefficients array is not currently used (could allow for different movement / speed based on pixel density differences for the track0 vs track1+2
# 
# set Track(0->1)Intersections stores the pixel location on track 0 for where it crosses track 1.
# 
# set Track(1->0)Intersections stores the pixel location on track 1 for where it crosses track 0.
# 
# set Track(1->2)Intersections stores the pixel location on track 1 for where it crosses track 2.
# 
# set Track(2->1)Intersections stores the pixel location on track 2 for where it crosses track 1.

def initTracks():
    global trackLengths, trackFrictionCoefficients, Track01Intersections, Track10Intersections, Track12Intersections, Track21Intersections
    # Track[0]=80 pixels
    # Track[1]=156 pixels
    # Trakc[2]=136 pixels
    trackLengths = [80, 156, 136]
    # Coefficents allow each track to run at a similar pace. Some tracks have lower pixel density (Track[0])
    trackFrictionCoefficients = [1, 1, 1]
    Track01Intersections = [16, 23, 44, 54]
    Track10Intersections = [33, 50, 89, 106]
    Track12Intersections = [6, 27, 55, 72, 130, 149]
    Track21Intersections = [5, 26, 46, 61, 115, 133]

def isCountdownTimerRunning():
    global countdownTimeRemainingms
    countdownTimeRemainingms = endTimeOfCurrentStatems - input.running_time()
    if countdownTimeRemainingms > 0:
        basic.show_number(Math.round(countdownTimeRemainingms / 1000))
        return True
    else:
        basic.show_number(0)
        return False

def on_logo_pressed():
    global resetGame
    if stateOfGame == -1:
        state0_init()
    elif stateOfGame >= 9:
        resetGame = True
    else:
        pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# movment value is converted to direction by simply determining if it was positive or negative...
# positive movement -> direction = 1
# negative movement -> direction = -1
def convertMovementToDirection(num: number):
    if num > 0:
        return 1
    else:
        return -1

# This function is used to adjust snakes' positionOfHead, direction, and growth based on the passed parameters of snakeIndex and movement...
# 
# Movement values translate to
# -3 = fast move left
# -2 = medium move left
# -1 = slow move left
# 0 = no movement
# 1 = slow move right
# 2 = medium move right
# 3 = fast move right
def onCommandReceived(snakeIndex7: number, movement: number):
    global lastDirection, newDirection, currentSnakeLength, currentSnakePositionOfHead, blockingSnakeIndex
    if stateOfGame >= 1 and stateOfGame <= 3:
        # Check to see if the controller has sent movement date for a snake that is dead.
        # If dead, return -1 (to avoid processing commands)
        # 
        # If alive, then process the command
        if snakeIsAlive[snakeIndex7] == 0:
            return -1
        lastDirection = snakeDirection[snakeIndex7]
        newDirection = convertMovementToDirection(movement)
        # We are using the movement parameter for TWO things...
        # 1. Direction
        # 2. Magnitude of movement
        # 
        # Compare the lastDirection the snake was moving (stored in snakeDirection array) to the newDirection returned by passing movement parameter from onCommandReceived into conventMovementToDirection function.
        # 
        # If direction has changed TWO things need to happen...
        # 1. Set the newDirection into snakeDirection array.
        # 
        # 2. The head flips to the other side of the snake when direction changes. To accomplish this we set 2 temp variables (currentSnakeLength and currentSnake Position). These are used to calculate and set the new snakePositionOfHead at the opposite side of the snake, thus we need to know where the head is and how long the snake currently is.
        if lastDirection != newDirection:
            snakeDirection[snakeIndex7] = newDirection
            # temp variables of currentSnakeLength and currentSnakePosition make is easier to calculate the snake's new positionOfHead depended on whether the snake is changing direction or not.
            currentSnakeLength = snakeLength[snakeIndex7]
            currentSnakePositionOfHead = snakePositionOfHead[snakeIndex7]
            if lastDirection == -1:
                # set snake's positionOfHead if it was moving LEFT
                # set snake's positionOfHead if it was moving LEFT
                # set snake's positionOfHead if it was moving LEFT
                # set snake's positionOfHead if it was moving LEFT
                snakePositionOfHead[snakeIndex7] = currentSnakePositionOfHead + currentSnakeLength - 1
            else:
                # set snake's positionOfHead if it was moving RIGHT
                # set snake's positionOfHead if it was moving RIGHT
                # set snake's positionOfHead if it was moving RIGHT
                # set snake's positionOfHead if it was moving RIGHT
                snakePositionOfHead[snakeIndex7] = currentSnakePositionOfHead - currentSnakeLength + 1
        # Magnitude = absolute value of the movement parameter
        # We loop through the next section for each pixel we WANT to TRY to move (based on Magnitude of the movement). There is no guarantee that there is enough space on the strip for a snake to move 3 spaces, but it might be able to move 1 or 2 spaces.
        # 
        # By running through this section step-by-step we can...
        # 1. Check to see if the snake can move to an open space and call the moveSnake function.
        # 2. Check to see if the snake is at the end of the strip and can score at that end of the strip. (The snake can only score/grow at an end of the strip that it hasn't scored at last time is scored). If it should score/grow we call growSnake
        for index8 in range(abs(movement)):
            # Checks for direction and to see if snake has room to continue moving in that direction (not at that edge).
            # 
            # Movement = - 1 (LEFT)
            # First IF statement is for moving LEFT and checks position 0 to see if their is room to move.
            # ELSE IF snake is already at LEFT edge AND the snake can score on the LEFT -> growSnake. Set CanScoreLeft to 0 and toggle CanScoreRight to 1.
            # 
            # Movement = 1 (RIGHT)
            # First IF statement is for moving RIGHT and checks position at far right of the track to see if their is room to move.
            # ELSE IF snake is already at RIGHT edge AND the snake can score on the RIGHT -> growSnake. Set CanScoreLeft to 1 and toggle CanScoreRight to 0.
            if newDirection == -1:
                if snakePositionOfHead[snakeIndex7] != 0:
                    moveSnake(snakeIndex7)
                    blockingSnakeIndex = isPixelBlocked(snakePositionOfHead[snakeIndex7], snakeTrack[snakeIndex7])
                    if blockingSnakeIndex != -1:
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        snakeScore[blockingSnakeIndex] = snakeScore[blockingSnakeIndex] + 2
                        snakeIsAlive[snakeIndex7] = 0
                        snakeFuneral(snakeIndex7)
                elif snakeCanScoreLeft[snakeIndex7] == 1:
                    growSnake(snakeIndex7)
                    snakeCanScoreLeft[snakeIndex7] = 0
                    snakeCanScoreRight[snakeIndex7] = 1
            elif newDirection == 1:
                if snakePositionOfHead[snakeIndex7] != trackLengths[snakeTrack[snakeIndex7]] - 1:
                    moveSnake(snakeIndex7)
                    blockingSnakeIndex = isPixelBlocked(snakePositionOfHead[snakeIndex7], snakeTrack[snakeIndex7])
                    if blockingSnakeIndex != -1:
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        # Add 2 to the score of the blocking snake after a collision has occurred.
                        snakeScore[blockingSnakeIndex] = snakeScore[blockingSnakeIndex] + 2
                        snakeIsAlive[snakeIndex7] = 0
                        snakeFuneral(snakeIndex7)
                elif snakeCanScoreRight[snakeIndex7] == 1:
                    growSnake(snakeIndex7)
                    snakeCanScoreLeft[snakeIndex7] = 1
                    snakeCanScoreRight[snakeIndex7] = 0
        if snakeIsAlive[snakeIndex7] == 1:
            showSnake(snakeIndex7)
        return 0
    else:
        return -1

# **************** CODE STARTS HERE *********************        
currentSnakePositionOfHead = 0
currentSnakeLength = 0
newDirection = 0
lastDirection = 0
scoreProportionSnake2 = 0
scoreProportionSnake1 = 0
scoreProportionSnake0 = 0
trackFrictionCoefficients: List[number] = []
jumpingSnakeIndex = 0
tempPixel = 0
index52 = 0
snakeIsBlocked = False
rightEdgeOfSnake = 0
leftEdgeOfSnake = 0
tempDirection = 0
spawnSuccess = False
trackLengths: List[number] = []
lastRoundedSecOnCountdownTimersecs = 0
currentRoundedSecOnCountdownTimersecs = 0
winningSnake = 0
rangeSnake2Proportion: neopixel.Strip = None
rangeSnake1Proportion: neopixel.Strip = None
rangeSnake0Proportion: neopixel.Strip = None
resetGame = False
Track12Intersections: List[number] = []
Track21Intersections: List[number] = []
Track10Intersections: List[number] = []
blockingSnakeIndex = 0
Track01Intersections: List[number] = []
currentIntersectionIndex = 0
snakeCanScoreRight: List[number] = []
snakeCanScoreLeft: List[number] = []
flashStatePeriodms = 0
numFlashStates = 0
snakeDirection: List[number] = []
snakeLength: List[number] = []
snakePositionOfHead: List[number] = []
currentPixel = 0
stripArray: List[neopixel.Strip] = []
tempTrack = 0
scoreTotal = 0
snakeIsAlive: List[number] = []
snakeTrack: List[number] = []
snakeScore: List[number] = []
range2: neopixel.Strip = None
endTimeOfCurrentStatems = 0
countdownTimeRemainingms = 0
strip2: neopixel.Strip = None
strip1: neopixel.Strip = None
strip0: neopixel.Strip = None
roundWinnerFlashTimesecs = 0
interRoundTimerLengthsecs = 0
preRoundTimerLengthsecs = 0
stateOfGame = 0
stateOfGame = -2
preRoundTimerLengthsecs = 5
interRoundTimerLengthsecs = 3
roundWinnerFlashTimesecs = 3
radio.set_group(200)
initTracks()
initLEDs()
state1_init()

def on_forever():
    # State -1 = PreGame LED display
    # State 0 = Countdown to game round 1.
    # State 1 = Round 1 of Game
    # State 2 = Round 2 of Game
    # State 3 = Round 3 of Game
    # State 4 = Transition from Round 1 to Round 2
    # State 5 = Transition from Round 2 to Round 3
    # State 9 = Game is over. Show snake proportional bar graph.
    if stateOfGame == -1:
        state1_run()
    elif stateOfGame == 0:
        state0_run()
    elif stateOfGame == 1:
        state1_run2()
    elif stateOfGame == 2:
        state2_run()
    elif stateOfGame == 3:
        state3_run()
    elif stateOfGame == 4:
        state4_run()
    elif stateOfGame == 5:
        state5_run()
    elif stateOfGame == 9:
        state9_run()
basic.forever(on_forever)

