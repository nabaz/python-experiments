# TODO: finish this
class Contacts:
    def __init__(self, first, last):
        self.first = first
        self.last = last


    @property
    def full_name(self):
        return ("{} {}".format(self.first, self.last))
