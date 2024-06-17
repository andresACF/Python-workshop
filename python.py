class MyClass:
    def __init__(self):
        self.myFav = {'Paris': 500, 'NYC': 600}

    def get_extraCost(self, dist):
        return self.myFav.get(dist, 0)

    def validThis(self, dist):
        return isinstance(dist, str)


class Passenger:
    def __init__(self, num):
        self.num = num

    def validNumber(self):
        return isinstance(self.num, int) and 0 < self.num <= 80

    def forHereDiscount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        else:
            return 0.0


class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        return isinstance(self.dur, int) and self.dur > 0

    def getFee(self):
        return 200 if self.dur < 7 else 0

    def getTheBestPromoEver(self, num):
        return 200 if self.dur > 30 or num == 2 else 0


class VacationPackage:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.myClass = MyClass()
        self.passenger = Passenger(num)
        self.totalTime = TotalTime(dur)
        self.dist = dist

    def sum(self):
        if (not self.myClass.validThis(self.dist) or
            not self.passenger.validNumber() or
                not self.totalTime.is_valid_total_time()):
            return -1

        numberTotal = self.costBas
        numberTotal += self.myClass.get_extraCost(self.dist)
        numberTotal += self.totalTime.getFee()
        numberTotal -= self.totalTime.getTheBestPromoEver(self.passenger.num)

        discount = self.passenger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)
        return max(int(numberTotal), 0)


def main():
    dist = "Paris"
    num = 4
    dur = 10

    calculator = VacationPackage(dist, num, dur)
    cost = calculator.sum()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()
