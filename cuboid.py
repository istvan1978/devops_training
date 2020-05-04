class Cuboid:
    def __init__(self, a, b, c):
        # Constructor of the class
        self.a = a
        self.b  = b
        self.c = c

    def surface(self):
        # Counts the surface of the Cuboid object
        top_area   = self.a * self.b
        front_area = self.a * self.c
        side_area  = self.b  * self.c
        return 2 * (top_area + front_area + side_area)

    def volume(self):
        # Counts the volume of the Cuboid object
        return self.a * self.b * self.c

    def help(self):
        print(self.surface().__doc__)
        print(self.volume().__doc__)

def main():
    cuboid = Cuboid(2, 3, 4)
    print("surface = ", cuboid.surface())
    print("volume = ", cuboid.volume())
    print("help = ", cuboid.help())

if __name__=="__main__":
    main()