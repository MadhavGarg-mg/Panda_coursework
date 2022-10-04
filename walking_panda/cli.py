from . import panda
import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation.", action="store_true")
    parser.add_argument("--scale", default=1, help="Scale Panda.", type=float)
    parser.add_argument("--move-side", default=0, help="Move Panda left(positive) or right(negative).", type=float)
    parser.add_argument("--move", default=0, help="Move Panda forward(positive) or behind(negative).", type=float)
    parser.add_argument("--fly", default=0, help="Make the Panda fly.", type=float)
    # parser.add_argument("--rotate-speed", default=0, help="Make the camera rotate faster.", type=int)

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()

