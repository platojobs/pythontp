import  pygame,sys

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()



# ai = AlienInvasion()
# ai.run_game()
# s = repr(ai)
# print(s)

"""
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

tup = tuple('string')
print(tup)

tup = tuple(['foo',[1,2],True])
tup[1].append(3)
print(tup)


pro = list(range(10))
print(pro)

b_list = ['foo','foo','baz']
b_list.append('cctv')
print(b_list)

list_unit =  [4, None, 'foo'] + [7, 8, (2, 3)]
print(list_unit)

list_unit.extend([17,18,(12,13)])
print(list_unit)
"""

a = [7,2,5,1,3]
a.sort()
print(a)

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)

author = 'piglei'
print('Hello,{}!'.format(author))

