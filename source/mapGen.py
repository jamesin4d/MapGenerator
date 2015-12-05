# Created by a human
# when:
# 12/2/2015
# 10:44 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------

from random import *


class LevelMap(object):
    def __init__(self):
        self.roomsList = []
        self.connectedRoomsList = []

    def generateMap(self, xSize, ySize, allowedFails, pathLength, maxRooms):
        # generate random layout of rooms, corridors and doors
        self.width = xSize
        self.height = ySize
        self.mapArray = []

        for y in range(ySize):
            temp = []
            for x in range(xSize):
                temp.append(1)
            self.mapArray.append(temp)

        width, height, type = self.makeRoom()
        while len(self.roomsList) == 0:
            y = randrange(ySize - 1 - height) + 1
            x = randrange(xSize - 1 - width) + 1
            self.placeRoom(height, width, x, y, xSize, ySize, 6, 0)

        hasFailed = 0

        while hasFailed < allowedFails:  # the lower the allowedFails, the smaller the map
            chooseRoom = randrange(len(self.roomsList))
            ex, ey, ex2, ey2, et = self.makeExit(chooseRoom)
            corridor = randrange(100)
            if corridor < pathLength:
                w, l, t = self.makeCorridor()
            else:
                w, l, t, = self.makeRoom()
            roomDone = self.placeRoom(l, w, ex2, ey2, xSize, ySize, t, et)
            if roomDone == 0:  # If placement failed increase possibility map is full
                hasFailed += 1
            elif roomDone == 2:  # Possiblilty of linking rooms
                if self.mapArray[ey2][ex2] == 0:
                    if randrange(100) < 7:
                        self.makePortal(ex, ey)
                    hasFailed += 1
            else:  # Otherwise, link up the 2 rooms
                self.makePortal(ex, ey)
                hasFailed = 0
                if t < 5:
                    tc = [len(self.roomsList) - 1, ex2, ey2, t]
                    self.connectedRoomsList.append(tc)
                    self.joinCorridor(len(self.roomsList) - 1, ex2, ey2, t, 50)
            if len(self.roomsList) == maxRooms:
                hasFailed = allowedFails
        self.finalJoining()

    def makeRoom(self):
        # Randomly produce room size
        rtype = 1
        rwide = randrange(32) + 3
        rlong = randrange(16) + 3
        return rwide, rlong, rtype

    def placeRoom(self, ll, ww, xposs, yposs, xsize, ysize, rty, ext):
        # Place feature if enough space and return canPlace as true or false
        # Arrange for 'direction'
        xpos = xposs
        ypos = yposs
        if ll < 0:
            ypos += ll + 1
            ll = abs(ll)
        if ww < 0:
            xpos += ww + 1
            ww = abs(ww)
        # Make offset if type is room
        if rty == 5:
            if ext == 0 or ext == 2:
                offset = randrange(ww)
                xpos -= offset
            else:
                offset = randrange(ll)
                ypos -= offset
        # Then check if there is space for the room
        canPlace = 1
        if ww + xpos + 1 > xsize - 1 or ll + ypos + 1 > ysize:
            canPlace = 0
            return canPlace
        elif xpos < 1 or ypos < 1:
            canPlace = 0
            return canPlace
        else:
            for j in range(ll):
                for k in range(ww):
                    if self.mapArray[(ypos) + j][(xpos) + k] != 1:
                        canPlace = 2
        # If there is space, add to list of rooms
        if canPlace == 1:
            temp = [ll, ww, xpos, ypos]
            self.roomsList.append(temp)
            for j in range(ll + 2):  # Then build walls
                for k in range(ww + 2):
                    self.mapArray[(ypos - 1) + j][(xpos - 1) + k] = 2
            for j in range(ll):  # Then build floor
                for k in range(ww):
                    self.mapArray[ypos + j][xpos + k] = 0
        return canPlace  # Return whether placed is true/false

    def makeCorridor(self):
        # Randomly produce corridor length and heading
        corridorLength = randrange(18) + 3
        direction = randrange(4)
        if direction == 0:  # North
            wd = 4
            lg = -corridorLength
        elif direction == 1:  # East
            wd = corridorLength
            lg = 4
        elif direction == 2:  # South
            wd = 4
            lg = corridorLength
        elif direction == 3:  # West
            wd = -corridorLength
            lg = 4
        return wd, lg, direction

    def joinCorridor(self, cno, xp, yp, ed, psb):
        """Check corridor endpoint and make an exit if it links to another room"""
        cArea = self.roomsList[cno]
        if xp != cArea[2] or yp != cArea[3]:  # Find the corridor endpoint
            endx = xp - (cArea[1] - 1)
            endy = yp - (cArea[0] - 1)
        else:
            endx = xp + (cArea[1] - 1)
            endy = yp + (cArea[0] - 1)
        checkExit = []
        if ed == 0:  # North corridor
            if endx > 1:
                coords = [endx - 2, endy, endx - 1, endy]
                checkExit.append(coords)
            if endy > 1:
                coords = [endx, endy - 2, endx, endy - 1]
                checkExit.append(coords)
            if endx < self.width - 2:
                coords = [endx + 2, endy, endx + 1, endy]
                checkExit.append(coords)
        elif ed == 1:  # East corridor
            if endy > 1:
                coords = [endx, endy - 2, endx, endy - 1]
                checkExit.append(coords)
            if endx < self.width - 2:
                coords = [endx + 2, endy, endx + 1, endy]
                checkExit.append(coords)
            if endy < self.height - 2:
                coords = [endx, endy + 2, endx, endy + 1]
                checkExit.append(coords)
        elif ed == 2:  # South corridor
            if endx < self.width - 2:
                coords = [endx + 2, endy, endx + 1, endy]
                checkExit.append(coords)
            if endy < self.height - 2:
                coords = [endx, endy + 2, endx, endy + 1]
                checkExit.append(coords)
            if endx > 1:
                coords = [endx - 2, endy, endx - 1, endy]
                checkExit.append(coords)
        elif ed == 3:  # West corridor
            if endx > 1:
                coords = [endx - 2, endy, endx - 1, endy]
                checkExit.append(coords)
            if endy > 1:
                coords = [endx, endy - 2, endx, endy - 1]
                checkExit.append(coords)
            if endy < self.height - 2:
                coords = [endx, endy + 2, endx, endy + 1]
                checkExit.append(coords)
        for xxx, yyy, xxx1, yyy1 in checkExit:  # Loop through possible exits
            if self.mapArray[yyy][xxx] == 0:  # If joins to a room
                if randrange(100) < psb:  # Possibility of linking rooms
                    self.makePortal(xxx1, yyy1)

    def makeExit(self, rn):
        # picks a random wall and a random spot on that wall
        room = self.roomsList[rn]
        while True:
            rw = randrange(4)
            if rw == 0:  # North wall
                rx = randrange(room[1]) + room[2]
                ry = room[3] - 1
                rx2 = rx
                ry2 = ry - 1
            elif rw == 1:  # East wall
                ry = randrange(room[0]) + room[3]
                rx = room[2] + room[1]
                rx2 = rx + 1
                ry2 = ry
            elif rw == 2:  # South wall
                rx = randrange(room[1]) + room[2]
                ry = room[3] + room[0]
                rx2 = rx
                ry2 = ry + 1
            elif rw == 3:  # West wall
                ry = randrange(room[0]) + room[3]
                rx = room[2] - 1
                rx2 = rx - 1
                ry2 = ry
            if self.mapArray[ry][rx] == 2:
                break  # If space is a wall, exit
        return rx, ry, rx2, ry2, rw

    def makePortal(self, px, py):
        # Creates doors in walls, yalls
        ptype = randrange(100)
        if ptype > 90:  # Secret door
            self.mapArray[py][px] = 5
            return
        if ptype > 75:  # Closed door
            self.mapArray[py][px] = 4
            return
        elif ptype > 40:  # Open door
            self.mapArray[py][px] = 3
            return
        else:  # Hole in the wall
            self.mapArray[py][px] = 0

    def finalJoining(self):
        for x in self.connectedRoomsList:  # loops through all corridors to see if any can be
            self.joinCorridor(x[0], x[1], x[2], x[3], 10)  # joined to other rooms


"""
mw = 40
mh =30
maxFails = 400
amtC = 74
amtR = 50

m = LevelMap()
m.generateMap(mw,mh,maxFails,amtC,amtR)

for y in range(mh):
    l = ""
    for x in range(mw):
        if m.mapArray[y][x] == 0:
            l += " "
        if m.mapArray[y][x] == 1:
            l += "."
        if m.mapArray[y][x] == 2:
            l += "#"
        if m.mapArray[y][x] == 3 or m.mapArray[y][x] == 4 or m.mapArray[y][x] == 5:
            l += "+"

    #print l

"""
