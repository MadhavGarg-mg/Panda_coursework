CSC1034: Practical 1
===========

This package is build as a part of the CSC1034: Portfolio-1. 

Type `python walking_panda.py` to see a moving rotating panda.

## Camera Options:

Type `python walking_panda.py --no-rotate` to stop the camera rotating.

Type `python walking_panda.py --rotate-speed=10` to increase the rotation speed of the camera by 10 times.

Type `python walking_panda.py --rotate-speed=0.5` to decrease the rotation speed of the camera by 2 times.

Type `python walking_panda.py --rotate-speed=-1` to move the camera clockwise.

Type `python walking_panda.py --zoom=2` to zoom in or out by 2 times.

Type `python walking_panda.py --zoom=0.5` to zoom in or out by 0.5 times.

If you use `python walking_panda.py --no-rotate --rotate-speed=500`, the camera rotate speed will not change
as the camera will not rotate.

## Panda Modifications Options:

Type `python walking_panda.py --scale=2` this will multiply the size of the panda by 2.

Type `python walking_panda.py --scale=0.5` this will multiply the size of the panda by 0.5.

Type `python walking_panda.py --no-walk` to stop the panda from walking.

Type `python walking_panda.py --hexagon` to make the panda walk in a hexagon. 

## Starting Position Options:

Type `python walking_panda.py --move-side=10` to move the panda to the left by 10 units.

Type `python walking_panda.py --move-side=-10` to move the panda to the right by 10 units.

Type `python walking_panda.py --move=10` to move the panda forward by 10 units.

Type `python walking_panda.py --move=-10` to move the panda behind by 10 units.

Type `python walking_panda.py --fly=5` to make a panda fly by 5 units.

## Multiple Arguments Recommendations:

Type `python walking_panda.py --hexagon --scale=2 --no-rotate` to see a big and slow panda walk in a hexagon.

Type `python walking_panda.py --hexagon --scale=0.5 --no-rotate` to see a small and speedy panda walk in a hexagon.

Type `python walking_panda.py --hexagon --no-rotate --fly=5` to see a flying panda walk in hexagons.
