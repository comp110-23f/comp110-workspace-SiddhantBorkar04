"""Turtle Drawing Assignment."""

__author__ = "730652641"

from turtle import Turtle, done 
leo: Turtle = Turtle()

leo.color("green")
n: int = 0
while n < 200:
    leo.forward(n)
    leo.right(n)
    n += 1

done()