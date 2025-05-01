class Point:
    points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points.append(self)

    def get_distance_to_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
            print("Передана не точка")
            return None
        return (
            (self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2
        ) ** 0.5

    def display(self):
        print(f"Point({self.x}, {self.y})")

    def get_point_with_max_distance(self):
        max_dist_point = max(
            self.points,
            key=lambda p: (p.get_distance_to_origin(), p.y)
        )
        max_dist_point.display()


if __name__ == '__main__':
    p1 = Point(4, 5)
    p2 = Point(2, 4)
    p3 = Point(5, 1)
    p2.get_point_with_max_distance()
