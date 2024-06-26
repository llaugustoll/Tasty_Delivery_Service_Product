from abc import abstractmethod, ABC


class IBaseRepository(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, obj):
        raise NotImplementedError
