from admin import Admin
from voter import Voter


def main():
    admin_user = Admin()
    voter_user=Voter()

    while True:
        print("\n=== Voting Management System ===")
        print("1. Create New admin")
        print("2. Election Schedule")
        print("3. Candidacy Register")
        print("4. Update Candidacy Detail")
        print("5. Delete Candidacy Detail")
        print("6. Voter User Registration")
        print("7. Update Voter Details")
        print("8. Search Voter Detail")
        print("9. Caste your vote")
        print("10. See Result")
        print("11. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            admin_user.create_admin()
            
        elif choice == '2':
            admin_user.election_schedule()

        elif choice == '3':
            admin_user.canditate_registration()
        elif choice == '4':
            admin_user.update_canditate()
        elif choice == '5':
            admin_user.del_canditate()
            
        elif choice == '6':
            voter_user.voter_registration()
        elif choice == '7':
            voter_user.update_voter_detail() 
        elif choice == '8':
            voter_user. search_voter()  
        elif choice == '9':
            voter_user.caste_vote()
        elif choice == '10':
            voter_user.view_result()                   
        elif choice == '11':
            print("Exiting Library Management System. Goodbye!")
            
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()