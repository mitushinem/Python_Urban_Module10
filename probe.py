# https://sysadminium.ru/python3-thread-synchronization/

########### Event

# from time import sleep
# from threading import Thread, Event, current_thread, active_count
#
# event = Event()
# max_t = 5
#
# def f():
#     thr_num = current_thread().name
#     print(f"Поток {thr_num} запустился. Но ждёт остальных.")
#     event.wait()
#     print(f"Событие наступило! Поток {thr_num} продолжил свою работу")
#
# for i in range(max_t):
#     Thread(target=f).start()
#     sleep(0.2)
#
# if active_count() >= max_t:
#     event.set()






################# Condition
# from time import sleep
# from threading import Thread, Condition
# cond = Condition()
#
# def f1():
#     while True:
#         with cond:
#             cond.wait()
#             print("Получили событие!")
#
# def f2():
#     for i in range(21):
#         if i % 5 == 0:
#             with cond:
#                 cond.notify()
#         else:
#             print(i)
#         sleep(0.2)
#
# Thread(target=f1, daemon=True).start()
# Thread(target=f2).start()






################## Barrier
#
# from time import sleep
# from threading import Thread, Barrier
#
# br = Barrier(3)
#
# a, b = 0, 0
#
#
# def f1(x):
#     global a
#     print('Вычисляем первое число')
#     a = x ** 2
#     sleep(1)
#     br.wait()
#
#
# def f2(x):
#     global b
#     print('Вычисляем второе число')
#     b = x * 2
#     sleep(2)
#     br.wait()


# t1 = Thread(target=f1, args=(3,)).start()
# t2 = Thread(target=f2, args=(7,)).start()
#
# br.wait()
#
# print("Результат = ", a+b)






###############  Semaphore


from time import sleep, time
from threading import Thread, Semaphore, current_thread

s = Semaphore(2)

def f():
   thname = current_thread().name
   start_tread = time()
   with s:
       sleep(1)
       print(f"Время выполнения потока {thname} = {time() - start_tread}")


for i in range(10):
   Thread(target=f).start()









