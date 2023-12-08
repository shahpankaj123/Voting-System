from abc import ABC, abstractmethod

class AdminAbstract(ABC):
    @abstractmethod
    def generate_id(self):
        '''generate unique id'''
        pass
    
    @abstractmethod
    def create_admin(self):
        '''admin can create new admin'''
        pass

    @abstractmethod
    def admin_login(self):
       '''login admin'''
       pass
        
    @abstractmethod  
    def election_schedule(self):
        """Admin can schedule the election date"""
        pass

    @abstractmethod
    def canditate_registration(self):
        """Admin can register the canditate for the election"""
        pass
    
    @abstractmethod
    def update_canditate():
        '''Admin can update the details of canditate of the election'''
        pass

    @abstractmethod
    def del_canditate(self):
        '''delete candidate'''
        pass

 