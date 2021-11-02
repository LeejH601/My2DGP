from types import ClassMethodDescriptorType


# class Star:
#     type = 'Star'
#     x = 100

#     def change():
#         x = 200
#         print('x is ', x)



# print('x IS ', Star.x)
# Star.change()
# print('x IS ', Star.x)

# star = Star()
# print('x IS ', star.x)
# star.change()





class Player:
    type = 'Player'

    __instance = None

    def __init__(self):
        self.x = 100
        if self.__instance == None:
            self.__instance = self

    def where(self):
        print(self.x)

player = Player()
player.where()


print(Player.type)

Player.where(Player.__instance)
Player.where(player)