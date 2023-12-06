from abc import ABC, abstractmethod

class Voter(ABC):
    @abstractmethod
    def voter_registration():
        """voter can register them by age, address, name"""
        pass

    @abstractmethod
    def update_voter_detail():
        """User can change their voter identity"""
        pass

    @abstractmethod
    def search_voter():
        """Search voter detail by voter number """
        pass
    
    @abstractmethod
    def caste_vote():
        """cast the vote on the designated date by allowing the user to login using the login credentials (VoterSNO and Password)"""
        pass


    @abstractmethod
    def vote_result():
        """display the result"""
        pass