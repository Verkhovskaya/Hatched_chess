import math

piece_name = "Rook"
piece_file = open("/Users/2017-A/Dropbox/Anna/Projects/Hatched_chessboard/"+piece_name+".md")
output_file = open("/Users/2017-A/Dropbox/Anna/Projects/Hatched_chessboard/arcs/"+piece_name+".txt", "w")
step_height = 0.05
step_rotation = 1.0/12*math.pi #radians, or
converstion_factor = 0.05 #Points to inches

rotation = 0
height = 0

for line in piece_file:
    line = float(line)
    x = math.sin(rotation)*line*converstion_factor
    y = math.cos(rotation)*line*converstion_factor

    output_file.write(str(x)+" "+str(y)+" "+str(height)+"\n")
    rotation += step_rotation
    height += step_height
