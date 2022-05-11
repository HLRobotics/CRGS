
"""
Inker Robotics Pvt Ltd 
Developed on Jan 2021
Hardware Designed and Developed by:Er.Anu Antony
Software and Logic Designed and Developed by:Er.Akhil P Jacob

"""

from Robot_Guidance_System import PhysicalParamTester
from FireBase import firedata
import time
l=300
b=300
x1=int(input("[Enter init x1]"))
y1=int(input("[Enter init y1]"))

    
x2=int(input("[Enter final x2]"))
y2=int(input("[Enter final y2]"))
id=int(input("[Enter ID]"))
data=PhysicalParamTester.Physics(x1,x2,y1,y2,1,l,b)
data1=str(data[0])
data2=str(data[1])
data3=str(data[2])
data4=str(data[3])

message=data1+data2+data3+data4
print(message)
x1=x2
y1=y2


feedback=firedata.fireData(message,id)
print( feedback)

