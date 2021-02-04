import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
guessed_states = []
while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Pass another state").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("missed_states.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


# this way u can find the cords on the map
# def get_mouse_click_cord(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_cord)
