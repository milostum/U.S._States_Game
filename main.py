import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#      []       {}
data = pandas.read_csv("50_states.csv")

all_states = data["state"].to_list()

s = 0
incorrect = 5
guessed_states = []
text = "Guess the State"
br = -1
while incorrect > 0 and len(guessed_states) < 50:
    answer_state = screen.textinput(title=text, prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        x = []
        y = []
        for state in all_states:
            br += 1
            if state not in guessed_states:
                missing_states.append(state)
                x_cor = data.x
                y_cor = data.y
                x.append(x_cor[br])
                y.append(y_cor[br])
        new_dict = {
            "state": missing_states,
            "x": x,
            "y": y
        }
        new_data = pandas.DataFrame(new_dict)
        new_data.to_csv("states_to_learn.csv")
        screen.tracer(0)
        for i in range(len(missing_states)):
            exit_t = turtle.Turtle()
            exit_t.color("red")
            exit_t.hideturtle()
            exit_t.penup()
            exit_t.goto(x[i], y[i])
            exit_t.write(f"{missing_states[i]}", align="center", font=("Times", 12, "normal"))
        screen.update()
        break

    if (answer_state in all_states) and not(answer_state in guessed_states):
        s += 1
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        state_x = int(state.x)
        state_y = int(state.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(f"{answer_state}", align="center", font=("Times", 12, "normal"))
    elif not(answer_state in guessed_states):
        incorrect -= 1
    text = f"{s}/50 States Correct"
if incorrect == 0:
    turtle.write("Game Over! You are fail.", align="center", font=("Times", 40, "bold"))
screen.exitonclick()


