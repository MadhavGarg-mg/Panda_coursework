from . import panda
import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    parser.add_argument("--no-rotate", help="Suppress Rotation.", action="store_true")
    parser.add_argument("--scale", default=1, help="Scale Panda.", type=float)
    parser.add_argument("--move-side", default=0, help="Move Panda left(positive) or right(negative).", type=int)
    parser.add_argument("--move", default=0, help="Move Panda forward(positive) or behind(negative).", type=int)
    parser.add_argument("--fly", default=0, help="Make the Panda fly.", type=int)
    parser.add_argument("--rotate-speed", default=1, help="Make the camera rotate faster.", type=float)
    parser.add_argument("--zoom", default=1, help="Make the camera zoom in or out.", type=float)
    parser.add_argument("--no-walk", help="Makes the panda stop walking.", action="store_true")
    parser.add_argument("--hexagon", help="Makes the panda walk in a hexagon.", action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()

