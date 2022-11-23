#!/usr/bin/env python3
import click
import datetime
import random

@click.command()
@click.option('--path', default='/home/jakub/Desktop/my_file.txt', help='Path to the file')
@click.option('--time',default=1,help='Where to save.')

def save_number(path, time):
    previous_time = datetime.datetime.now()
    while(1):
        current_time = datetime.datetime.now()
        if((current_time - previous_time).seconds >= time):
            random_number = random.random()
            with open(path,'a') as file:
                file.write(str(current_time) + ' : ' + str(random_number)+ '\n')
            previous_time = current_time

    

if __name__ == '__main__':
    save_number()

