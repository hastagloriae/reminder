import schedule
import time
from datetime import datetime


def reminder():
    # Выводит уведомление.
    print('Сегодня день который Вы выбрали для напоминания!')


def job(day):
    # вызывает функцию если та совпадает.
    today = datetime.now().day
    if today == day:
        reminder()


def schedule_reminder(day):
    # заставляет работать програму в заданное время.
    person_time = input(f'Введите время для напоминания в формате ЧЧ:MM ')



    schedule.every().day.at(person_time).do(job, day=day)
    return person_time  # Возвращаем время, чтобы использовать его далее


if __name__ == "__main__":
    user_day = int(input("Введите день месяца для напоминания (1-31): "))

    if user_day < 1 or user_day > 31:
        print("Неверный день. Пожалуйста, введите день от 1 до 31.")
    else:
        person_time = schedule_reminder(user_day)

        print(f"Напоминание будет срабатывать каждый {user_day}-й день месяца в {person_time}.")

        while True:
            schedule.run_pending()
            time.sleep(1)


