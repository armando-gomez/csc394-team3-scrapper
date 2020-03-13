import csv
import re

def convertData(dataFiles):
    locData = []
    with open('uscities.csv', 'r') as citiesCSV:
        reader = csv.reader(citiesCSV)
        for i in reader:
            locData.append(i)
    citiesCSV.close()

    states = {
		"AL" : "Alabama",
		"AL" : "Alaska",
		"AZ" : "Arizona",
		"AR" : "Arkansas",
		"CA" : "California",
		"CO" : "Colorado",
        "CT" : "Connecticut",
		"DE" : "Delaware",
		"FL" : "Florida",
		"GA" : "Georgia",
		"HI" : "Hawaii",
		"ID" : "Idaho",
        "IL" : "Illinois",
		"IN" : "Indiana",
		"IA" : "Iowa",
		"KS" : "Kansas",
		"KY" : "Kentucky",
		"LA" : "Louisiana",
        "ME" : "Maine",
		"MD" : "Maryland",
		"MA" : "Massachusetts",
		"MI" : "Michigan",
		"MN" : "Minnesota",
		"MS" : "Mississippi",
        "MO" : "Missouri",
		"MT" : "Montana",
		"NE" : "Nebraska",
		"NV" : "Nevada",
		"NH" : "New Hampshire",
		"NJ" : "New Jersey",
        "NM" : "New Mexico",
		"NY" : "New York",
		"NC" : "North Carolina",
		"ND" : "North Dakota",
		"OH" : "Ohio",
		"OK" : "Oklahoma",
        "OR" : "Oregon",
		"PA" : "Pennsylvania",
		"RI" : "Rhode Island",
		"SC" : "South Carolina",
		"SD" : "South Dakota",
		"TN" : "Tennessee",
        "TX" : "Texas",
		"UT" : "Utah",
		"VT" : "Vermont",
		"VA" : "Virginia",
		"WA" : "Washington",
		"WV" : "West Virginia",
        "WI" : "Wisconsin",
        "WY" : "Wyoming"
	}
    with open('jobData.csv', 'w', newline='') as file:
        data = []
        data.append(["Title", "Company", "City","State", "lowPay", "highPay","Equity" ,"latitude", "longitude" ,"Posted", "Link", "Timestamp"])

        for files in dataFiles:
            with open(files) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if "Title" in row[0] and "Company" in row[1]:
                        continue
                    else:
                        Title = ""
                        Company = ""
                        City = ""
                        State = ""
                        lowPay = None
                        highPay = None
                        Equity = False
                        Latitude = None
                        Longitude = None
                        Posted = ""
                        Link = ""
                        Timestamp = ""
                        Title = row[0]
                        Company = row[1]
                        Posted = row[4]
                        Link = row[5]
                        Timestamp = row[6]
                        try:
                            temp = row[2]
                            temp = temp.split(',')
                            City = temp[0]
                            temp = temp[1].split(' ')
                            State = temp[1]
                            State = states.get(State)
                        except:
                            City = ""
                            State = ""
                            pass

                        if row[3] == "" or row[3] == " " or row[3] == ''or row[3] == ' ':
                            pass
                        elif "Equity" in row[3]:
                            Equity = True
                        else:
                            temp = row[3].split('-')
                            temp2 = temp[0]
                            if files == "GlassdoorData.csv":
                                lowPay = temp2[temp2.find("$")+1:temp2.find("K")]
                                lowPay = int(lowPay) * 1000
                                temp2 = temp[1]
                                highPay = temp2[temp2.find("$")+1:temp2.find("k")]
                                highPay = int(highPay) * 1000
                            else:
                                try:
                                    lowPay = temp2[temp2.find("$")+1:temp2.find("k")]
                                    lowPay = int(lowPay) * 1000
                                    temp2 = temp[1]
                                    highPay = temp2[temp2.find(" ")+1:temp2.find("k")]
                                    highPay = int(highPay) * 1000
                                except:
                                    lowPay = None
                                    highPay = None
                                    pass

                        try:                                
                            for i in locData:                                
                                if City == i[0] and State == i[3]:
                                    Latitude = i[8]
                                    Longitude = i[9]
                        
                        except:
                            print("ERRORS FINDING LATITUDE AND LONGITUDE CODE")
                            pass
                        data.append([Title,Company,City,State,lowPay,highPay,Equity,Latitude,Longitude,Posted,Link,Timestamp])
                        Equity = False
                       
            csvfile.close()
        for row in data:

            try:
                writer = csv.writer(file)
                writer.writerow(row)
            except:
                pass
    file.close()
                

                        
stack = "StackoverflowData.csv"
indeed ="IndeedData.csv"
glass = "GlassdoorData.csv"

files = []
files.append(stack)
files.append(indeed)
files.append(glass)
convertData(files)
