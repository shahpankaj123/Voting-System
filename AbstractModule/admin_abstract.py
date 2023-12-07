from abc import ABC, abstractmethod

class AdminAbstract(ABC):
    @abstractmethod
    def create_admin():
        '''admin can create new admin'''
        pass

    @abstractmethod
    def admin_login():
       '''login admin'''
       pass
        
    @abstractmethod  
    def election_schedule():
        """Admin can schedule the election date"""
        pass

    @abstractmethod
    def canditate_registration():
        """Admin can register the canditate for the election"""
        pass

    @abstractmethod
    def del_canditate():
        '''delete candidate'''
        pass

 