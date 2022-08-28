'''
testing for env set up
'''
import random


def average(d, n):
    '''
    Function to calculate the average
    '''
    avg = d / n
    return avg


def running_average(numbers):
    '''
    Function to find the running average
    '''
    avgs = []
    total = 0
    for i, num in enumerate(numbers):
        total += num
        current_avg = average(total, i + 1)
        avgs.append(current_avg)
    return avgs


def highest_running_average(numbers):
    '''
    Function to find highest running averate
    '''
    averages = running_average(numbers)
    return max(averages)


def generate_number(n):
    '''
    function to generate a random number
    '''
    return random.sample(range(1, 300), n)


if __name__ == '__main__':
    nums = generate_number(100)
    print('Numbers', nums)
    print('Running Average:', running_average(nums))
    print('Highest Average:', highest_running_average(nums))
    print('Hello World')
