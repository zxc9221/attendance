from abc import ABC, abstractmethod
class AttendanceBook(ABC):
    @abstractmethod
    def attendance(self, name, day_of_week):
        pass

    @abstractmethod
    def get_remove_player(self):
        pass