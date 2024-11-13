import random
from SimWindow import SimWindow

def generateSegments(segsCount: int):
    segs = []
    forbidden_y = []
    forbidden_x = []
    
    for i in range(segsCount):
        print(i)
        if i == 0:
            p1 = random.randint(0, 100)
            p2 = random.randint(0, 100)
            p3 = p1
            p4 = random.randint(0, 100)
            
            seg1 = (p1,p2)
            seg2 = (p3,p4)
            
            segs.append(((seg1, seg2)))
            forbidden_y.append(range(abs(p2)))
            continue
        

        if i % 2 == 0:
            seg1 = segs[i-1][1]
            px = seg1[0]
            py = random.randint(0, 100)
            segs.append(((seg1, (px, py))))
            
            
            
        else:
            seg1 = segs[i-1][1]
            py = seg1[1]
            px = random.randint(0, 100)
            segs.append(((seg1, (px, py))))
            
            

    print(segs)
    return segs

segs = generateSegments(10)

#Setup of the interface
ms = SimWindow(segs, cars = [], draw_bridges=True)
#show the window
ms.show()