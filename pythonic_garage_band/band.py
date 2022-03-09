from abc import ABC, abstractmethod

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members 
        Band.instances.append(self)
        
    def play_solos(self):
        all_solo = []
        for member in self.members:
            all_solo.append(member.solo)
        return all_solo

    def __str__(self):
        return f'{self.name}'


    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician():
    members=[]
    def __init__(self, name, kind, instrument, solo):
        self.name = name
        self.kind = kind
        self.instrument = instrument
        self.solo = solo
        Musician.members.append(self)
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}" 

    def __repr__(self):
        return f"{self.kind} instance. Name = {self.name}"
    
    def get_instrument(self):
        return f'{self.instrument}'

    def play_solo(self):
        return f'{self.solo}'


class Guitarist(Musician):
    #Class Variables
    musician_kind= 'Guitarist'
    musician_instrument = 'guitar'
    musician_solo = 'face melting guitar solo'
    

    def __init__(self, name):
        super().__init__(name, Guitarist.musician_kind, Guitarist.musician_instrument, Guitarist.musician_solo)
        

class Bassist(Musician):
    #Class Variables
    musician_kind= 'Bassist'
    musician_instrument = 'bass'
    musician_solo = 'bom bom buh bom'
    

    def __init__(self, name):
        super().__init__(name, Bassist.musician_kind, Bassist.musician_instrument, Bassist.musician_solo)


class Drummer(Musician):
    #Class Variables
    musician_kind= 'Drummer'
    musician_instrument = 'drums'
    musician_solo = 'rattle boom crash'
    

    def __init__(self, name):
        super().__init__(name, Drummer.musician_kind, Drummer.musician_instrument,Drummer.musician_solo)




# if __name__ == "__main__":  
#     band1 = Band("hhhh", ["s"])
#     band2 = Band("s", ["s"])

#     print(Band.to_list())
