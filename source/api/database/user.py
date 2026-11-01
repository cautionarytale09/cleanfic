import persistent

class ProfilePicture(persistent.Persistent):
    # There comes a time when you must admit that some things are better left for future you
    pass

class Profile(persistent.Persistent):

    def __init__(self, linkedUser : User, name : str, profilePicture : ProfilePicture):
        self.linkedUser = linkedUser
        self.name = name
        self.profilePicture = profilePicture
        
class User(persistent.Persistent):
    mainProfile : Profile
    profiles : [Profile]

    def __init__(self, mainProfile):
        self.mainProfile = mainProfile
        self.profiles = [mainProfile]
    
    def addProfile(self, profile : Profile):
        self.profiles.append(profile)
    
    def removeProfile(self, profile : Profile):
        self.profiles.remove(profile)
    
    def editProfile(self, oldProfile : Profile, newProfile : Profile):
        i = 0
        for profile in self.profiles:
            if profile == oldProfile:
                self.profiles[i] = newProfile
                if self.mainProfile == oldProfile:
                    self.mainProfile = self.profiles[i]
            i = i + 1
        


