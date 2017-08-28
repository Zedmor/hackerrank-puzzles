class Clock:
    def __init__(self, hrs, mins):
        mins+=hrs*60
        self.hrs= mins//60
        self.mins=mins-mins//60*60
    def __repr__(self):
        return("%02d:%02d" % (self.hrs,self.mins))
    def add(self, toadd):
        self.mins+=self.hrs*60+toadd
        self.hrs = self.mins // 60
        self.mins = self.mins - self.mins // 60 * 60
        return ("%02d:%02d" % (self.hrs, self.mins))
str(Clock(8,67))