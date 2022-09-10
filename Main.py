from dataclasses import replace
from email import header
from email.policy import default
from queue import PriorityQueue
from xml.etree.ElementPath import find
import bs4
from Importer import parser
import csv
import itertools

filePath = (r"HTMLDocs\firstfile.htm")


data = open(filePath,'r')
htmlData = bs4.BeautifulSoup (data ,'html.parser')
htmlDataArr = htmlData.get_text("td")
htmlDataArr = htmlDataArr.replace(" ","")
htmlDataArr = htmlDataArr.replace("\n","")
htmlDataArr = htmlDataArr.replace("\xa0","")
htmlDataSplitArr = htmlDataArr.split("td")
Parse = parser(htmlDataSplitArr)


Parse.findDIMMData()
Parse.findVideoAdapterData()
Parse.findDiskDriveData()
Parse.findMonitorData()

headerNames = [
Parse. findUserNameData(),
Parse. findMotherboardData(),
Parse. findCPUTypeData(),
Parse. findCurrentPowerSourceData(),
Parse. findSystemMemoryData(),
]

listDimm = list(itertools.chain(*Parse.DimmList))

if len(listDimm) == 2:
     headerNames.append(listDimm[0])
elif len(listDimm) == 4:
     headerNames.append(listDimm[0])
     headerNames.append(listDimm[2])
elif len(listDimm) == 6:
     headerNames.append(listDimm[0])
     headerNames.append(listDimm[2])
     headerNames.append(listDimm[4])
elif len(listDimm) == 8:
     headerNames.append(listDimm[0])
     headerNames.append(listDimm[2])
     headerNames.append(listDimm[4])
     headerNames.append(listDimm[6])


for i in range(len(Parse.VideoAdapterList)):
     headerNames.append(Parse.VideoAdapterList[i])

for i in range(len(Parse.DiscList)):
     headerNames.append(Parse.DiscList[i])
     
for i in range(len(Parse.MonitorList)):
     headerNames.append(Parse.MonitorList[i])


Parse.findVideoAdapterNameData()
Parse.findDiskDriveNameData()
Parse.findMonitorNameData()

accessoriesName = [
Parse.findUserNameNameData(),
Parse.findMotherboardNameData(),
Parse.findCPUNameData(),
Parse.findCurrentPowerSourceName(),
Parse.findSystemMemoryCount(),
]

listDimm = list(itertools.chain(*Parse.DimmList))
if len(listDimm) == 2:
     accessoriesName.append(listDimm[1])
if len(listDimm) == 4:
     accessoriesName.append(listDimm[1])
     accessoriesName.append(listDimm[3])
elif len(listDimm) == 6:
     accessoriesName.append(listDimm[1])
     accessoriesName.append(listDimm[3])
     accessoriesName.append(listDimm[5])
elif len(listDimm) == 8:
     accessoriesName.append(listDimm[1])
     accessoriesName.append(listDimm[3])
     accessoriesName.append(listDimm[5])
     accessoriesName.append(listDimm[7])


for i in range(len(Parse.VideoAdapterNameList)):
     accessoriesName.append(Parse.VideoAdapterNameList[i])

for i in range(len(Parse.DiscNameList)):
     accessoriesName.append(Parse.DiscNameList[i])
     
for i in range(len(Parse.MonitorNameList)):
     accessoriesName.append(Parse.MonitorNameList[i])
print(accessoriesName)

with open ("ConvertData.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(headerNames)    
    writer.writerow(accessoriesName)      
                 
                   
                   