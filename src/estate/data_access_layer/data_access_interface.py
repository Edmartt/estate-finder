

from abc import ABC, abstractmethod


class DataAccessInterface(ABC):

    @abstractmethod
    def read_properties_without_filters(self, *args: tuple):
        pass

    @abstractmethod
    def read_properties_with_filters(self, *args):
        pass
