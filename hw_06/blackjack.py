suit_d = {'Spade': 0, 'Heart': 1, 'Diamond': 2, 'Club': 3}
rank_d = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13
}

class card(object):
    def read(self):
        self.suit, self.rank = map(str, input().split())
    def display(self):
        if self.rank == 'A':
            print("{} 1 11".format(self.suit))
        else:
            if self.rank in ['J', 'Q', 'K', '10']:
                self.point = 10
            elif ord(self.rank) in range(ord('2'), ord('9') + 1):      # ord()是将某个字符转换为其ascii码的函数
                self.point = int(self.rank)
            print("{} {}".format(self.suit, self.point))

    def get_point(self):    # 处理除了Ace之外的情况
        if self.rank == '10':
            return 10
        elif ord(self.rank) in range(ord('2'), ord('9') + 1):      # ord()是将某个字符转换为其ascii码的函数
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K', '10']:
            return 10

class hand(list):   #继承list类，其中的元素为card类型
    # def add_card(self, c: card):
    #     self.append(c)
    def display(self):      #需要调整输出的格式，在一行内输出
        self.hand_sort()
        for x in self[:-1]:
            print("{}{}".format(x.suit, x.rank), end = ' ')
        print("{}{}".format(self[-1].suit, self[-1].rank))
        self.disp_result()
    def count_pnt(self):
        ttl_pnt = 0
        ace_num = 0
        for x in self:
            if x.rank != 'A':
                ttl_pnt += x.get_point()
            elif x.rank == 'A':
                ace_num += 1
                ttl_pnt += 11
        while(ace_num > 0):
            if (ttl_pnt <= 21):
                break
            else:
                ace_num -= 1
                ttl_pnt -= 10
        return ttl_pnt
    def hand_sort(self):
        self.sort(key = lambda x: (rank_d[x.rank], suit_d[x.suit]))  
    def disp_result(self):
        point = self.count_pnt()
        if point > 21:
            print('Bust')
        elif len(self) == 2 and point == 21:
            print('Blackjack')
        else :
            print(point)
            
class player(object):
    h = hand()
    def init(self):
        c1 = card()
        c1.read()
        c2 = card()
        c2.read()
        self.h.extend([c1, c2])
    def hit(self, c):
        print('Hit')
        self.h.append(c)
        c.display()
    def stand(self):
        print('Stand')
        self.h.display()

p = player()
p.init()
while p.h.count_pnt() < 17:
    c = card()
    c.read()
    p.hit(c)
p.stand()