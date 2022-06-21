#Name: TSHIRELETSO ELTON PHAKEDI
#Project: DEVPROX Test 2 Solution



#importing a date module to access the systems current date 
from datetime import date


#Creating a main Class to hold users personal details
class Client:

    #defining a firstnames list with 20 initialized values
    names = ["Leon","Jody Ron Frank","Thabo Rodney","Neo","Atlehang","Whale","Elon Boron","Thapelo","Zukile","Banda",
             "Derik","Joe Ean","Ron Van Welde","Meike","Tshidiso","Oratile","Puleng Meike","Ipeleng","Fourie","David"]
    
    #defining a lastnames list with 20 initialized values
    surnames = ["Phakedi","Lekoma","Sepato","Lee","Senalta","Leeuw","Zachariah","Roelen","Moloi","Casius",
                "Mohammed","Silo","Olifant","Berry","Van Schalk Wyk","Moses","Williams","Claasen","Zondi","Bafokeng"]
    
    def __init__ (self,names,surnames):
        #initialising class variables
        self.firstNames = names
        self.lastName = surnames

    
##########################################################################################

    #defining a class method to workout users initial(s)
    def genInitials(self,first_Names):
        
        self.firstNames = first_Names

        first_initial = self.firstNames[0]

        mid = first_Names.find(" ")+1
        mid_initial = self.firstNames[mid]
           
        last = first_Names.rfind(" ")+1
        last_initial = self.firstNames[last]
            
        return (first_initial + mid_initial + last_initial)
        
        

##########################################################################################
    
    #defining a class method to generate random date of births
    def dateOfBirth(self):
 
        import random
       
        day = random.randint(1,31)
        month = random.randint(1,12)
        year = str(19)+str(random.randint(52,70))
        return day,month,year

##########################################################################################
    
    #defining a function to write elements(users personal details) into csv file
    def csvFile(self,no_Variation):
        #importing both 'csv' and 'random' modules - to access and use their built-in functions and methods
        import csv
        import random

        #declaring empty list variables of various fields as temporary data containers
        user_record =[]
        user_firstname = []
        user_lastname = []
        user_initials = []
        user_DOB = []
        age = []

        #opening a file to write data and exporting it as a csv file 
        with open ('output.csv','w') as my_csvfile:
            
            #creating field names for identification of data - headernames 
            field_names =['UserId','First_Names','Last_Names','Initials','Age','DateOfBirth']
            
            csv_writer = csv.writer(my_csvfile)
            csv_writer = csv.DictWriter(my_csvfile,fieldnames = field_names,delimiter = ',') 
            csv_writer.writeheader()

            #declaring and initializing a counter variable - to keep track of written records 
            count = 1
          
            #declaring an iteration function 'while loop' to repeatedly write data into a file - per no of given variation
            while count <= no_Variation  : 
                 
                    #randomly picking a name from given firstnames list
                    user_firstname = random.choice(self.names)
                    #randomly picking a Surname from given firstnames list
                    user_lastname = random.choice(self.surnames)

                    #Combining randomly picked up firstname and surname - to form one name
                    fullname = list(user_firstname +" "+user_lastname)

                    #calling a method working out user initial - too find initials of randomly picked up name above
                    user_initials = self.genInitials(user_firstname)

                    #calling a method generating random date of birth - to separately store its returned values
                    day,month,year = self.dateOfBirth()

                    #Computing the AGE from a randomly generated birth year with the current year
                    age = date.today().year-int(year)

                    #Combining the separately returned values of Date of Birth method into a correct joined Date of Birth
                    user_DOB = str(day)+"/"+str(month)+"/"+str(year)

                    #Checking if the name DOES NOT exist in the record - to avoid duplication of records
                    if not fullname in user_record:
                        user_record =[count,user_firstname,user_lastname,user_initials,age,user_DOB]
                        
                        #Writing elements into an opened file 
                        csv_writer.writerow({'UserId':count,'First_Names':user_firstname,'Last_Names':user_lastname,
                                             'Initials':user_initials,'Age':age,'DateOfBirth':user_DOB})
                    #incrementing a counter by 1 after each record is recorded
                    count +=1
        #closing a file after writing data into it
        my_csvfile.close()
##########################################################################################

#Creating a class instance to access and use class defined methods and functions
obj_1 = Client("","") 

#printing an empty string - to open a new line on next output
print (" ")
#requesting a user to input number of variation to execute 
noOfVar = int(input ("Enter a number of variations: "))
#passing the number of variations(provided by the user) to our class method
obj_1.csvFile(noOfVar)


