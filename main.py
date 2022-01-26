import turtle
import random

stack = []


# max_it = maximum iterations, word = starting axiom such as 'F', proc_rules are the rules that
# change the elements of word if it's key is found in dictionary notation, x and y are the
# coordinates, and turn is the starting angle

def createWord(max_it, word, proc_rules, x, y, turn):
    turtle.up()
    turtle.home()
    turtle.goto(x, y)
    turtle.right(turn)
    turtle.down()

    t = 0
    while t < max_it:
        word = rewrite(word, proc_rules)
        drawit(word, 5, 20)
        t = t + 1


def rewrite(word, proc_rules):
    # rewrite changes the word at each iteration depending on proc_rules

    wordList = list(word)

    for i in range(len(wordList)):
        curChar = wordList[i]
        if curChar in proc_rules:
            wordList[i] = proc_rules[curChar]

    return "".join(wordList)


def drawit(newWord, d, angle):
    # drawit 'draws' the words

    newWordLs = list(newWord)
    for i in range(len(newWordLs)):
        cur_Char = newWordLs[i]
        if cur_Char == 'F':
            turtle.forward(d)
        elif cur_Char == '+':
            turtle.right(angle)
        elif cur_Char == '-':
            turtle.left(angle)
        elif cur_Char == '[':
            state_push()
        elif cur_Char == ']':
            state_pop()


def state_push():
    global stack

    stack.append((turtle.position(), turtle.heading()))


def state_pop():
    global stack

    position, heading = stack.pop()

    turtle.up()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.down()


def randomStart():
    # x can be anywhere from -300 to 300, all across the canvas
    x = random.randint(-300, 300)

    # these are trees, so we need to constrain the 'root' of each
    # to a fairly narrow range from -320 to -280
    y = random.randint(-320, -280)

    # heading (the angle of the 'stalk') will be constrained
    # from -80 to -100 (10 degrees either side of straight up)
    heading = random.randint(-100, -80)

    return ((x, y), heading)


def main():
    # define the list for rule sets.
    # each set is iteration range [i_range], the axiom and the rule for making a tree.
    # the randomizer will select one of these for building.

    rule_sets = []
    rule_sets.append(((3, 5), 'F', {'F': 'F[+F][-F]F'}))
    rule_sets.append(((4, 6), 'B', {'B': 'F[-B][+ B]', 'F': 'FF'}))
    rule_sets.append(((2, 4), 'F', {'F': 'FF+[+F-F-F]-[-F+F+F]'}))

    # define the number of trees to build
    tree_count = 50

    # speed up the turtle
    turtle.tracer(10, 0)

    # for each tree...
    for x in range(tree_count):
        # pick a random number between 0 and the length
        # of the rule set -1 - this results in selecting
        # a result randomly from the list of possible rules.

        rand_i = random.randint(0, len(rule_sets) - 1)
        selected_ruleset = rule_sets[rand_i]

        # unpack the tuple stored for this ruleset
        i_range, word, rule = selected_ruleset

        # pick a random number inside the given iteration_range to be the
        # iteration length for this command list.
        low, high = i_range
        i = random.randint(low, high)

        # get a random starting location and heading for the tree
        start_position, start_heading = randomStart()

        # unpack the x & y coordinates from the position
        start_x, start_y = start_position

        # build the current tree
        createWord(i, word, rule, start_x, start_y, start_heading)


if __name__ == '__main__': main()
