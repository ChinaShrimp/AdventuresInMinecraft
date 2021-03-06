# Adventure 4: vanishingBridge.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a bridge as you walk in the air or on water,
# and when your feet are safe again, the bridge magically disappears.

# Import necessary modules
import mcpi.minecraft as minecraft
import time

# Constants for the block types
AIR = 0
FLOWING_WATER = 8
WATER = 9
GLASS = 20

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Create a bridge list that is empty.
# There are no blocks in your bridge at the moment,
# so it always starts empty
bridge = []

# Define a function to build a bridge if your feet are not safe
# This function will be reusable in other programs
def buildBridge():
  # Get the position of your player
  x, y, z = mc.player.getTilePos()

  # Get the block directly below your player
  b = mc.getBlock(x, y-1, z)

  # Is the player safe?
  if b == AIR or b == FLOWING_WATER or b==WATER:
    # Player is unsafe, build a glass block directly under the player
    mc.setBlock(x, y-1, z, GLASS)
    # Use a second list to remember the three parts of this coordinate
    # but note y-1 as you want to remember the block position below
    coordinate = [x, y-1, z]

    # Add the new coordinate to the end of your bridge list
    bridge.append(coordinate)

elif b != GLASS:
    # Player is safe and not on the bridge
    if len(bridge) > 0:
      # There is still some bridge remaining
      # Remove the last coordinate from the bridge list
      coordinate = bridge.pop()

      # Set the block at that coordinate to AIR, to delete the bridge
      mc.setBlock(coordinate[0], coordinate[1], coordinate[2], AIR)

      # Delay a short time so that the bridge vanishes slowly
      time.sleep(0.25)

# Game loop
while True:
  # Don't run the game loop too fast, you might crash your computer
  # But don't run the game loop too slow, you might fall off the bridge
  time.sleep(0.25)

  # Decide what to do with the bridge
  buildBridge()

# END
