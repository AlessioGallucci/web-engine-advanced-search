# https://en.wikipedia.org/wiki/Natural_language_processing

class Operator:
    """
    This is the main class for an operator
    """
    def __init__(self):
        self.synonyms = None
        pass

    def _representation(self):
        pass

    def check_synonyms(self, ele):
        if ele in self.synonyms:
            return True
        else:
            return False


class And(Operator):
    """
    This is the plus operator
    """
    def __init__(self):
        Operator.__init__(self)
        self.synonyms = ['and', 'plus']

    def _representation(self):
        return '+'




class And(Operator):
    """
    This is the plus operator
    """
    def __init__(self):
        Operator.__init__(self)
        self.synonyms = ['and', 'plus']



def built_query(query_natural_language):
    operators = list()
    operators.append(And())

    query = "https://www.google.nl/search?q="

    qnl_split = query_natural_language.split()
    assert qnl_split[0] == 'search'

    query +=


    return query




if __name__ == "__main__":
    query_natural_language = "search spinoza exclude baruch"

    built_query(query_natural_language=query_natural_language)
