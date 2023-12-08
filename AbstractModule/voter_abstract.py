from abc import ABC, abstractmethod

class VoterAbstract(ABC):
    @abstractmethod
    def voter_registration(self):
        """voter can register them by age, address, name"""
        pass

    @abstractmethod
    def update_voter_detail(self):
        """User can change their voter identity"""
        pass

    @abstractmethod
    def search_voter(self):
        """Search voter detail by voter number """
        pass
    
    @abstractmethod
    def caste_vote(self):
        """cast the vote on the designated date by allowing the user to login using the login credentials (VoterSNO and Password)"""
        pass


    @abstractmethod
    def view_result(self):
        """display the result"""
        pass
