from typing import List
from day import Day
from term import Term
from lesson import Lesson
from action import Action


class TimetableWithoutBreaks(object):
    lessons = []

    """ Class containing a set of operations to manage the timetable """

##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if fullTime:
            pass
        else:
            pass

        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
fullTime : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""

##########################################################

    def busy(self, term: Term) -> bool:
        for lesson in self.lessons:
            if lesson.term.day == term.day and term.hour == term.hour and lesson.term.minute == term.minute:
                return True
            return False

        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
"""

##########################################################

    def put(self, lesson: Lesson) -> bool:
        pass

        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
"""

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        pass

        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
"""

##########################################################

    def perform(self, actions: List[Action]):
        pass

        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
"""

##########################################################

    def get(self, term: Term) -> Lesson:
        pass

        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
"""

##########################################################
    def __str__(self):
        pass
