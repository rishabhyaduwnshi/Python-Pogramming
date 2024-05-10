class iPhone6:
    def home(self):
        print("home is pressed")

class iPhoneX(iPhone6):
    def home(self):
        print("home is touched")
        


#both home functions will preint different output according to their classes
i6 = iPhone6()
i6.home()

ix = iPhoneX()
ix.home()
