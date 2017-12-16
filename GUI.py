from tkinter import *

import randomWalk
from randomWalk import *

personNum = 3
frameNum = 50
iterationTime = 1
viewHeight = 1080
viewWidth = 1980
minSpeed = 10
maxSpeed = 20
walkingDirectionRange = [-90, 450]
cameraHeight = 100
cameraDistance = 100

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("PoseSimulator")
        master.minsize(width=666, height=666)

        self.personNumLabel = Label(master, text = "Person Number: ")
        self.personNumLabel.place(x=10, y=10)
        self.personNumEntry = Entry(master, width = 5)
        self.personNumEntry.insert(0, "3")
        self.personNumEntry.place(x=120, y=10)

        self.frameNumLabel = Label(master, text="Frame Number: ")
        self.frameNumLabel.place(x=10, y=40)
        self.frameNumEntry = Entry(master, width=5)
        self.frameNumEntry.insert(0, "50")
        self.frameNumEntry.place(x=120, y=40)

        self.iterationLabel = Label(master, text="Iteration: ")
        self.iterationLabel.place(x=10, y=70)
        self.iterationEntry = Entry(master, width=5)
        self.iterationEntry.insert(0, "1000")
        self.iterationEntry.place(x=120, y=70)

        self.viewWidthLabel = Label(master, text="View Width: ")
        self.viewWidthLabel.place(x=10, y=100)
        self.viewWidthEntry = Entry(master, width=5)
        self.viewWidthEntry.insert(0, "1980")
        self.viewWidthEntry.place(x=120, y=100)

        self.viewHeightLabel = Label(master, text="View Height: ")
        self.viewHeightLabel.place(x=10, y=130)
        self.viewHeightEntry = Entry(master, width=5)
        self.viewHeightEntry.insert(0, "1080")
        self.viewHeightEntry.place(x=120, y=130)

        #

        self.speedRangeLabel = Label(master, text="Speed Range: ")
        self.speedRangeLabel.place(x=310, y=10)
        self.minSpeed = Entry(master, width=5)
        self.minSpeed.insert(0, "10")
        self.minSpeed.place(x=420, y=10)
        self.maxSpeed = Entry(master, width=5)
        self.maxSpeed.insert(0, "20")
        self.maxSpeed.place(x=480, y=10)

        self.walkingDirectionRangeLabel = Label(master, text="Direction Changing Range: ")
        self.walkingDirectionRangeLabel.place(x=310, y=40)
        self.minAngle = Entry(master, width=5)
        self.minAngle.insert(0, "-90")
        self.minAngle.place(x=420, y=70)
        self.maxAngle = Entry(master, width=5)
        self.maxAngle.insert(0, "90")
        self.maxAngle.place(x=480, y=70)

        self.cameraWidthLabel = Label(master, text="Camera Width: ")
        self.cameraWidthLabel.place(x=310, y=100)
        self.cameraWidthEntry = Entry(master, width=5)
        self.cameraWidthEntry.insert(0, "100")
        self.cameraWidthEntry.place(x=420, y=100)

        self.cameraHeightLabel = Label(master, text="Camera Height: ")
        self.cameraHeightLabel.place(x=310, y=130)
        self.cameraHeightEntry = Entry(master, width=5)
        self.cameraHeightEntry.insert(0, "100")
        self.cameraHeightEntry.place(x=420, y=130)

        self.greet_button = Button(master, text="Random Walk", command=self.generateRandomPose)
        self.greet_button.place(x=50, y=300)

        self.generate_button = Button(master, text="Naive Random Walk", command=self.generateNaiveRandomPose)
        self.generate_button.place(x=50, y=330)

        self.generate_button = Button(master, text="Noise Random Walk", command=self.generateNoiseRandomPose)
        self.generate_button.place(x=50, y=360)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x=50, y=390)

    def greet(self):
        print("Greetings!")

    def generateRandomPose(self):
        personNum = int(self.personNumEntry.get())
        frameNum = int(self.frameNumEntry.get())
        iterationTime = int(self.iterationEntry.get())
        viewHeight = float(self.viewHeightEntry.get())
        viewWidth = float(self.viewHeightEntry.get())
        minSpeed = float(self.minSpeed.get())
        maxSpeed = float(self.maxSpeed.get())
        walkingDirectionRangeMin = float(self.minAngle.get())
        walkingDirectionRangeMax = float(self.maxAngle.get())
        cameraHeight = float(self.cameraHeightEntry.get())
        cameraDistance = float(self.cameraWidthEntry.get())
        randomWalk.run(frameNum, iterationTime, cameraHeight, cameraDistance, viewHeight, viewWidth, minSpeed, maxSpeed,
                       walkingDirectionRangeMin, walkingDirectionRangeMax, personNum)

    def generateNaiveRandomPose(self):
        personNum = int(self.personNumEntry.get())
        frameNum = int(self.frameNumEntry.get())
        iterationTime = int(self.iterationEntry.get())
        viewHeight = float(self.viewHeightEntry.get())
        viewWidth = float(self.viewHeightEntry.get())
        minSpeed = float(self.minSpeed.get())
        maxSpeed = float(self.maxSpeed.get())
        walkingDirectionRangeMin = float(self.minAngle.get())
        walkingDirectionRangeMax = float(self.maxAngle.get())
        cameraHeight = float(self.cameraHeightEntry.get())
        cameraDistance = float(self.cameraWidthEntry.get())
        randomWalk.run(frameNum, iterationTime, cameraHeight, cameraDistance, viewHeight, viewWidth, minSpeed, maxSpeed,
                       walkingDirectionRangeMin, walkingDirectionRangeMax, personNum)

    def generateNoiseRandomPose(self):
        personNum = int(self.personNumEntry.get())
        frameNum = int(self.frameNumEntry.get())
        iterationTime = int(self.iterationEntry.get())
        viewHeight = float(self.viewHeightEntry.get())
        viewWidth = float(self.viewHeightEntry.get())
        minSpeed = float(self.minSpeed.get())
        maxSpeed = float(self.maxSpeed.get())
        walkingDirectionRangeMin = float(self.minAngle.get())
        walkingDirectionRangeMax = float(self.maxAngle.get())
        cameraHeight = float(self.cameraHeightEntry.get())
        cameraDistance = float(self.cameraWidthEntry.get())
        randomWalk.run(frameNum, iterationTime, cameraHeight, cameraDistance, viewHeight, viewWidth, minSpeed, maxSpeed,
                       walkingDirectionRangeMin, walkingDirectionRangeMax, personNum)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()