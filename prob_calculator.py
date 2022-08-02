import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        # parse the parameters using the tuple kwargs
        for key in kwargs:
            for _ in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, nbDraw):
        if nbDraw > len(self.contents):
            return self.contents
        else:
            list_select = []
            for _ in range(nbDraw):
                elt = random.randint(0, len(self.contents) - 1)
                x = self.contents.pop(elt)
                list_select.append(x)
            return list_select


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0
    for _ in range(num_experiments):

        #get a copy from the hat object passed as a parameter
        hat_copy = copy.deepcopy(hat)

        #2:drawing 'num_balls_drawn' balls
        s = hat_copy.draw(num_balls_drawn)

        #3:construct the 'get_balls' dictionary from the list of string s
        get_balls = dict()
        for elt in s:
            get_balls[elt] = get_balls.get(elt, 0) + 1

        #4:chek if we get at least the expected_balls (compare between'get_balls' and 'expected_balls')
        bool = True
        for key in expected_balls:
            if key not in get_balls:
                bool = False
                break
            elif expected_balls[key] > get_balls[key]:
                bool = False
                break

        if bool:
            M = M + 1

    return M / num_experiments
