class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print('.', end='')

# ^^ you are given this

# vv

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    """ Represented as a list of lines. """
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))



# To avoid excessive generation of same template,
# when you implement same object several times, using cache
class LineToPointAdapter:
    cache = {}

    def __init__(self, line):

        # hash(): https://www.programiz.com/python-programming/methods/built-in/hash
        self.h = hash(line)  # will calculate the unique value of the line
        if self.h in self.cache:
            return

        super().__init__()

        print(f'Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        # no longer use self, since we don't use same point anymore
        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    # https://www.programiz.com/python-programming/iterator
    def __iter__(self):
        return iter(self.cache[self.h])


def draw(rcs):
    print('\n\n--- Drawing some stuff ---\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)



if __name__ == "__main__":
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rcs)
    draw(rcs)