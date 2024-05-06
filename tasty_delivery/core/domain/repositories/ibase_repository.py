from abc import abstractmethod, ABC


class IBaseRepository(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError


