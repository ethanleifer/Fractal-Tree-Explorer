"""
File Name: FractalTreeExplorerV1
Project: Fractal Tree Explorer
Made By: Ethan Leifer
Original Dependencies: DEgraphics.py, fractUtils.py (both in this directory)
Description:

"""

# imports

from DEgraphics import *
from NLDUtils import *
import fractUtils
from math import cos, radians, sin
from random import random, randrange, uniform


win = DEGraphWin(title='Koch Curve Explorer Window', hBGColor='black', width=800, height=800)
gui = DEGraphWin(title='GUI', width=600, height=500, offsets=[win.width, 0], defCoords=[0, 0, 8, 7], hBGColor='black')
gui.displayGrid()


# CONSTANTS

# font used on gui's
FONT = 'helvetica'

# global variables
buttonsActive = False # to manage the activating and deactivating of buttons

# create gui

# title text object
txtTitle = Text(Point(4, 6.5), "Fractal Tree Explorer")
txtTitle.setFace(FONT)
txtTitle.setSize(30)
txtTitle.draw(gui)

# main buttons
btnExit = SimpleButton(win=gui, topLeft=Point(.1, .9), width=1.8, height=.8, label='EXIT', font=(FONT, 35),
                       buttonColor='red', )
btnDraw = SimpleButton(win=gui, topLeft=Point(4.1, .9), width=1.8, height=.8, label="DRAW", font=(FONT, 25),
                       buttonColor='blue', textColor='white')
btnClear = SimpleButton(win=gui, topLeft=Point(6.1, .9), width=1.8, height=.8, label="CLEAR", font=(FONT, 25),
                        buttonColor='blue', textColor='white')
btnZoomIn = SimpleButton(win=gui, topLeft=Point(.1, 1.9), width=1.8, height=.8, label="ZOOM\nIN", font=(FONT, 20),
                         buttonColor='blue', textColor='white')
btnZoomOut = SimpleButton(win=gui, topLeft=Point(2.1, 1.9), width=1.8, height=.8, label="ZOOM\nOUT", font=(FONT, 20),
                          buttonColor='blue', textColor='white')
resetToDefault = SimpleButton(win=gui, topLeft=Point(2.1, .9), width=1.8, height=.8, label="RESET TO\nDEFAULT", font=(FONT, 20), buttonColor='blue', textColor='white')


