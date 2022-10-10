from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("panda_power.wav")
play_obj = wave_obj.play()


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate, scale, move_side, move, fly, rotate_speed, zoom, no_walk):
        ShowBase.__init__(self)

        self.no_rotate = no_rotate
        self.rotate_speed = rotate_speed
        self.zoom = zoom
        self.no_walk = no_walk
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

        posInterval1 = self.pandaActor.posInterval(1,
                                                   Point3(1.9, 3, 0),
                                                   startPos=Point3(3.5, 0, 0))
        posInterval2 = self.pandaActor.posInterval(1,
                                                   Point3(-1.9, 3, 0),
                                                   startPos=Point3(1.9, 3, 0))
        posInterval3 = self.pandaActor.posInterval(1,
                                                   Point3(-3.5, 0, 0),
                                                   startPos=Point3(-1.9, 3, 0))
        posInterval4 = self.pandaActor.posInterval(1,
                                                   Point3(-1.9, -3, 0),
                                                   startPos=Point3(-3.5, 0, 0))
        posInterval5 = self.pandaActor.posInterval(1,
                                                   Point3(1.9, -3, 0),
                                                   startPos=Point3(-1.9, -3, 0))
        posInterval6 = self.pandaActor.posInterval(1,
                                                   Point3(3.5, 0, 0),
                                                   startPos=Point3(1.9, -3, 0))
        hprInterval1 = self.pandaActor.hprInterval(1,
                                                   Point3(-60, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(1,
                                                   Point3(-120, 0, 0),
                                                   startHpr=Point3(-60, 0, 0))
        hprInterval3 = self.pandaActor.hprInterval(1,
                                                   Point3(-180, 0, 0),
                                                   startHpr=Point3(-120, 0, 0))
        hprInterval4 = self.pandaActor.hprInterval(1,
                                                   Point3(-240, 0, 0),
                                                   startHpr=Point3(-180, 0, 0))
        hprInterval5 = self.pandaActor.hprInterval(1,
                                                   Point3(-300, 0, 0),
                                                   startHpr=Point3(-240, 0, 0))
        hprInterval6 = self.pandaActor.hprInterval(1,
                                                   Point3(-360, 0, 0),
                                                   startHpr=Point3(-300, 0, 0))
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  posInterval3, hprInterval3,
                                  posInterval4, hprInterval4,
                                  posInterval5, hprInterval5,
                                  posInterval6, hprInterval6,
                                  name="pandaPace")
        self.pandaPace.loop()

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

