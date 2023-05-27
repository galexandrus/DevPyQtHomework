import random


class Game2048:

    def __init__(self):

        self.__plate = 0
        self.__new_nums = []
        self.__rows_count = 4
        self.__cols_count = 4
        self.__signs_to_move = "wasdцфыв"
        self.__your_score = 0
        self.__top_score = [0, 0, 0, 0, 0]
        self.is_game_over = False
        self.field = []

        self.init_field()
        self.init_new_nums()

    @property
    def signs_to_move(self):
        return self.__signs_to_move

    @property
    def your_score(self):
        return self.__your_score

    @property
    def top_score(self):
        return self.__top_score

    @top_score.setter
    def top_score(self, score_list: list) -> None:
        for i in range(5):
            self.__top_score[i] = score_list[i]

    def update_top_score(self) -> None:
        """
        Обновление списка лучших результатов

        :return: None
        """
        for score_index in range(len(self.top_score)):
            if self.your_score > self.top_score[score_index]:
                self.__top_score.insert(score_index, self.your_score)
                self.__top_score.pop()
                break

    def init_field(self) -> None:
        """
        Инициализация игрового поля

        :return: None
        """
        for row_num in range(self.__rows_count):
            self.field.append([])
            for col_num in range(self.__cols_count):
                self.field[row_num].append(self.__plate)

    def init_new_nums(self) -> None:
        """
        Подготовка списка элементов для вставки в игровое поля при каждом ходе

        :return: None
        """
        for _ in range(9):
            self.__new_nums.append(2)
        self.__new_nums.append(4)

    def check_free_plates(self) -> list:
        """
        Составление списка свободных ячеек

        :return: list
        """
        free_plates = []
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 0:
                    free_plates.append((i, j))
        return free_plates

    def new_num_appear(self) -> bool:
        """
        Появление нового значения на игровом поле при совершении хода

        :return: bool
        """
        free_plates = self.check_free_plates()

        try:
            random_free_coords = free_plates[random.randrange(0, len(free_plates))]
        except ValueError:
            return False

        random_number = self.__new_nums[random.randrange(0, len(self.__new_nums))]
        self.field[random_free_coords[0]][random_free_coords[1]] = random_number

        return True

    def turn(self, sign: str) -> None:
        """
        Описание одного хода

        :param sign: str - символ, который укажет направление смещения
        :return: None
        """
        if sign in "aф":
            self.shift_plates()
        elif sign in "dв":
            self.horizontal_mirror()
            self.shift_plates()
            self.horizontal_mirror()
        elif sign in "wц":
            self.transpose_field()
            self.shift_plates()
            self.transpose_field()
        elif sign in "sы":
            self.transpose_field()
            self.horizontal_mirror()
            self.shift_plates()
            self.horizontal_mirror()
            self.transpose_field()
        elif sign is None or sign not in self.signs_to_move:
            raise ValueError("Sign must be in 'wasdцфыв'")

    def shift_plates(self) -> None:
        """
        Смещение плиток влево

        :return: None
        """
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
                        self.__your_score += row[j]
                        changes += 1
                        sums += 1

    def horizontal_mirror(self) -> None:
        """
        Зеркальное отображение поля. Используется для хода вправо и вниз

        :return: None
        """
        for row in self.field:
            row[0], row[-1] = row[-1], row[0]
            row[1], row[2] = row[2], row[1]

    def transpose_field(self) -> None:
        """
        Транспонирование игрового поля. Используется для хода вверх и вниз

        :return: None
        """
        for i in range(self.__rows_count):
            for j in range(self.__cols_count - i):
                self.field[i][j + i], self.field[j + i][i] = self.field[j + i][i], self.field[i][j + i]
