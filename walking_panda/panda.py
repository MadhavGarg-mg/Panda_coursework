from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

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

