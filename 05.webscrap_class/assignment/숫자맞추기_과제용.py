import random as rd

class random_number_game:
    def __init__(self):
        self.random_num = rd.randint(1, 100)
        self.att_num = []

    def set_game(self):
        self.random_num = rd.randint(1, 100)
        self.att_num = []
        print('세로운 숫자가 설정 되었습니다.')

    def guess(self, num):
        self.att_num.append(num)

        if num < self.random_num:
            print('높은 숫자를 입력하세요.')
        elif num > self.random_num:
            print('낮은 숫자를 입력하세요.')
        else:
            print(f"정답입니다! {len(self.att_num)}번 만에 맞추셨습니다.")
            self.show_att_num()
            return 1
        return 0
    
    def show_att_num(self):
        print('입력한 숫자 목록 입니다.')
        for i in range(len(self.att_num)):
            if i == len(self.att_num) - 1:
                print(self.att_num[i])
            else:
                print(self.att_num[i], end=' - ')

    def guess_chk(self):
        if len(self.att_num) >= 10:
            self.show_att_num()
            if input('시도 회수 초과 되었습니다.\n다시 시작하시겠습니까? (y/n) >> ').lower() == 'y':
                print(f'정답은 = {self.random_num}')
                self.set_game()
                return True
            else:
                print(f'정답은 = {self.random_num}')
                return False
        else:
            return True





if __name__ == '__main__':
    game = random_number_game()

    print('게임을 시작합니다!')
    while game.guess_chk():
        num = int(input('숫자를 입력하세요. (1 ~ 100)>> '))

        if num < 0 or num > 100:
            print('숫자를 다시 입력하세요. ')
            continue

        if game.guess(num):
            if input('다시 하시겠습니까? (y/n)').lower() == 'y':
                game.set_game()
            else:
                print('게임을 종료합니다.')
                break
            