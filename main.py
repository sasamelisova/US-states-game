from turtle import Turtle, Screen
import pandas
turtle = Turtle()
screen = Screen()
image = "blank_states_img.gif"
screen.title("U. S. States Game")
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
tim = Turtle()

new_list_of_states = data["state"].to_list()
list_of_guesses = []
score = 0
end_of_game = False
while not end_of_game:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What´s another states name?")
    new_answer_state = answer_state.title()
    list_of_states = data["state"].to_list()
    if new_answer_state == "Exit":
        data = pandas.DataFrame(new_list_of_states)
        data.to_csv("states_to_learn.csv")
        break
    for state_1 in list_of_states:
        if state_1 == new_answer_state:
            new_state = data[data.state == new_answer_state]
            new_state_list = new_state.values.tolist()
            first_value = new_state_list[0]
            x_value = first_value[1]
            y_value = first_value[2]
            tim.hideturtle()
            tim.penup()
            tim.goto(x=x_value, y=y_value)
            tim.write(arg=state_1)
            list_of_guesses.append(state_1)
            score += 1
            new_list_of_states.remove(state_1)















