from . import panda
import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation", action="store_true")
    args = parser.parse_args()

    # parser = argparse.ArgumentParser(prog="walking_panda")
    # parser.add_argument("--scale", help="Suppress Rotation", action="store_true")
    # args1 = parser.parse_args()
    # # Jumping? Standing?

    walking = panda.WalkingPanda(**vars(args))
    # scale = panda.WalkingPanda(**vars(args1))
    walking.run()
    # scale.run()
