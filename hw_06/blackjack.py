class card(object):
    def read(self):
        self.suit, self.rank = map(str, input().split())
    def display(self):
        if self.rank == 'A':
            print("{} 1 11".format(self.suit))
        else:
            if ord(self.rank) in range(ord('2'), ord('9') + 1):      # ord()是将某个字符转换为其ascii码的函数
                self.point = int(self.rank)
            elif self.rank in ['J', 'Q', 'K', '10']:
                self.point = 10
            print("{} {}".format(self.suit, self.point))

    def get_point(self):    # 处理除了Ace之外的情况
        if ord(self.rank) in range(ord('2'), ord('9') + 1):      # ord()是将某个字符转换为其ascii码的函数
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K', '10']:
            return 10

class hand(list):   #继承list类，其中的元素为card类型
    # def add_card(self, c: card):
    #     self.append(c)
    def display(self):      #需要调整输出的格式，在一行内输出
        for x in self[:-1]:
            print("{}{}".format(x.suit, x.rank), end = ' ')
        print("{}{}".format(self[-1:].suit, self[-1:].rank))
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
            
class player(object):
    h = hand()
    def hit(self, c):
        print('Hit')
        c = card()
        c.read()
        self.h.append(c)
        c.display()
    def stand(self, c):
        print('Stand')
        self.h.display()
