from BasicTerm import BasicTerm


class Break:
    def __init__(self, term: BasicTerm):
        if type(term) is not BasicTerm:
            raise TypeError("'term' musi być typu 'BasicTerm'.")

        self.term = term

    def __str__(self):
        return "---"

    def getTerm(self):
        return self.term
