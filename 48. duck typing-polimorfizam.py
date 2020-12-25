class visualstudio:
    def mogucnosti(self):
        print("ispravljanje")
        print("predviđanje")
class laptop:
    def code(self,ide):
        ide.mogucnosti()
class pycharm:
    def mogucnosti(self):
        print("ispravljanje")
        print("predviđanje")
        print("debagovanje")
        print("ispravljanje")
ide=visualstudio()
lap1=laptop()
lap1.code(ide)
ide=pycharm() #zamena  je valjda to duck typing
lap1.code(ide)