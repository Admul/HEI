from concurrent.futures import thread
from ctypes.wintypes import tagMSG
from logging.handlers import WatchedFileHandler
from re import X
from threading import *
import time
import random
import math

time_sleep = 0.5
refresh = 2

def traveler1(speed, thread): 
    global position1
    global position2
    global position3
    count_1km = 1
    
    while position1 < way:
        global position1
        global position2
        global position3
        
        count = 0
        
        speed = speed * thread
        position1 += speed
        
        count = math.floor(position1/500)
        while count > 0 and position1 >= 500*count and (position2 < 500*count or position3 < 500*count):
            time.sleep(time_sleep)
            
        time.sleep(1)   

def traveler2():
    while position2 < way:
        global x2
        global position1
        global position3

        speed = 8 * x2
        position2 += speed
        
        count = math.floor(position2/500)
        while count > 0 and position2 >= 500*count and (position1 < 500*count or position3 < 500*count):
            time.sleep(time_sleep)
        
        time.sleep(1)

def traveler3():
    while position3 < way:
        global x3
        global position1
        global position2

        speed = 6 * x3
        position3 += speed
        
        count = math.floor(position3/500)
        while count > 0 and position3 >= 500*count and (position1 < 500*count or position2 < 500*count):
            time.sleep(1)
            
        if position1 >= (1000*count_1km) and position2 >= (1000*count_1km) and position3 >= (1000*count_1km):
            count_1km += 1
            get_thread_number()
        
        time.sleep(time_sleep)
        
def get_travelers_positions():
    global position1
    global position2
    global position3
    
    while position1 < way or position2 < way or position3 < way:
        print(f"Путешественник 1:\nПозиция - {position1}:{x1}")
        print(f"Путешественник 2:\nПозиция - {position2}:{x2}")
        print(f"Путешественник 3:\nПозиция - {position3}:{x3}")
        print('*'*50)
        time.sleep(refresh)
    

def get_thread_number():
    thread_numbers = [1, 2, 3]
    
    global x1, x2, x3
    
    x1 = random.choice(thread_numbers)
    
    choice = random.choice(thread_numbers)
    while choice == x1:
        choice = random.choice(thread_numbers)
    x2 = choice
        
    choice = random.choice(thread_numbers)
    while choice == x1 or choice == x2:
        choice=random.choice(thread_numbers)
    x3 = choice

way = 5 * 1000

position1 = 0
position2 = 0
position3 = 0

x1 = 0
x2 = 0
x3 = 0
get_thread_number()

th1 = Thread(target=traveler1)
th2 = Thread(target=traveler2)
th3 = Thread(target=traveler3)
th4 = Thread(target=get_travelers_positions)

th1.start()
th2.start()
th3.start()
th4.start()