#!/user/bin/env python3

__author__ = "spyderkam"

# Colors
BLUE = (0, 0, 255)
GREEN = (50, 168, 82)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def formation(formation_type):
  match formation_type:
    case "433":
      return {"blue": [
        [75, 300],   # GK
        [235, 140],  # LB
        [190, 250],  # LCB
        [190, 350],  # RCB
        [235, 460],  # RB
        [350, 200],  # LCM
        [350, 300],  # CM
        [350, 400],  # RCM
        [500, 150],  # LW
        [500, 300],  # ST
        [500, 450],  # RW
      ], "red": [
        [725, 300],  # GK
        [565, 140],  # LB
        [610, 250],  # LCB
        [610, 350],  # RCB
        [565, 460],  # RB
        [450, 200],  # LCM
        [450, 300],  # CM
        [450, 400],  # RCM
        [300, 150],  # LW
        [300, 300],  # ST
        [300, 450],  # RW
      ]}
    
    case "4231":
      return {"blue": [
        [75, 300],   # GK
        [235, 140],  # LB
        [190, 250],  # LCB
        [190, 350],  # RCB
        [235, 460],  # RB
        [350, 250],  # LDM
        [350, 350],  # RDM
        [450, 150],  # LAM
        [450, 300],  # CAM
        [450, 450],  # RAM
        [500, 300],  # ST
      ], "red": [
        [725, 300],  # GK
        [565, 140],  # LB
        [610, 250],  # LCB
        [610, 350],  # RCB
        [565, 460],  # RB
        [450, 250],  # LDM
        [450, 350],  # RDM
        [350, 150],  # LAM
        [350, 300],  # CAM
        [350, 450],  # RAM
        [300, 300],  # ST
      ]}

    case "442":
      return {"blue": [
        [75, 300],   # GK
        [235, 140],  # LB
        [190, 250],  # LCB
        [190, 350],  # RCB
        [235, 460],  # RB
        [350, 150],  # LM
        [350, 250],  # LCM
        [350, 350],  # RCM
        [350, 450],  # RM
        [500, 250],  # LST
        [500, 350],  # RST
      ], "red": [
        [725, 300],  # GK
        [565, 140],  # LB
        [610, 250],  # LCB
        [610, 350],  # RCB
        [565, 460],  # RB
        [450, 150],  # LM
        [450, 250],  # LCM
        [450, 350],  # RCM
        [450, 450],  # RM
        [300, 250],  # LST
        [300, 350],  # RST
      ]}
    
    case "4231":
      return {"blue": [
        [75, 300],   # GK
        [235, 140],  # LB
        [190, 250],  # LCB
        [190, 350],  # RCB
        [235, 460],  # RB
        [350, 250],  # LDM
        [350, 350],  # RDM
        [450, 150],  # LAM
        [450, 300],  # CAM
        [450, 450],  # RAM
        [500, 300],  # ST
      ], "red": [
        [725, 300],  # GK
        [565, 140],  # LB
        [610, 250],  # LCB
        [610, 350],  # RCB
        [565, 460],  # RB
        [450, 250],  # LDM
        [450, 350],  # RDM
        [350, 150],  # LAM
        [350, 300],  # CAM
        [350, 450],  # RAM
        [300, 300],  # ST
      ]}