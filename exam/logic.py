import os
import random


class Game2048:

    def __init__(self):
        self.__plate = 0
        self.__new_nums = []
        self.__rows_count = 4
        self.__cols_count = 4
        self.__signs_to_move = "wasd"
        self.__score = 0
        self.field = []

        self.init_field()
        self.init_new_nums()
        self.game_process()

    @property
    def score(self):
        return self.__score

    def init_field(self):
        for row_num in range(self.__rows_count):
            self.field.append([])
            for col_num in range(self.__cols_count):
                self.field[row_num].append(self.__plate)

    def init_new_nums(self):
        for _ in range(9):
            self.__new_nums.append(2)
        self.__new_nums.append(4)

    def new_num_appear(self):
        free_plates = []
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 0:
                    free_plates.append((i, j))

        random_free_coords = free_plates[random.randrange(0, len(free_plates))]
        random_number = self.__new_nums[random.randrange(0, len(self.__new_nums))]
        self.field[random_free_coords[0]][random_free_coords[1]] = random_number

    def game_process(self):
        self.new_num_appear()

        while not self.is_game_over():
            self.clear_console()
            print(f"Score: {self.__score}")
            print()
            for row in self.field:
                print(row)
            print()

            while True:
                sign = input("Enter w to move up, s to move down, a to move left, d to move right: ")
                if sign in self.__signs_to_move:
                    break
                else:
                    print("The sign must be in 'wasd': w to move up, s to move down, a to move left, d to move right")
                    continue

            if sign == "a":
                self.shift_plates()
            elif sign == "d":
                self.horizontal_mirror()
                self.shift_plates()
                self.horizontal_mirror()
            elif sign == "w":
                self.transpose_field()
                self.shift_plates()
                self.transpose_field()
            elif sign == "s":
                self.transpose_field()
                self.horizontal_mirror()
                self.shift_plates()
                self.horizontal_mirror()
                self.transpose_field()

            self.new_num_appear()

    def shift_plates(self):
        for row in self.field:
            changes = 1
            sums = 0
            while changes != 0:
                changes = 0
                for j in range(self.__cols_count - 1):
                    if row[j + 1] == 0:
                        continue
                    elif row[j] == 0:
                        row[j] = row[j + 1]
                        row[j + 1] = 0
                        changes += 1
                    elif row[j] == row[j + 1] and sums < 1:
                        row[j] += row[j + 1]
                        row[j + 1] = 0
                        self.__score += row[j]
                        changes += 1
                        sums += 1

    def horizontal_mirror(self):
        for row in self.field:
            row[0], row[-1] = row[-1], row[0]
            row[1], row[2] = row[2], row[1]

    def transpose_field(self):
        for i in range(self.__rows_count):
            for j in range(self.__cols_count - i):
                self.field[i][j + i], self.field[j + i][i] = self.field[j + i][i], self.field[i][j + i]

    def is_game_over(self) -> bool:
        # self.new_num_appear() execute with ValueError:
        # ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
        # ValueError: empty range for randrange() (0, 0, 0)
        return False

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    game = Game2048()
    # game.field[0][0] = 4
    # game.field[1][2] = 8
    # print()
    # for row in game.field:
    #     print(row)
    # print()
    # game.new_num_appear()
