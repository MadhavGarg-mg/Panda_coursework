from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

import simpleaudio as sa

# Add music
wave_obj = sa.WaveObject.from_wave_file("panda_power.wav")
play_obj = wave_obj.play()


class WalkingPanda(ShowBase):
    def __init__(self, scale, move_side, move, fly, rotate_speed, zoom, no_walk=False, hexagon=False, no_rotate=False):
        ShowBase.__init__(self)

        self.no_rotate = no_rotate
        self.rotate_speed = rotate_speed
        self.zoom = zoom
        self.no_walk = no_walk
        self.hexagon = hexagon

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8 + move_side, 42 + move, 0 - fly)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005 * scale, 0.005 * scale, 0.005 * scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        if not self.no_walk:
            self.pandaActor.loop("walk")

        if self.hexagon:
            move0 = self.pandaActor.posInterval(0 * scale, Point3(1.9, 3, 0), startPos=Point3(1.9, 3, 0))
            move1 = self.pandaActor.posInterval(2 * scale, Point3(-1.9, 3, 0), startPos=Point3(1.9, 3, 0))
            move2 = self.pandaActor.posInterval(2 * scale, Point3(-3.5, 0, 0), startPos=Point3(-1.9, 3, 0))
            move3 = self.pandaActor.posInterval(2 * scale, Point3(-1.9, -3, 0), startPos=Point3(-3.5, 0, 0))
            move4 = self.pandaActor.posInterval(2 * scale, Point3(1.9, -3, 0), startPos=Point3(-1.9, -3, 0))
            move5 = self.pandaActor.posInterval(2 * scale, Point3(3.5, 0, 0), startPos=Point3(1.9, -3, 0))
            move6 = self.pandaActor.posInterval(2 * scale, Point3(1.9, 3, 0), startPos=Point3(3.5, 0, 0))

            turn0 = self.pandaActor.hprInterval(0 * scale, Point3(270, 0, 0), startHpr=Point3(270, 0, 0))
            turn1 = self.pandaActor.hprInterval(2 * scale, Point3(330, 0, 0), startHpr=Point3(270, 0, 0))
            turn2 = self.pandaActor.hprInterval(2 * scale, Point3(390, 0, 0), startHpr=Point3(330, 0, 0))
            turn3 = self.pandaActor.hprInterval(2 * scale, Point3(450, 0, 0), startHpr=Point3(390, 0, 0))
            turn4 = self.pandaActor.hprInterval(2 * scale, Point3(510, 0, 0), startHpr=Point3(450, 0, 0))
            turn5 = self.pandaActor.hprInterval(2 * scale, Point3(570, 0, 0), startHpr=Point3(510, 0, 0))
            turn6 = self.pandaActor.hprInterval(2 * scale, Point3(630, 0, 0), startHpr=Point3(570, 0, 0))

            self.pandaPace = Sequence(move0, turn0, move1, turn1, move2, turn2, move3, turn3, move4, turn4,
                                      move5, turn5, move6, turn6, name="pandaPace")  # Gives the panda coordinates.
            self.pandaPace.loop()  # Loops panda continuously.

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        if not self.no_rotate:
            angleDegrees = task.time * 6.0 * self.rotate_speed
            angleRadians = angleDegrees * (pi / 180.0)
        else:
            angleDegrees = 0
            angleRadians = 0
        self.camera.setPos(20 * 1 / self.zoom * sin(angleRadians), -20.0 * 1 / self.zoom * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
