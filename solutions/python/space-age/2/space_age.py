'''Program for calculating age on each planets for our solar system.'''
class SpaceAge:
    '''This class have many methods for calculating your age on each planet in our solar system.'''
    def __init__(self, seconds):
        self.seconds = seconds
    def on_mercury(self):
        '''Calculates age on mercury based on a mercury year in seconds and age in seconds.'''
        return round(self.seconds / 7600543.82, 2)
    def on_venus(self):
        '''Calculates age on venus based on a venus year in seconds and age in seconds.'''
        return round(self.seconds / 19414149.05, 2)
    def on_earth(self):
        '''Calculates age on earth based on a earth year in seconds and age in seconds.'''
        return round(self.seconds / 31557600, 2)
    def on_mars(self):
        '''Calculates age on mars based on a mars year in seconds and age in seconds.'''
        return round(self.seconds / 59354032.69, 2)
    def on_jupiter(self):
        '''Calculates age on jupiter based on a jupiter year in seconds and age in seconds.'''
        return round(self.seconds / 374355659.12, 2)
    def on_saturn(self):
        '''Calculates age on saturn based on a saturn year in seconds and age in seconds.'''
        return round(self.seconds / 929292362.88, 2)
    def on_uranus(self):
        '''Calculates age on uranus based on a uranus year in seconds and age in seconds.'''
        return round(self.seconds / 2651370019.33, 2)
    def on_neptune(self):
        '''Calculates age on neptune based on a neptune year in seconds and age in seconds.'''
        return round(self.seconds / 5200418560.03, 2)
    
