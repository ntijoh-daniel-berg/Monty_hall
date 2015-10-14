class Door(object):

    def __init__(self, secret):
        self.secret = secret
        self.is_picked = False

    def pick(self):
        self.is_picked = True

    @property
    def is_car(self):
        return self.secret == 'car'
