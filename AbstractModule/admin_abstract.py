from abc import ABC, abstractmethod

class AdminAbstract(ABC):
    @abstractmethod
    def election_schedule():
        """Admin can schedule the election date"""
        pass

    @abstractmethod
    def canditate_registration():
        """Admin can register the canditate for the election"""
        pass