#!/bin/python3

import sys
#from dataclasses import dataclass

class Iris:
	irisType: str
	sLen: float
	sWid: float
	pLen: float
	pWid: float
	
	def __init__(self, iType, iSLen, iSWid, iPLen, iPWid):
		self.irisType = iType
		self.sLen = iSLen
		self.sWid = iSWid
		self.pLen = iPLen
		self.pWid = iPWid

def readData(inFile):
	irisList = []
	reading = False
	with open(inFile, "r") as file:
		for line in file:
			if "@Data" in line:
				reading = True
				continue
			if reading:
				fields = line.split(',')
				if fields[4] == "Iris-setosa":
					irisType = "setosa"
				elif fields[4] == "Iris-virginica":
					irisType = "virginica"
				elif fields[4] == "Iris-versicolor":
					irisType = "versicolor"
				else:
					irisType = "unknown"
				irisList.append(Iris(irisType, float(fields[0]), float(fields[1]), float(fields[2]), float(fields[3])))
	return irisList		
	
def procNumField(iList, field):
	vals = []
	for iris in iList:
		if field == 1:
			vals.append(iris.sLen)
		elif field == 2:
			vals.append(iris.sWid)
		elif field == 3:
			vals.append(iris.pLen)
		elif field == 4:
			vals.append(iris.pWid)
		else:
			print(f"Field {field} is invalid")
			exit(1)
	fieldMin = min(vals)
	fieldMax = max(vals)
	fieldAvg = sum(vals)/len(vals)
	return fieldMin, fieldMax, fieldAvg
	
def countIrisTypes(iList):
	setCount = 0
	virCount = 0
	verCount = 0
	for iris in iList:
		iType = iris.irisType
		if iType == "setosa":
			setCount += 1
		elif iType == "virginica":
			virCount += 1
		elif iType == "versicolor":
			verCount += 1
		else:
			print(f"Iris type {iType} is unknown")
			exit(1)
	return setCount, virCount, verCount

def main(args):
	if len(args) != 2:
		print(f"Incorrect number of arguments. Expected 1, got {len(args)}")
		exit(1)
	
	irisList = readData(args[1])
	print(f"{irisList}")
	
	#fieldMin, fieldMax, fieldAvg = procNumField(irisList, 1)
	#print(f"Sepal Length: min = {fieldMin}, max = {fieldMax}, average = {fieldAvg}")
	#fieldMin, fieldMax, fieldAvg = procNumField(irisList, 2)
	#print(f"Sepal Width: min = {fieldMin}, max = {fieldMax}, average = {fieldAvg}")
	#fieldMin, fieldMax, fieldAvg = procNumField(irisList, 3)
	#print(f"Petal Length: min = {fieldMin}, max = {fieldMax}, average = {fieldAvg}")
	#fieldMin, fieldMax, fieldAvg = procNumField(irisList, 4)
	#print(f"Petal Width: min = {fieldMin}, max = {fieldMax}, average = {fieldAvg}")
	
	numSet, numVir, numVer = countIrisTypes(irisList)
	print(f"Iris Types: Iris Steosa = {numSet}, Iris Versicolor = {numVer}, Iris Virginica = {numVir}")		

	
if __name__ == '__main__':
	main(sys.argv);
