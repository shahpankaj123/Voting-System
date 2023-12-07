from AbstractModule.admin_abstract import AdminAbstract
import re
import uuid
import os
import json
class Admin(AdminAbstract):
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename='data_files/admin_log.txt'
        self.file_path = os.path.join(current_directory, filename)
        filename1='data_files/schedule.txt'
        self.file_path1 = os.path.join(current_directory, filename1)
        filename2='data_files/candidatelist.txt'
        self.file_path2 = os.path.join(current_directory, filename2)

    def create_admin(self):
        try:
          if self.admin_login():
            id=str(uuid.uuid4())
            username=input("enter the username:")
            password=input("enter the password:")
            password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:,<.>]).{8,}$')
            if password_pattern.match(password):
                data={"id":id,"username":username,"password":password}
                try: 
                  with open(self.file_path, 'r') as file:
                    self.existing_data=json.load(file) 
                except FileNotFoundError:
                   print("File Name not found")  


                print(self.existing_data)
                self.existing_data.append(data)
                with open(self.file_path, 'w') as file:
                    json.dump(self.existing_data, file,indent=2)
                print("Admin created successfully")
            else:
                print("Please Make Strong Password") 
          else:
              print("Username or Password not matched")                                 
        except Exception as e:
           print(e)

    def admin_login(self):
        try:
            print("---Admin Login System ---")
            username=input("enter the username:")
            password=input("enter the password:") 
            try:
               with open(self.file_path, 'r') as file:
                 self.existing_data=json.load(file)
            except FileNotFoundError:
                print("File Name not found")     

            data=[list for list in self.existing_data if list['username']==username and list['password']==password]
            if data:
                print("Login successfully")
                return True
            else:
                print("Username or Password not matched")
                return False
        except Exception as e:
            print(e) 

    def election_schedule(self): 
        try:
         if self.admin_login():
            Constituency=input("enter the Constituency name:")
            date=input("enter the date of election(YYYY-MM-DD)")
            data={"Constituency":Constituency,"Date":date}
            try:
             with open(self.file_path1, 'r') as file:
                self.schedule_data=json.load(file)
            except FileNotFoundError:
                print("File Name not found")    

            self.schedule_data.append(data)

            with open(self.file_path1, 'w') as file:
                json.dump(self.schedule_data, file,indent=2)

            print("Election Scheduled successfully")
         else:
            print("You are not authorired to schedule a election") 

        except Exception as e:
            print(e)

    def canditate_registration(self):
        try:
          if self.admin_login():
            id=str(uuid.uuid4())
            name=input("enter the name of candicate:")
            party=input("enter the political party")
            candidacy_location=input("enter the Candidacy From")
            data={"id":id,"name":name,"party":party,"candidacy_location":candidacy_location}
            try:
              with open(self.file_path2, 'r') as file:
                self.candidacy_data=json.load(file)
            except FileNotFoundError:
                print("File Name not found")    

            self.candidacy_data.append(data)

            with open(self.file_path2, 'w') as file:
                json.dump(self.candidacy_data, file,indent=2)

            print("Candidate registration Successfully")

          else:
            print("You are not authorired to schedule a election")  

        except Exception as e:
            print(e)

    def update_canditate(self):
        try:
          if self.admin_login():
            id=input('enter the id of candidate:')
            try:
              with open(self.file_path2, 'r') as file:
                self.candidacy_data=json.load(file)
            except FileNotFoundError:
                 print("File Name not found")

            g=False    
            for data in self.candidacy_data:
                if data['id']==id:
                   name=input("enter the name of candicate:")
                   party=input("enter the political party")
                   candidacy_location=input("enter the Candidacy From") 
                   data['name']=name
                   data['party']=party
                   data['candidacy_location']=candidacy_location
                   g=True
                else:
                  print('Id not Found')    

            if g==True: 
               with open(self.file_path2, 'w') as file:
                    json.dump(self.candidacy_data, file,indent=2)
               print("Data Updated Successfully")
        except Exception as e:
           print(e)      
                     
    def del_canditate(self):
        try:
          if self.admin_login():
            id=input('enter the id of candidate:')
            try:
              with open(self.file_path2, 'r') as file:
                self.candidacy_data=json.load(file)
            except FileNotFoundError:
                print("File Name not found")

            for data in self.candidacy_data:
                if data['id'] == id:
                  self.candidacy_data.remove(data)
                  with open(self.file_path2, 'w') as file:
                    json.dump(self.candidacy_data, file,indent=2)   
                  print("Candidate removed successfully")
                else:
                  print("ID not found") 
          else:
             print("You are not authorired to schedule a election") 
        except Exception as e:
           print(e)     
                     

a=Admin()
a.create_admin()
a.election_schedule()
a.canditate_registration()
a.update_canditate()
a.del_canditate()

        




        
                    
                  