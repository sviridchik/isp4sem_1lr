import matplotlib
matplotlib.use('Agg')
import turtle

smiles = turtle.Turtle()
smiles.penup()
smiles.goto(-75,150)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(75,150)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(0,0)
smiles.pendown()
smiles.circle(100,90)

smiles.penup()
smiles.setheading(180)
smiles.goto(0,0)
smiles.pendown()
smiles.circle(-100,90)