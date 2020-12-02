#!/usr/bin/env python
import csv

class extractData:
   def __init__(self):
      self.x = []
      self.rot = []	
      with open('/home/nikolai/Cyborg_project/src/sensorpackage/sensor.csv') as file:
         reader = csv.reader(file)
	 for row in reader:
	    #row[0] = index (not used)
	    #row[1] = x measurement (used for rotating the robot about z-axis)
            #row[2] = y measurement (used for translation in x-direction of robot)
	    #row[1] = z measurement (not used)
	    self.x.append(row[2])
	    self.rot.append(row[1])

data = extractData()
print(data.x)
print(data.rot)