# levels entry
entLevels = IntEntry(Point(5, 1.25), width=10, span=[0, 15])
entLevels.draw(gui)
entLevels.setFace(FONT)
btnEnterLevels = SimpleButton(gui, topLeft=Point(6.1, 1.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtLevels = Text(Point(5, 1.75), "# of Levels = ")
txtLevels.setFace(FONT)
txtLevels.draw(gui)

# intialLength entry
entIntialLength = DblEntry(Point(5, 2.25), width=10, span=[0, 10])
entIntialLength.draw(gui)
entIntialLength.setFace(FONT)
btnIntialLength = SimpleButton(gui, topLeft=Point(6.1, 2.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtIntialLength = Text(Point(5, 2.75), "Intial Length = ")
txtIntialLength.setFace(FONT)
txtIntialLength.draw(gui)

# scale Factor entry
entScaleFactor = DblEntry(Point(5, 3.25), width=10, span=[0, 2])
entScaleFactor.draw(gui)
entScaleFactor.setFace(FONT)
btnScaleFactor = SimpleButton(gui, topLeft=Point(6.1, 3.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtScaleFactor = Text(Point(5, 3.75), "Scale Factor = ")
txtScaleFactor.setFace(FONT)
txtScaleFactor.draw(gui)

# scale Factor randomness entry
entScaleFactorRandomness = DblEntry(Point(1, 3.25), width=10, span=[0, 1])
entScaleFactorRandomness.draw(gui)
entScaleFactorRandomness.setFace(FONT)
btnScaleFactorRandomness = SimpleButton(gui, topLeft=Point(2.1, 3.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtScaleFactorRandomness = Text(Point(1, 3.75), "Scale Factor\nRandomess = +- ")
txtScaleFactorRandomness.setFace(FONT)
txtScaleFactorRandomness.draw(gui)


# probability it will draw entry
entProbDraw = IntEntry(Point(1, 2.25), width=10, span=[0, 100])
entProbDraw.draw(gui)
entProbDraw.setFace(FONT)
btnProbDraw = SimpleButton(gui, topLeft=Point(2.1, 2.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtProbDraw = Text(Point(1, 2.75), "probability of Branch\nDrawing = ")
txtProbDraw.setFace(FONT)
txtProbDraw.draw(gui)

# angle entry
entTheta = DblEntry(Point(5, 4.25), width=10, span=[0, 90])
entTheta.draw(gui)
entTheta.setFace(FONT)
btnTheta = SimpleButton(gui, topLeft=Point(6.1, 4.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtTheta = Text(Point(5, 4.75), "Branch Angle = ")
txtTheta.setFace(FONT)
txtTheta.draw(gui)

# angle randomness entry
entThetaRandomness = DblEntry(Point(1, 4.25), width=10, span=[0, 45])
entThetaRandomness.draw(gui)
entThetaRandomness.setFace(FONT)
btnThetaRandomness = SimpleButton(gui, topLeft=Point(2.1, 4.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtThetaRandomness = Text(Point(1, 4.75), "Branch Angle\nRandomness = +-")
txtThetaRandomness.setFace(FONT)
txtThetaRandomness.draw(gui)

#Leaf Color

txtLeafColor = Text(Point(1, 5.75), "Leaf Color:")
txtLeafColor.setFace(FONT)
txtLeafColor.setSize(15)
txtLeafColor.draw(gui)

btnLeafColorGreen = SimpleButton(gui, topLeft=Point(0.05, 5.5), width=.4, height=.4, label="", buttonColor="Green",
                                 edgeColor="Black", edgeWidth=2)
btnLeafColorBrown = SimpleButton(gui, topLeft=Point(0.55, 5.5), width=.4, height=.4, label="", buttonColor="Brown",
                                 edgeColor="Black", edgeWidth=2)
btnLeafColorOrange = SimpleButton(gui, topLeft=Point(1.05, 5.5), width=.4, height=.4, label="", buttonColor="Orange",
                                 edgeColor="Black", edgeWidth=2)
btnLeafColorRed = SimpleButton(gui, topLeft=Point(1.55, 5.5), width=.4, height=.4, label="", buttonColor="Red",
                                 edgeColor="Black", edgeWidth=2)
leafColorBtns = [btnLeafColorGreen, btnLeafColorBrown, btnLeafColorRed, btnLeafColorOrange]
leafColorOptions = ["Green", "Brown", "Red", "Orange"]

# Background Color

txtBackgroundColor = Text(Point(3, 5.75), "Background Color:")
txtBackgroundColor.setFace(FONT)
txtBackgroundColor.setSize(15)
txtBackgroundColor.draw(gui)

btnBackgroundColorWhite = SimpleButton(gui, topLeft=Point(2.05, 5.5), width=.6, height=.4, label="", buttonColor="White",
                                 edgeColor="Black", edgeWidth=2)
btnBackgroundColorBlack = SimpleButton(gui, topLeft=Point(2.7, 5.5), width=.6, height=.4, label="", buttonColor="Black",
                                 edgeColor="Black", edgeWidth=2)
btnBackgroundColorLightBlue = SimpleButton(gui, topLeft=Point(3.35, 5.5), width=.6, height=.4, label="", buttonColor="Light Blue",
                                 edgeColor="Black", edgeWidth=2)
backgroundColorBtns = [btnBackgroundColorWhite, btnBackgroundColorBlack, btnBackgroundColorLightBlue]
bacnkgroundColorOptions = ["White", "Black", "Light Blue"]

# Number of Levels that are considered a leaf  entry
entLeafLevels = IntEntry(Point(5, 5.25), width=10, span=[0, 5])
entLeafLevels.draw(gui)
entLeafLevels.setFace(FONT)
btnLeafLevels = SimpleButton(gui, topLeft=Point(6.1, 5.9), width=1.8, height=.8, label="Enter", font=(FONT, 15),
                              buttonColor='blue', textColor='white')
txtLeafLevels = Text(Point(5, 5.75), "# of Levels\nconsidered a leaf = ")
txtLeafLevels.setFace(FONT)
txtLeafLevels.draw(gui)


# alpha is between 0 and 1
# branch angle is between 0 and 360?

class FractalTree():

    def __init__(self, win, L0, scaleFactor, p, intialAngle, theta, levels):

        self.win = win
        self.intialLength = L0
        self.scaleFactor = scaleFactor
        self.scaleFactorRandomness = 0
        self.intialPoint = p
        self.intialAngle = intialAngle
        self.branchAngle = theta
        self.branchRandomness = 0
        self.maxLevels = levels

        self.lines = []
        self.lineThickness = 3

        self.probDraw = 1
        self.trunkColor = "burlywood4"
        self.leafColor = "Green"

        # this is the number of levels that considered part of the "leaf". I think 2 or 3 looks the best
        self.numLevelsConsideredLeafs = 2

        self.isDrawn = False



    def generateFractalTreeManager(self):
        self.lines = []
        self.generateFractalTree(0, self.intialAngle, self.branchAngle, self.intialPoint.clone(), self.intialLength,
                                 self.scaleFactor, self.trunkColor)

    def generateFractalTree(self, levels, intialAngle, theta, p, length, scaleFactor, color):

        if levels >= self.maxLevels-self.numLevelsConsideredLeafs:
            color = self.leafColor
        # base case
        self.lines.append(fractUtils.drawLine(self.win, p, intialAngle, length, lineThickness=self.lineThickness,
                                   lineColor=color))
        if levels < self.maxLevels:
            if self.probDraw > random():
                p1 = p.clone()
                # adds randomness to scale factor and theta
                sf = scaleFactor + uniform( -self.scaleFactorRandomness, self.scaleFactorRandomness)
                t = theta + uniform( -self.branchRandomness, self.branchRandomness)
                self.generateFractalTree(levels + 1, t + intialAngle, t, p1, length * sf, sf, self.trunkColor)
            if self.probDraw > random():
                p2 = p.clone()
                sf = scaleFactor + uniform( -self.scaleFactorRandomness, self.scaleFactorRandomness)
                t = theta + uniform(-self.branchRandomness, self.branchRandomness)
                self.generateFractalTree(levels + 1, intialAngle - t, t, p2, length * sf, sf, self.trunkColor)

    def drawFractalTree(self):
        for l in self.lines:
            l.draw(self.win)

        self.isDrawn = True

    def undrawFractalTree(self):
        for l in self.lines:
            l.undraw()

        self.isDrawn = False

    def setTrunkColor(self, lineColor):
        self.trunkColor = lineColor

    def setLeafColor(self, leafColor):
        self.leafColor = leafColor

def changeActivationButtons():
    global buttonsActive

    if buttonsActive:
        btnExit.deactivate()
        btnClear.deactivate()
        btnDraw.deactivate()
        btnZoomIn.deactivate()
        btnZoomOut.deactivate()
        btnEnterLevels.deactivate()
        btnIntialLength.deactivate()
        btnProbDraw.deactivate()
        btnScaleFactor.deactivate()
        btnScaleFactorRandomness.deactivate()
        btnTheta.deactivate()
        btnThetaRandomness.deactivate()
        resetToDefault.deactivate()
        btnLeafLevels.deactivate()
        for btn in leafColorBtns:
            btn.deactivate()
        for btn in backgroundColorBtns:
            btn.deactivate()

    else:
        btnExit.activate()
        btnClear.activate()
        btnDraw.activate()
        btnZoomIn.activate()
        btnZoomOut.activate()
        btnEnterLevels.activate()
        btnIntialLength.activate()
        btnProbDraw.activate()
        btnScaleFactor.activate()
        btnScaleFactorRandomness.activate()
        btnTheta.activate()
        btnThetaRandomness.activate()
        resetToDefault.activate()
        btnLeafLevels.activate()
        for btn in leafColorBtns:
            btn.activate()
        for btn in backgroundColorBtns:
             btn.activate()


    buttonsActive = not(buttonsActive)

def updateTextBoxes(ft):
    txtLevels.setText("Levels: " + str(ft.maxLevels))
    txtIntialLength.setText("Intial Length: " + str(ft.intialLength))
    txtProbDraw.setText("Probability of Branch\nDrawing = " + str(ft.probDraw*100) + "%")
    txtScaleFactor.setText("Scale Factor = " + str(ft.scaleFactor))
    txtScaleFactorRandomness.setText("Scale Factor\nRandomess = +- " + str(ft.scaleFactorRandomness))
    txtTheta.setText("Branch Angle = " + str(ft.branchAngle))
    txtThetaRandomness.setText("Branch Angle\nRandomness = +-" + str(ft.branchRandomness))
    txtLeafLevels.setText("# of Levels\nconsidered a leaf = " + str(ft.numLevelsConsideredLeafs))

def redrawIfDrawn(ft):
    if ft.isDrawn:
        ft.undrawFractalTree()
        ft.generateFractalTreeManager()
        ft.drawFractalTree()

def main():
    global lineColorBtns, backgroundColorBtns, colorList

    ft = FractalTree(win, 5, .7, Point(0, -8), 90, 30, 8)
    grassRect = Rectangle(Point(-10,-6), Point(10,-10))
    grassRect.setFill("Green")
    grassRect.draw(win)

    changeActivationButtons()
    firstTime = True
    clickPoint = Point(100, 100)

    currentLeafClicked = btnLeafColorGreen
    currentBackgroundClicked = btnBackgroundColorWhite

    updateTextBoxes(ft)

    while not (btnExit.clicked(clickPoint)):
        if btnDraw.clicked(clickPoint) or firstTime:
            # update and draw a Fractal Tree

            # NOTE: I dont allow the drawining of multiple trees,
            # so I force the user to clear the window before they can redraw it
            if not (ft.isDrawn):
                 ft.generateFractalTreeManager()
                 ft.drawFractalTree()
            btnDraw.deactivate()
            btnClear.activate()

        if btnClear.clicked(clickPoint):
            # undraw the Fractal Tree
            ft.undrawFractalTree()
            btnDraw.activate()
            btnClear.deactivate()

        if btnEnterLevels.clicked(clickPoint):
            ft.maxLevels = entLevels.getValue()

        if btnIntialLength.clicked(clickPoint):
            ft.intialLength = entIntialLength.getValue()

        if btnProbDraw.clicked(clickPoint):
            ft.probDraw = entProbDraw.getValue()/100

        if btnScaleFactor.clicked(clickPoint):
            ft.scaleFactor = entScaleFactor.getValue()

        if btnScaleFactorRandomness.clicked(clickPoint):
            ft.scaleFactorRandomness = entScaleFactorRandomness.getValue()

        if btnTheta.clicked(clickPoint):
            ft.branchAngle = entTheta.getValue()

        if btnThetaRandomness.clicked(clickPoint):
            ft.branchRandomness = entThetaRandomness.getValue()

        if btnLeafLevels.clicked(clickPoint):
            ft.numLevelsConsideredLeafs = entLeafLevels.getValue()

        # reset values to the defaults
        if resetToDefault.clicked(clickPoint):
            ft.intialLength = 5
            ft.scaleFactor = .7
            ft.scaleFactorRandomness = 0
            ft.branchAngle = 30
            ft.branchRandomness = 0
            ft.maxLevels = 8
            ft.probDraw = 1
            ft.numLevelsConsideredLeafs = 2

        # let the user click the color buttons and then change the colors in the window
        for i in range(0, len(leafColorBtns)):
            if leafColorBtns[i].clicked(clickPoint):
                ft.setLeafColor(leafColorOptions[i])
                leafColorBtns[i].setEdgeColor("Light Green")
                currentLeafClicked.setEdgeColor("Black")
                currentLeafClicked = leafColorBtns[i]
                redrawIfDrawn(ft)

        for i in range(0, len(backgroundColorBtns)):
            if backgroundColorBtns[i].clicked(clickPoint):
                win.setBackground(bacnkgroundColorOptions[i])
                backgroundColorBtns[i].setEdgeColor("Light Green")
                currentBackgroundClicked.setEdgeColor("Black")
                currentBackgroundClicked = backgroundColorBtns[i]
                redrawIfDrawn(ft)

        # let the user zoom in and out
        if btnZoomIn.clicked(clickPoint):
            win.zoom("in", keepRatio=True)

        if btnZoomOut.clicked(clickPoint):
            win.zoom("out", keepRatio=True)

        firstTime = False
        updateTextBoxes(ft)
        clickPoint = gui.getMouse()

if __name__ == "__main__":
    main()