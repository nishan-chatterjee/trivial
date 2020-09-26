# trivial
Fun incosequential experiments


Did a quick check of the blue vs brown ratio of the opening animation of 3Blue1Brown (Image attached) using OpenCV because they seemed a bit off. Well, here are the results:
Blue : Brown = 2.4035 : 1 when rgb values of blue > red considered increase in blue count.
Blue : Brown = 2.5326 : 1 when blue >= red considered increase in blue count.
Considering the gift of education he has granted us with, I'll stick to rounding the equality.

Blue >= Red
    /usr/bin/python3.8 /home/nishan/Github/local_exps/blue_brown_ratio.py
    Number of blue pixels =  77961
    Number of brown pixels =  30783
    Ratio of blue to brown =  2.5325991618750607  :  1.0

    Process finished with exit code 137 (interrupted by signal 9: SIGKILL)

Blue > Red
    /usr/bin/python3.8 /home/nishan/Github/local_exps/blue_brown_ratio.py
    Number of blue pixels =  77087
    Number of brown pixels =  31657
    Ratio of blue to brown =  2.4350696528413938  :  1.0

    
Note on the 3blue1brown_logo_ratio implementation:
The true optical intuition behind the brown of the logo should rather be thought of being closer to the brown section, and not an artifact of the color ratio of the logo itself (which results in brown points on the edge of the eye). Correct that in the next implementation.
