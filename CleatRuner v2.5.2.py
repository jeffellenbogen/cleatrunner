{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red19\green118\blue70;\red144\green1\blue18;\red15\green112\blue1;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c3529\c52549\c34510;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c50196\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf0 \strokec4  state1_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     strip0.rotate(\cf5 \strokec5 1\cf0 \strokec4 )\cb1 \
\cb3     strip1.rotate(\cf5 \strokec5 -1\cf0 \strokec4 )\cb1 \
\cb3     strip2.rotate(\cf5 \strokec5 1\cf0 \strokec4 )\cb1 \
\cb3     strip0.show()\cb1 \
\cb3     strip1.show()\cb1 \
\cb3     strip2.show()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  snakeIcon():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     basic.show_leds(\cf6 \cb3 \strokec6 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6         . # # # #\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         # # . # #\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         # . . . .\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         # # . . #\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         . # # # .\cf0 \cb1 \strokec4 \
\cf6 \cb3 \strokec6         """\cf0 \cb3 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state1_init2():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     snakeIcon()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state0_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  countdownTimeRemainingms, stateOfGame\cb1 \
\cb3     countdownTimeRemainingms = endTimeOfCurrentStatems - \cf2 \strokec2 input\cf0 \strokec4 .running_time()\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  countdownTimeRemainingms >= \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         showCountdownTimer()\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         basic.clear_screen()\cb1 \
\cb3         state1_init2()\cb1 \
\cb3         stateOfGame = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state4_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  countdownTimeRemainingms, stateOfGame\cb1 \
\cb3     countdownTimeRemainingms = endTimeOfCurrentStatems - \cf2 \strokec2 input\cf0 \strokec4 .running_time()\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  countdownTimeRemainingms > interRoundTimerLengthsecs * \cf5 \strokec5 1000\cf0 \strokec4 :\cb1 \
\cb3         flashWinningSnake()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  countdownTimeRemainingms >= \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         showCountdownTimer()\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         basic.clear_screen()\cb1 \
\cb3         state2_init()\cb1 \
\cb3         stateOfGame = \cf5 \strokec5 2\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  displaySnakesScore(snakeIndex: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  range2\cb1 \
\cb3     range2 = strip0.\cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 0\cf0 \strokec4 , snakeScore[snakeIndex])\cb1 \
\cb3     range2.show_color(returnSnakeBodyColor(snakeIndex))\cb1 \
\cb3     basic.show_number(snakeScore[snakeIndex])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # This function determines whichSnake is on a given track that is passed as the trackNum parameter.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # Loop through snakeTrack0, 1, 2 and see which snake is currently on the passed trackNum.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # Return the snake(0, 1, or 2) for the given track\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # Error handling, returns -1 if somehow there is no snake on the track in question. NOTE - This might be helpful if there is no snake on a given track because the snake previously occupying a given track has already died in the current round.\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  whichSnakeOnTrack(trackNum: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 for\cf0 \strokec4  tempSnakeIndex \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         \cf7 \strokec7 # Gets track position for each snake in order...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # For example \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # In round 2\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Snake 0 -> 2\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Snake 1 -> 0\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Snake 2 -> 1\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeTrack[tempSnakeIndex] == trackNum:\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[tempSnakeIndex] != \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  tempSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  returnSnakeHeadColor(snakeIndex2: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  snakeIndex2 == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 255\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  snakeIndex2 == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 200\cf0 \strokec4 , \cf5 \strokec5 50\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 100\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 255\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  setTotalScore():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  scoreTotal\cb1 \
\cb3     scoreTotal = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index2 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         scoreTotal += snakeScore[index2]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  showSnake(snakeIndex22: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  tempTrack, currentPixel\cb1 \
\cb3     tempTrack = snakeTrack[snakeIndex22]\cb1 \
\cb3     stripArray[tempTrack].show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[snakeIndex22] != \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         currentPixel = snakePositionOfHead[snakeIndex22]\cb1 \
\cb3         \cf7 \strokec7 # Sets the current snake's head color\cf0 \cb1 \strokec4 \
\cb3         stripArray[tempTrack].set_pixel_color(currentPixel, returnSnakeHeadColor(snakeIndex22))\cb1 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  index \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (snakeLength[snakeIndex22] - \cf5 \strokec5 1\cf0 \strokec4 ):\cb1 \
\cb3             \cf7 \strokec7 # If you are moving left, snakeDirection is negative, but we want to be moving to the pixels to the right, so we invert the direction.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # If you are moving right, snakeDirection is positive, but we want to be moving to the pixels to the left, so we also invert the direction.\cf0 \cb1 \strokec4 \
\cb3             currentPixel = currentPixel + \cf5 \strokec5 -1\cf0 \strokec4  * snakeDirection[snakeIndex22]\cb1 \
\cb3             \cf7 \strokec7 # set the current snake's body segments to the body color\cf0 \cb1 \strokec4 \
\cb3             stripArray[tempTrack].set_pixel_color(currentPixel, returnSnakeBodyColor(snakeIndex22))\cb1 \
\cb3         stripArray[tempTrack].show()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  flashWinningSnake():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  numFlashStates, flashStatePeriodms\cb1 \
\cb3     numFlashStates = \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\cb3     flashStatePeriodms = \cf5 \strokec5 150\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 int\cf0 \strokec4 (\cf2 \strokec2 input\cf0 \strokec4 .running_time() / flashStatePeriodms) % numFlashStates < \cf5 \strokec5 2\cf0 \strokec4 :\cb1 \
\cb3         showSnake(getRoundWinner())\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         stripArray[snakeTrack[getRoundWinner()]].show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state0_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakePositionOfHead, snakeDirection, snakeScore, snakeTrack, snakeIsAlive, endTimeOfCurrentStatems, stateOfGame\cb1 \
\cb3     snakeLength = [\cf5 \strokec5 5\cf0 \strokec4 , \cf5 \strokec5 8\cf0 \strokec4 , \cf5 \strokec5 8\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreLeft = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreRight = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakePositionOfHead = [\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 ]\cb1 \
\cb3     snakeDirection = [\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 ]\cb1 \
\cb3     snakeScore = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeTrack = []\cb1 \
\cb3     snakeIsAlive = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index9 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         snakeColor: List[number] = []\cb1 \
\cb3         snakeColor.append(index9)\cb1 \
\cb3         snakeTrack.append(index9)\cb1 \
\cb3         spawnSnake(index9)\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index4 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         showSnake(index4)\cb1 \
\cb3     endTimeOfCurrentStatems = \cf2 \strokec2 input\cf0 \strokec4 .running_time() + \cf5 \strokec5 1000\cf0 \strokec4  * preRoundTimerLengthsecs\cb1 \
\cb3     stateOfGame = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # This function checks whether the current snake that has been sent a command (and therefore passed into this function as a parameter).\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # For the given snake we need to see if the snake is on Track 0, 1, or 2. The if/else statements are run based on the track of the current snake being evaluated.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # We set currentIntersectionIndex to the index of the intersection that the snakePositionOfHead is touch for the current snake. The "find index of" block will either return the position in the appropriate intersections array where the head is currently located, or return -1 if the head isn't in an intersection on their current track.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # IF the currentIntersectionsIndex DOES NOT = -1 (head is at an intersection) we continue...\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # ____________________\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # Return values\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # -1 -> not blocked at this pixel\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 0 -> blocked by snake 0\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 1 -> blocked by snake 1\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 2 -> blocked by snake 2\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  isPixelBlocked(candPixel: number, candTrack: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  currentIntersectionIndex, blockingSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  candTrack == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         currentIntersectionIndex = Track01Intersections.index_of(candPixel)\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  currentIntersectionIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3             \cf7 \strokec7 # temp variable blockingSnakeIndex is set to the return value for the snake on the other track for this intersection.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # Here we are working on intersections of Track0 which crosses only Track1.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # call whichSnakeOnTrack1 will return the snake on that track and store it in the temp variable blockingSnakeIndex.\cf0 \cb1 \strokec4 \
\cb3             blockingSnakeIndex = whichSnakeOnTrack(\cf5 \strokec5 1\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[blockingSnakeIndex] == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # We use blockingSnakeIndex to get the direction of the snake that is potentially in the intersection.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # If the direction = 1, the blocking Snake is facing RIGHT and we use compound AND statements to determine if the blocking snake is in the intersection (based on the positionOfHead and snakeLength).\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # If the direction = -1. we are moving LEFT, the math is slightly different, so it has a separate set of conditional statements to determine if the snake is blocking that intersection.\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeDirection[blockingSnakeIndex] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] >= Track10Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) <= Track10Intersections[currentIntersectionIndex]:\cb1 \
\cb3                     \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] <= Track10Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) >= Track10Intersections[currentIntersectionIndex]:\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  candTrack == \cf5 \strokec5 2\cf0 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 # Same concept as above...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # We are looking at snake on Track 2 and see if it is block at an intersection onf Track\cf0 \cb1 \strokec4 \
\cb3         currentIntersectionIndex = Track21Intersections.index_of(candPixel)\cb1 \
\cb3         \cf7 \strokec7 # If the currentSnake's headPosition is at an intersection on this track....\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  currentIntersectionIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3             blockingSnakeIndex = whichSnakeOnTrack(\cf5 \strokec5 1\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[blockingSnakeIndex] == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeDirection[blockingSnakeIndex] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] >= Track12Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) <= Track12Intersections[currentIntersectionIndex]:\cb1 \
\cb3                     \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] <= Track12Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) >= Track12Intersections[currentIntersectionIndex]:\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 # Same concept as above...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # We are looking at snake on Track 1 and see if it is block at an intersection on Track 0.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # NOTE: Track 1 intersects with Track 0 and Track 2, which is why this section of code happens here and below.\cf0 \cb1 \strokec4 \
\cb3         currentIntersectionIndex = Track10Intersections.index_of(candPixel)\cb1 \
\cb3         \cf7 \strokec7 # If the currentSnake's headPosition is at an intersection on this track....\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  currentIntersectionIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3             blockingSnakeIndex = whichSnakeOnTrack(\cf5 \strokec5 0\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[blockingSnakeIndex] == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeDirection[blockingSnakeIndex] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] >= Track01Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) <= Track01Intersections[currentIntersectionIndex]:\cb1 \
\cb3                     \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] <= Track01Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) >= Track01Intersections[currentIntersectionIndex]:\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3         \cf7 \strokec7 # Same concept as above...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # We are looking at snake on Track 1 and see if it is block at an intersection on Track 2.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # NOTE: Track 1 intersects with Track 0 and Track 2, which is why this section of code happens here and above.\cf0 \cb1 \strokec4 \
\cb3         currentIntersectionIndex = Track12Intersections.index_of(candPixel)\cb1 \
\cb3         \cf7 \strokec7 # If the currentSnake's headPosition is at an intersection on this track....\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Then, check the other snake that COULD hit this intersection, to see if it is also occupying the intersection\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  currentIntersectionIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3             blockingSnakeIndex = whichSnakeOnTrack(\cf5 \strokec5 2\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[blockingSnakeIndex] == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  snakeDirection[blockingSnakeIndex] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] >= Track21Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] - (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) <= Track21Intersections[currentIntersectionIndex]:\cb1 \
\cb3                     \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] <= Track21Intersections[currentIntersectionIndex] \cf2 \strokec2 and\cf0 \strokec4  snakePositionOfHead[blockingSnakeIndex] + (snakeLength[blockingSnakeIndex] - \cf5 \strokec5 1\cf0 \strokec4 ) >= Track21Intersections[currentIntersectionIndex]:\cb1 \
\cb3                 \cf2 \strokec2 return\cf0 \strokec4  blockingSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state9_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  resetGame:\cb1 \
\cb3         state1_init()\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 int\cf0 \strokec4 (\cf2 \strokec2 input\cf0 \strokec4 .running_time() / flashStatePeriodms) % numFlashStates >= \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3             rangeSnake0Proportion.show_color(returnSnakeBodyColor(\cf5 \strokec5 0\cf0 \strokec4 ))\cb1 \
\cb3             rangeSnake1Proportion.show_color(returnSnakeBodyColor(\cf5 \strokec5 1\cf0 \strokec4 ))\cb1 \
\cb3             rangeSnake2Proportion.show_color(returnSnakeBodyColor(\cf5 \strokec5 2\cf0 \strokec4 ))\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  winningSnake == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                 rangeSnake0Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  winningSnake == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 rangeSnake1Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  winningSnake == \cf5 \strokec5 2\cf0 \strokec4 :\cb1 \
\cb3                 rangeSnake2Proportion.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state1_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  stateOfGame, resetGame\cb1 \
\cb3     basic.clear_screen()\cb1 \
\cb3     strip0.clear()\cb1 \
\cb3     strip1.clear()\cb1 \
\cb3     strip2.clear()\cb1 \
\cb3     strip0.show_rainbow(\cf5 \strokec5 290\cf0 \strokec4 , \cf5 \strokec5 350\cf0 \strokec4 )\cb1 \
\cb3     strip1.show_rainbow(\cf5 \strokec5 20\cf0 \strokec4 , \cf5 \strokec5 80\cf0 \strokec4 )\cb1 \
\cb3     strip2.show_rainbow(\cf5 \strokec5 180\cf0 \strokec4 , \cf5 \strokec5 240\cf0 \strokec4 )\cb1 \
\cb3     stateOfGame = \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3     resetGame = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  returnSnakeBodyColor(snakeIndex3: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  snakeIndex3 == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 200\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 200\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  snakeIndex3 == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 120\cf0 \strokec4 , \cf5 \strokec5 160\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  neopixel.rgb(\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 100\cf0 \strokec4 , \cf5 \strokec5 255\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  showCountdownTimer():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  currentRoundedSecOnCountdownTimersecs, lastRoundedSecOnCountdownTimersecs\cb1 \
\cb3     currentRoundedSecOnCountdownTimersecs = Math.\cf2 \strokec2 round\cf0 \strokec4 (countdownTimeRemainingms / \cf5 \strokec5 1000\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  currentRoundedSecOnCountdownTimersecs != lastRoundedSecOnCountdownTimersecs:\cb1 \
\cb3         basic.show_number(currentRoundedSecOnCountdownTimersecs)\cb1 \
\cb3         lastRoundedSecOnCountdownTimersecs = currentRoundedSecOnCountdownTimersecs\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state45_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  lastRoundedSecOnCountdownTimersecs, endTimeOfCurrentStatems\cb1 \
\cb3     lastRoundedSecOnCountdownTimersecs = \cf5 \strokec5 1000\cf0 \strokec4  * (roundWinnerFlashTimesecs + interRoundTimerLengthsecs)\cb1 \
\cb3     endTimeOfCurrentStatems = \cf2 \strokec2 input\cf0 \strokec4 .running_time() + lastRoundedSecOnCountdownTimersecs\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  initLEDs():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  strip0, strip1, strip2, stripArray\cb1 \
\cb3     strip0 = neopixel.create(DigitalPin.P2, trackLengths[\cf5 \strokec5 0\cf0 \strokec4 ], NeoPixelMode.RGB)\cb1 \
\cb3     strip1 = neopixel.create(DigitalPin.P0, trackLengths[\cf5 \strokec5 1\cf0 \strokec4 ], NeoPixelMode.RGB)\cb1 \
\cb3     strip2 = neopixel.create(DigitalPin.P1, trackLengths[\cf5 \strokec5 2\cf0 \strokec4 ], NeoPixelMode.RGB)\cb1 \
\cb3     stripArray = [strip0, strip1, strip2]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  growSnake(snakeIndex4: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Add 3 to the score for the current snakeIndex. This is called when a snake reaches an egg at either end of their track\cf0 \cb1 \strokec4 \
\cb3     snakeScore[snakeIndex4] = snakeScore[snakeIndex4] + \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\cb3     snakeLength[snakeIndex4] = snakeLength[snakeIndex4] + \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # When using the spawnSnake function, you MUST already set snakeTrack and snakeLength, otherwise things will not work properly.\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  spawnSnake(snakeIndex5: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  spawnSuccess, tempTrack, tempDirection, leftEdgeOfSnake, rightEdgeOfSnake, snakeIsBlocked, index52, tempPixel\cb1 \
\cb3     spawnSuccess = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 while\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  (spawnSuccess):\cb1 \
\cb3         tempTrack = snakeTrack[snakeIndex5]\cb1 \
\cb3         snakePositionOfHead[snakeIndex5] = randint(snakeLength[snakeIndex5],\cb1 \
\cb3             trackLengths[tempTrack] - (snakeLength[snakeIndex5] - \cf5 \strokec5 1\cf0 \strokec4 ))\cb1 \
\cb3         tempDirection = randint(\cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  tempDirection == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3             snakeDirection[snakeIndex5] = \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             snakeDirection[snakeIndex5] = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeDirection[snakeIndex5] == \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3             leftEdgeOfSnake = snakePositionOfHead[snakeIndex5]\cb1 \
\cb3             rightEdgeOfSnake = snakePositionOfHead[snakeIndex5] + snakeLength[snakeIndex5] - \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             rightEdgeOfSnake = snakePositionOfHead[snakeIndex5]\cb1 \
\cb3             leftEdgeOfSnake = snakePositionOfHead[snakeIndex5] - snakeLength[snakeIndex5] + \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         snakeIsBlocked = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3         index52 = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 while\cf0 \strokec4  index52 <= snakeLength[snakeIndex5]:\cb1 \
\cb3             tempPixel = leftEdgeOfSnake + index52\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  isPixelBlocked(tempPixel, snakeTrack[snakeIndex5]) != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3                 snakeIsBlocked = \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3                 \cf2 \strokec2 break\cf0 \cb1 \strokec4 \
\cb3             index52 += \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  (snakeIsBlocked):\cb1 \
\cb3             spawnSuccess = \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # This helper function is used to alter positionOfHead for the passed snakeIndex (0,1,or 2).\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  moveSnake(snakeIndex6: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # sets the snakePositionofHead for the current snakeIndex to the sum of the current position + direction. So this moves the head right by 1 if the direction is positive and left if the direction is negative.\cf0 \cb1 \strokec4 \
\cb3     snakePositionOfHead[snakeIndex6] = snakePositionOfHead[snakeIndex6] + snakeDirection[snakeIndex6]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state2_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  stateOfGame\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  currentTotalSnakesAlive() <= \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         state45_init()\cb1 \
\cb3         stateOfGame = \cf5 \strokec5 5\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  getRoundWinner():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 for\cf0 \strokec4  index3 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[index3] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  index3\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # Need to deal with potential tie scores for 1st place\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  getWinner():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  winningSnake\cb1 \
\cb3     winningSnake = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index6 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeScore[index6] > snakeScore[winningSnake]:\cb1 \
\cb3             winningSnake = index6\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  winningSnake\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  currentTotalSnakesAlive():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 return\cf0 \strokec4  snakeIsAlive[\cf5 \strokec5 0\cf0 \strokec4 ] + (snakeIsAlive[\cf5 \strokec5 1\cf0 \strokec4 ] + snakeIsAlive[\cf5 \strokec5 2\cf0 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  snakeFuneral(deadSnakeIndex: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  jumpingSnakeIndex\cb1 \
\cb3     showSnake(deadSnakeIndex)\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  snakeTrack[deadSnakeIndex] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         jumpingSnakeIndex = whichSnakeOnTrack(\cf5 \strokec5 0\cf0 \strokec4 )\cb1 \
\cb3         snakeIsAlive[jumpingSnakeIndex] = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3         showSnake(jumpingSnakeIndex)\cb1 \
\cb3         snakeIsAlive[jumpingSnakeIndex] = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         snakeLength[jumpingSnakeIndex] = \cf5 \strokec5 2\cf0 \strokec4  * snakeLength[jumpingSnakeIndex]\cb1 \
\cb3         snakeTrack[jumpingSnakeIndex] = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         spawnSnake(jumpingSnakeIndex)\cb1 \
\cb3         showSnake(jumpingSnakeIndex)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state1_run2():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  stateOfGame\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  currentTotalSnakesAlive() <= \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         state45_init()\cb1 \
\cb3         stateOfGame = \cf5 \strokec5 4\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state3_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakeTrack, snakeIsAlive, stateOfGame\cb1 \
\cb3     snakeIcon()\cb1 \
\cb3     snakeLength = [\cf5 \strokec5 8\cf0 \strokec4 , \cf5 \strokec5 5\cf0 \strokec4 , \cf5 \strokec5 8\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreLeft = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreRight = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeTrack = [\cf5 \strokec5 2\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeIsAlive = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index5 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         spawnSnake(index5)\cb1 \
\cb3         showSnake(index5)\cb1 \
\cb3     stateOfGame = \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  on_received_value(name, value):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  stateOfGame >= \cf5 \strokec5 1\cf0 \strokec4  \cf2 \strokec2 and\cf0 \strokec4  stateOfGame <= \cf5 \strokec5 3\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  value != \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3             onCommandReceived(parse_float(name), value)\cb1 \
\cb3 radio.on_received_value(on_received_value)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # This function sets all information about each track....\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # trackLengths array stores the number of Pixels for Track 0,1,2\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # trackFrictionCoefficients array is not currently used (could allow for different movement / speed based on pixel density differences for the track0 vs track1+2\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # set Track(0->1)Intersections stores the pixel location on track 0 for where it crosses track 1.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # set Track(1->0)Intersections stores the pixel location on track 1 for where it crosses track 0.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # set Track(1->2)Intersections stores the pixel location on track 1 for where it crosses track 2.\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # set Track(2->1)Intersections stores the pixel location on track 2 for where it crosses track 1.\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  initTracks():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  trackLengths, trackFrictionCoefficients, Track01Intersections, Track10Intersections, Track12Intersections, Track21Intersections\cb1 \
\cb3     \cf7 \strokec7 # Track[0]=80 pixels\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Track[1]=156 pixels\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # Trakc[2]=136 pixels\cf0 \cb1 \strokec4 \
\cb3     trackLengths = [\cf5 \strokec5 80\cf0 \strokec4 , \cf5 \strokec5 156\cf0 \strokec4 , \cf5 \strokec5 136\cf0 \strokec4 ]\cb1 \
\cb3     \cf7 \strokec7 # Coefficents allow each track to run at a similar pace. Some tracks have lower pixel density (Track[0])\cf0 \cb1 \strokec4 \
\cb3     trackFrictionCoefficients = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     Track01Intersections = [\cf5 \strokec5 16\cf0 \strokec4 , \cf5 \strokec5 23\cf0 \strokec4 , \cf5 \strokec5 44\cf0 \strokec4 , \cf5 \strokec5 54\cf0 \strokec4 ]\cb1 \
\cb3     Track10Intersections = [\cf5 \strokec5 33\cf0 \strokec4 , \cf5 \strokec5 50\cf0 \strokec4 , \cf5 \strokec5 89\cf0 \strokec4 , \cf5 \strokec5 106\cf0 \strokec4 ]\cb1 \
\cb3     Track12Intersections = [\cf5 \strokec5 6\cf0 \strokec4 , \cf5 \strokec5 27\cf0 \strokec4 , \cf5 \strokec5 55\cf0 \strokec4 , \cf5 \strokec5 72\cf0 \strokec4 , \cf5 \strokec5 130\cf0 \strokec4 , \cf5 \strokec5 149\cf0 \strokec4 ]\cb1 \
\cb3     Track21Intersections = [\cf5 \strokec5 5\cf0 \strokec4 , \cf5 \strokec5 26\cf0 \strokec4 , \cf5 \strokec5 46\cf0 \strokec4 , \cf5 \strokec5 61\cf0 \strokec4 , \cf5 \strokec5 115\cf0 \strokec4 , \cf5 \strokec5 133\cf0 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  isCountdownTimerRunning():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  countdownTimeRemainingms\cb1 \
\cb3     countdownTimeRemainingms = endTimeOfCurrentStatems - \cf2 \strokec2 input\cf0 \strokec4 .running_time()\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  countdownTimeRemainingms > \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         basic.show_number(Math.\cf2 \strokec2 round\cf0 \strokec4 (countdownTimeRemainingms / \cf5 \strokec5 1000\cf0 \strokec4 ))\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         basic.show_number(\cf5 \strokec5 0\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  on_logo_pressed():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  resetGame\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  stateOfGame == \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3         state0_init()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame >= \cf5 \strokec5 9\cf0 \strokec4 :\cb1 \
\cb3         resetGame = \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 pass\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 input\cf0 \strokec4 .on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)\cb1 \
\
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state9_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  scoreTotal, endTimeOfCurrentStatems, scoreProportionSnake0, scoreProportionSnake1, scoreProportionSnake2, rangeSnake0Proportion, rangeSnake1Proportion, rangeSnake2Proportion, stateOfGame\cb1 \
\cb3     scoreTotal = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3     setTotalScore()\cb1 \
\cb3     endTimeOfCurrentStatems = \cf2 \strokec2 input\cf0 \strokec4 .running_time() + \cf5 \strokec5 2000\cf0 \cb1 \strokec4 \
\cb3     scoreProportionSnake0 = Math.ceil(snakeScore[\cf5 \strokec5 0\cf0 \strokec4 ] / scoreTotal * trackLengths[\cf5 \strokec5 0\cf0 \strokec4 ])\cb1 \
\cb3     scoreProportionSnake1 = Math.ceil(snakeScore[\cf5 \strokec5 1\cf0 \strokec4 ] / scoreTotal * trackLengths[\cf5 \strokec5 0\cf0 \strokec4 ])\cb1 \
\cb3     scoreProportionSnake2 = Math.ceil(snakeScore[\cf5 \strokec5 2\cf0 \strokec4 ] / scoreTotal * trackLengths[\cf5 \strokec5 0\cf0 \strokec4 ])\cb1 \
\cb3     rangeSnake0Proportion = strip0.\cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 0\cf0 \strokec4 , scoreProportionSnake0)\cb1 \
\cb3     basic.show_number(getWinner())\cb1 \
\cb3     rangeSnake1Proportion = strip0.\cf2 \strokec2 range\cf0 \strokec4 (scoreProportionSnake0, scoreProportionSnake1)\cb1 \
\cb3     rangeSnake2Proportion = strip0.\cf2 \strokec2 range\cf0 \strokec4 (scoreProportionSnake0 + scoreProportionSnake1,\cb1 \
\cb3         scoreProportionSnake2)\cb1 \
\cb3     stateOfGame = \cf5 \strokec5 9\cf0 \cb1 \strokec4 \
\cb3     strip0.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\cb3     strip1.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\cb3     strip2.show_color(neopixel.colors(NeoPixelColors.BLACK))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state5_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  countdownTimeRemainingms, stateOfGame\cb1 \
\cb3     countdownTimeRemainingms = endTimeOfCurrentStatems - \cf2 \strokec2 input\cf0 \strokec4 .running_time()\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  countdownTimeRemainingms > interRoundTimerLengthsecs * \cf5 \strokec5 1000\cf0 \strokec4 :\cb1 \
\cb3         flashWinningSnake()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  countdownTimeRemainingms >= \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         showCountdownTimer()\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         basic.clear_screen()\cb1 \
\cb3         state3_init()\cb1 \
\cb3         stateOfGame = \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state3_run():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  currentTotalSnakesAlive() <= \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         state9_init()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  state2_init():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  snakeLength, snakeCanScoreLeft, snakeCanScoreRight, snakeTrack, snakeIsAlive, stateOfGame\cb1 \
\cb3     snakeIcon()\cb1 \
\cb3     snakeLength = [\cf5 \strokec5 8\cf0 \strokec4 , \cf5 \strokec5 8\cf0 \strokec4 , \cf5 \strokec5 5\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreLeft = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeCanScoreRight = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     snakeTrack = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 2\cf0 \strokec4 , \cf5 \strokec5 0\cf0 \strokec4 ]\cb1 \
\cb3     snakeIsAlive = [\cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 , \cf5 \strokec5 1\cf0 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  index7 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf5 \strokec5 3\cf0 \strokec4 ):\cb1 \
\cb3         spawnSnake(index7)\cb1 \
\cb3         showSnake(index7)\cb1 \
\cb3     stateOfGame = \cf5 \strokec5 2\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # movment value is converted to direction by simply determining if it was positive or negative...\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # positive movement -> direction = 1\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # negative movement -> direction = -1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  convertMovementToDirection(num: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  num > \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 # This function is used to adjust snakes' positionOfHead, direction, and growth based on the passed parameters of snakeIndex and movement...\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # Movement values translate to\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # -3 = fast move left\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # -2 = medium move left\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # -1 = slow move left\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 0 = no movement\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 1 = slow move right\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 2 = medium move right\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 # 3 = fast move right\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  onCommandReceived(snakeIndex7: number, movement: number):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 global\cf0 \strokec4  lastDirection, newDirection, currentSnakeLength, currentSnakePositionOfHead, blockingSnakeIndex\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  stateOfGame >= \cf5 \strokec5 1\cf0 \strokec4  \cf2 \strokec2 and\cf0 \strokec4  stateOfGame <= \cf5 \strokec5 3\cf0 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 # Check to see if the controller has sent movement date for a snake that is dead.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # If dead, return -1 (to avoid processing commands)\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # If alive, then process the command\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[snakeIndex7] == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3         lastDirection = snakeDirection[snakeIndex7]\cb1 \
\cb3         newDirection = convertMovementToDirection(movement)\cb1 \
\cb3         \cf7 \strokec7 # We are using the movement parameter for TWO things...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 1. Direction\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 2. Magnitude of movement\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Compare the lastDirection the snake was moving (stored in snakeDirection array) to the newDirection returned by passing movement parameter from onCommandReceived into conventMovementToDirection function.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # If direction has changed TWO things need to happen...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 1. Set the newDirection into snakeDirection array.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 2. The head flips to the other side of the snake when direction changes. To accomplish this we set 2 temp variables (currentSnakeLength and currentSnake Position). These are used to calculate and set the new snakePositionOfHead at the opposite side of the snake, thus we need to know where the head is and how long the snake currently is.\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  lastDirection != newDirection:\cb1 \
\cb3             snakeDirection[snakeIndex7] = newDirection\cb1 \
\cb3             \cf7 \strokec7 # temp variables of currentSnakeLength and currentSnakePosition make is easier to calculate the snake's new positionOfHead depended on whether the snake is changing direction or not.\cf0 \cb1 \strokec4 \
\cb3             currentSnakeLength = snakeLength[snakeIndex7]\cb1 \
\cb3             currentSnakePositionOfHead = snakePositionOfHead[snakeIndex7]\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  lastDirection == \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving LEFT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving LEFT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving LEFT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving LEFT\cf0 \cb1 \strokec4 \
\cb3                 snakePositionOfHead[snakeIndex7] = currentSnakePositionOfHead + currentSnakeLength - \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving RIGHT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving RIGHT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving RIGHT\cf0 \cb1 \strokec4 \
\cb3                 \cf7 \strokec7 # set snake's positionOfHead if it was moving RIGHT\cf0 \cb1 \strokec4 \
\cb3                 snakePositionOfHead[snakeIndex7] = currentSnakePositionOfHead - currentSnakeLength + \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # Magnitude = absolute value of the movement parameter\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # We loop through the next section for each pixel we WANT to TRY to move (based on Magnitude of the movement). There is no guarantee that there is enough space on the strip for a snake to move 3 spaces, but it might be able to move 1 or 2 spaces.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # By running through this section step-by-step we can...\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 1. Check to see if the snake can move to an open space and call the moveSnake function.\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 # 2. Check to see if the snake is at the end of the strip and can score at that end of the strip. (The snake can only score/grow at an end of the strip that it hasn't scored at last time is scored). If it should score/grow we call growSnake\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  index8 \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf2 \strokec2 abs\cf0 \strokec4 (movement)):\cb1 \
\cb3             \cf7 \strokec7 # Checks for direction and to see if snake has room to continue moving in that direction (not at that edge).\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # Movement = - 1 (LEFT)\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # First IF statement is for moving LEFT and checks position 0 to see if their is room to move.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # ELSE IF snake is already at LEFT edge AND the snake can score on the LEFT -> growSnake. Set CanScoreLeft to 0 and toggle CanScoreRight to 1.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # \cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # Movement = 1 (RIGHT)\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # First IF statement is for moving RIGHT and checks position at far right of the track to see if their is room to move.\cf0 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 # ELSE IF snake is already at RIGHT edge AND the snake can score on the RIGHT -> growSnake. Set CanScoreLeft to 1 and toggle CanScoreRight to 0.\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  newDirection == \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[snakeIndex7] != \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3                     moveSnake(snakeIndex7)\cb1 \
\cb3                     blockingSnakeIndex = isPixelBlocked(snakePositionOfHead[snakeIndex7], snakeTrack[snakeIndex7])\cb1 \
\cb3                     \cf2 \strokec2 if\cf0 \strokec4  blockingSnakeIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         snakeScore[blockingSnakeIndex] = snakeScore[blockingSnakeIndex] + \cf5 \strokec5 2\cf0 \cb1 \strokec4 \
\cb3                         snakeIsAlive[snakeIndex7] = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3                         snakeFuneral(snakeIndex7)\cb1 \
\cb3                 \cf2 \strokec2 elif\cf0 \strokec4  snakeCanScoreLeft[snakeIndex7] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                     growSnake(snakeIndex7)\cb1 \
\cb3                     snakeCanScoreLeft[snakeIndex7] = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3                     snakeCanScoreRight[snakeIndex7] = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  newDirection == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  snakePositionOfHead[snakeIndex7] != trackLengths[snakeTrack[snakeIndex7]] - \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                     moveSnake(snakeIndex7)\cb1 \
\cb3                     blockingSnakeIndex = isPixelBlocked(snakePositionOfHead[snakeIndex7], snakeTrack[snakeIndex7])\cb1 \
\cb3                     \cf2 \strokec2 if\cf0 \strokec4  blockingSnakeIndex != \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         \cf7 \strokec7 # Add 2 to the score of the blocking snake after a collision has occurred.\cf0 \cb1 \strokec4 \
\cb3                         snakeScore[blockingSnakeIndex] = snakeScore[blockingSnakeIndex] + \cf5 \strokec5 2\cf0 \cb1 \strokec4 \
\cb3                         snakeIsAlive[snakeIndex7] = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3                         snakeFuneral(snakeIndex7)\cb1 \
\cb3                 \cf2 \strokec2 elif\cf0 \strokec4  snakeCanScoreRight[snakeIndex7] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3                     growSnake(snakeIndex7)\cb1 \
\cb3                     snakeCanScoreLeft[snakeIndex7] = \cf5 \strokec5 1\cf0 \cb1 \strokec4 \
\cb3                     snakeCanScoreRight[snakeIndex7] = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  snakeIsAlive[snakeIndex7] == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3             showSnake(snakeIndex7)\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 -1\cf0 \cb1 \strokec4 \
\cb3 currentSnakePositionOfHead = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 currentSnakeLength = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 newDirection = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 lastDirection = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 scoreProportionSnake2 = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 scoreProportionSnake1 = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 scoreProportionSnake0 = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 trackFrictionCoefficients: List[number] = []\cb1 \
\cb3 jumpingSnakeIndex = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 tempPixel = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 index52 = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 snakeIsBlocked = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3 rightEdgeOfSnake = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 leftEdgeOfSnake = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 tempDirection = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 spawnSuccess = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3 trackLengths: List[number] = []\cb1 \
\cb3 lastRoundedSecOnCountdownTimersecs = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 currentRoundedSecOnCountdownTimersecs = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 winningSnake = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 rangeSnake2Proportion: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 rangeSnake1Proportion: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 rangeSnake0Proportion: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 resetGame = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3 Track12Intersections: List[number] = []\cb1 \
\cb3 Track21Intersections: List[number] = []\cb1 \
\cb3 Track10Intersections: List[number] = []\cb1 \
\cb3 blockingSnakeIndex = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 Track01Intersections: List[number] = []\cb1 \
\cb3 currentIntersectionIndex = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 snakeCanScoreRight: List[number] = []\cb1 \
\cb3 snakeCanScoreLeft: List[number] = []\cb1 \
\cb3 flashStatePeriodms = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 numFlashStates = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 snakeDirection: List[number] = []\cb1 \
\cb3 snakeLength: List[number] = []\cb1 \
\cb3 snakePositionOfHead: List[number] = []\cb1 \
\cb3 currentPixel = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 stripArray: List[neopixel.Strip] = []\cb1 \
\cb3 tempTrack = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 scoreTotal = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 snakeIsAlive: List[number] = []\cb1 \
\cb3 snakeTrack: List[number] = []\cb1 \
\cb3 snakeScore: List[number] = []\cb1 \
\cb3 range2: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 endTimeOfCurrentStatems = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 countdownTimeRemainingms = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 strip2: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 strip1: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 strip0: neopixel.Strip = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3 roundWinnerFlashTimesecs = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 interRoundTimerLengthsecs = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 preRoundTimerLengthsecs = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 stateOfGame = \cf5 \strokec5 0\cf0 \cb1 \strokec4 \
\cb3 stateOfGame = \cf5 \strokec5 -2\cf0 \cb1 \strokec4 \
\cb3 preRoundTimerLengthsecs = \cf5 \strokec5 5\cf0 \cb1 \strokec4 \
\cb3 interRoundTimerLengthsecs = \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\cb3 roundWinnerFlashTimesecs = \cf5 \strokec5 3\cf0 \cb1 \strokec4 \
\cb3 radio.set_group(\cf5 \strokec5 200\cf0 \strokec4 )\cb1 \
\cb3 initTracks()\cb1 \
\cb3 initLEDs()\cb1 \
\cb3 state1_init()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  on_forever():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 # State -1 = PreGame LED display\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 0 = Countdown to game round 1.\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 1 = Round 1 of Game\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 2 = Round 2 of Game\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 3 = Round 3 of Game\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 4 = Transition from Round 1 to Round 2\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 5 = Transition from Round 2 to Round 3\cf0 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 # State 9 = Game is over. Show snake proportional bar graph.\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  stateOfGame == \cf5 \strokec5 -1\cf0 \strokec4 :\cb1 \
\cb3         state1_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 0\cf0 \strokec4 :\cb1 \
\cb3         state0_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 1\cf0 \strokec4 :\cb1 \
\cb3         state1_run2()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 2\cf0 \strokec4 :\cb1 \
\cb3         state2_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 3\cf0 \strokec4 :\cb1 \
\cb3         state3_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 4\cf0 \strokec4 :\cb1 \
\cb3         state4_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 5\cf0 \strokec4 :\cb1 \
\cb3         state5_run()\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  stateOfGame == \cf5 \strokec5 9\cf0 \strokec4 :\cb1 \
\cb3         state9_run()\cb1 \
\cb3 basic.forever(on_forever)\cb1 \
\
}