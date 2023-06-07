"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time


if __name__ == '__main__':
    with Timer() as timer:
        print('Подождем 1 секунду')
        time.sleep(1)
        print('Подождем еще 1 секунду')
        time.sleep(1)
        print('И еще 1 секунду')
        time.sleep(1)
    print("Execution time:", timer.elapsed_time)
