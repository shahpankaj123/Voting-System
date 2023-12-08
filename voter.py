import json
from AbstractModule.voter_abstract import VoterAbstract
from datetime import datetime
import os

class Voter(VoterAbstract):
    CURRENT_DIR = os.getcwd()
    VOTER_DETAIL_PATH = os.path.join(CURRENT_DIR, "Data_files", "voter_detail.txt")
    
    
    @staticmethod
    def generate_id() -> int:
        file_path = os.path.join(Voter.CURRENT_DIR, "LogFiles", "voter_id.log")
        try:
            with open(file_path, "r") as file:
                id = int(file.read())
        except FileNotFoundError:
            with open(file_path, "w+") as file:
                id = 0
                file.write(str(id))

        id +=1
        with open(file_path, 'r+') as file:
            file.write(str(id))
        return id

    
    def voter_registration(self) -> None:
        full_name = input("Enter your full-name: ")
        try:
            date_str = input("Enter your Date of birth (yyyy-mm-dd): ")
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format enter in (yyyy-mm-dd)")
            date_str = input("Enter the valid date format (yyyy-mm-dd)")

        brith_year = int(date_str.split('-')[0])
        
        if not self.check_age(brith_year):
            print("Your are under age")  
            
        address = input("Enter your address: ")
        password = input("Create Password: ")

        voter_detail = {
            "id": self.generate_id(),
            "name": full_name,
            "date_of_birth": date_str,
            "address": address,
            "password":password
        }
        self.insert_data(voter_detail)
        print("added")

    
    def insert_data(self, data: dict) -> None:
        file_path = os.path.join(Voter.CURRENT_DIR, "Data_files", "voter_detail.txt")
        with open(file_path, "a+") as voter_detail:
            data_str = json.dumps(data)
            voter_detail.write(data_str + '\n')

    def check_age(self,birth_year: int)-> bool:
        current_year = datetime.today().now().date().year
        return (current_year - birth_year) >= 18

    def view_result(self):
        file_path = os.path.join(Voter.CURRENT_DIR, 'Data_files', 'vote_store.txt')

        try:
            with open(file_path, 'r') as file:
                print("Canditate ID\t\t Total Vote")
                print("-" * 40)
                for line in file:

                    vote = json.loads(line)
                    print(f"{vote['id']}\t\t\t{vote['total_vote']}")
                    print("-" * 40)
                    
        except FileNotFoundError:
            print("No votes recorded yet.")


    def update_voter_detail(self):
        voter_data = []
        voter_id = input("Enter a voter ID: ")
        with open(Voter.VOTER_DETAIL_PATH, 'r') as file:
            for line in file:
                voter_dict = json.loads(line)
                voter_data.append(voter_dict)

        for voter in voter_data:
            if int(voter["id"]) == int(voter_id):
                print(voter)
                voter['name'] = input("Update your name: ") or voter['name']
                voter['date_of_birth'] = input("Update data: ") or voter['date_of_birth']
                voter['address'] = input("Update address: ") or voter['address']
                voter['password'] = input("Update password: ") or voter['password']
                print("Profile updated")
                break
        

        with open(Voter.VOTER_DETAIL_PATH, 'w') as file:
            for data in voter_data:
                data_str = json.dumps(data)
                file.write(data_str + '\n')  


    def search_voter(self):
        voter_id = input("Enter a voter id: ")
        voter_data = []

        with open(Voter.VOTER_DETAIL_PATH, 'r') as file:
            for line in file:
                voter_dict = json.loads(line)
                voter_data.append(voter_dict)

        found_voter = None

        for voter in voter_data:
            if voter["id"] == int(voter_id):
                found_voter = voter
                break

        if found_voter:
            print("Voter found:")
            print("ID:", found_voter["id"])
            print("Name:", found_voter["name"])
            print("Date of Birth:", found_voter["date_of_birth"])
            print("Address:", found_voter["address"])
            print("Password:", found_voter["password"])
        else:
            print("Voter not found with ID:", voter_id)



    
    def caste_vote(self):
        voterId = int(input("Enter your voterID: "))
        file_path = os.path.join(Voter.CURRENT_DIR, 'Data_files', 'vote_store.txt')
        voted_list = []
        if self.check_voter_exists(voterId):
            self.display_candidates()
            print("Caste vote by candidate id number")
            canditate_id = int(input("Enter the canditate ID: "))
            if self.check_candidate_id(canditate_id):
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            voted_dict = json.loads(line)
                            voted_list.append(voted_dict)
                except FileNotFoundError:
                    with open(file_path, 'w') as file:
                        pass
                
                found = False
                for voted in voted_list:
                    if int(voted['id']) == canditate_id:
                        voted['total_vote'] +=1
                        found = True
                        break
                if not found:
                    canditate_vote = {
                        "id": canditate_id,
                        'total_vote': 1
                    }
                    voted_list.append(canditate_vote)

                with open(file_path, 'w') as file:
                    for data in voted_list:
                        data_str = json.dumps(data)
                        file.write(data_str + '\n') 

                print("Vote successfully cast")
            else:
                print("Invalid candidate id")
        else:
            print("Invalid voter id")





    @staticmethod
    def display_candidates():
        file_path = os.path.join(Voter.CURRENT_DIR, "Data_files", "candidatelist.txt")
        with open(file_path, 'r') as file:
            candidates = json.load(file)

        print("Candidate List:")
        print("ID\tName\t\tParty\t\tCandidacy Location")
        print("-" * 80)
        
        for candidate in candidates:
            print(f"{candidate['id']}\t{candidate['name']}\t\t{candidate['party']}\t\t{candidate['candidacy_location']}")

        
    @staticmethod
    def check_candidate_id(candidateID: int) -> bool:
        file_path = os.path.join(Voter.CURRENT_DIR, 'Data_files', 'candidatelist.txt')

        with open(file_path, 'r') as file:
            candidate_list = json.load(file)
        print(candidate_list)

        for candidate_dict in candidate_list:
            if int(candidate_dict['id']) == candidateID:
                return True

        return False

                

    @staticmethod
    def check_voter_exists(voterId: int):
        with open(Voter.VOTER_DETAIL_PATH, 'r') as file:
            for line in file:
                voter_dict = json.loads(line)
                if int(voter_dict['id']) == voterId:
                    return True
                    break








