from pixy import *
from ctypes import *
from networktables import NetworkTables

NetworkTables.initialize(server='roborio-6025-frc.local') # Roborio ile iletişim kuruyoruz

table = NetworkTables.getTable("Vision") # table oluşturuyoruz

# Pixy Python SWIG get blocks example #

print ("Pixy Python SWIG Example -- Get Blocks")

# Initialize Pixy Interpreter thread #
pixy_init()

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

blocks = BlockArray(100)
frame  = 0

# Wait for blocks #
while 1:

  count = pixy_get_blocks(100, blocks)

  if count > 0:
    # Blocks found #
    print 'frame %3d:' % (frame)
    frame = frame + 1
    for index in range (0, count):
      print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height)
      table.putNumber("X", blocks[index].x) # roborioya değeri göndermek
      table.putNumber("Y", blocks[index].y) # roborioya değeri göndermek
