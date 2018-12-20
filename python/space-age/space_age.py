class SpaceAge(object):
    ORBITAL_PERIOD = {
    'earth' :1,
    'mercury':0.2408467,
    'venus':0.61519726,
    'mars':1.8808158,
    'jupiter':11.862615,
    'saturn':29.447498,
    'uranus':84.016846,
    'neptune':164.79132
    }
    def __init__(self, seconds):
        self.seconds = seconds
        self.earthYear = seconds/31557600
        for (planet, period) in self.ORBITAL_PERIOD.items():
            planetOld = lambda p = period:round(self.earthYear/p,2)
            setattr(self,'on_'+planet,planetOld)