#!/usr/bin/env python
# -*- coding:utf-8 -*-


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz_buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print("not fizz not buzz")


if __name__ == "__main__":

    while 1:
        try:
            num = input("type number:")

            fizz_buzz(int(num))

        except:
            if num == "exit":
                break
            print("please type numeric")
