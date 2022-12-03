from abc import ABC, abstractmethod
from typing import List
from lesson import Lesson
from day import Day
from term import Term
from action import Action


class BasicTimetable(ABC):
    def __init__(self):
        self.timetable = []
        self.dct = {}

    def busy(self, term: Term) -> bool:
        if self.get(term) is not None:
            return True
        return False

##########################################################

    def get(self, term: Term) -> Lesson:
        # if not self.busy(term):
        #     return None

        for lesson in self.timetable:
            if lesson.term == term:
                return lesson
        else:
            return None

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        changes = []

        for _ in actions:
            match _:
                case "d-":
                    changes.append(Action.DAY_EARLIER)
                case "d+":
                    changes.append(Action.DAY_LATER)
                case "t-":
                    changes.append(Action.TIME_EARLIER)
                case "t+":
                    changes.append(Action.TIME_LATER)
                case _:
                    raise ValueError(f"Translation {_} is incorrect")

        return changes

##########################################################

    def perform(self, actions: List[Action]):
        for _ in range(len(actions)):
            ptr = _ % len(self.timetable)

            match actions[_].value:
                case 0:
                    Lesson.earlierDay(self.timetable[ptr])
                case 1:
                    Lesson.laterDay(self.timetable[ptr])
                case 2:
                    Lesson.earlierTime(self.timetable[ptr])
                case 3:
                    Lesson.laterTime(self.timetable[ptr])

##########################################################
