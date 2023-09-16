import pandas
import turtle


screen = turtle.Screen()
image = "Egypt Map.gif"
screen.addshape(image)
map = turtle.Turtle()
map.shape(image)
data = pandas.read_csv("govs-data.csv")
text = turtle.Turtle()
score = 0
correct_guesses = []
FONT = ('Arial', 7, 'bold')
all_govs = data.gov.to_list()


while score < 27:
    answer_gov = screen.textinput(f"{score}/27 Governorate Correct", "What`s the Governorate Name ?").title()
    #print govs not guessed

    if answer_gov == "Exit":
        missing_govs = [gov for gov in all_govs if gov not in correct_guesses]
        print(missing_govs)
        break
    #check correct answer
    row = data[data.gov == answer_gov]
    gov_str = row.gov.to_string(index=False)
    if answer_gov in all_govs:
        if answer_gov not in correct_guesses:
            correct_guesses.append(answer_gov)
            score += 1
            #write correct gusses onto the map
            text.ht()
            text.penup()
            x_int = int(row.x)
            y_int = int(row.y)
            text.goto(x_int, y_int)
            text.write(f"{answer_gov}",align="center", font=FONT)
#check score!
end = turtle.Turtle()
end.penup()
end.write("Well Done!", align="center", font=('Arial', 30, 'bold'))







screen.exitonclick()







