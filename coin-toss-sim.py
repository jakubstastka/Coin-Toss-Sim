import random


class CoinToss:
    # multi sided coins to be added in the next update
    # TODO: figure out if multi sided coin is still a coin or if it becomes a cube
    coin_sides = ["heads", "tails"]

    @classmethod
    def throw_coin(cls):
        result = random.choice(CoinToss.coin_sides)
        return result

    @classmethod
    def toss(cls, multitoss):

        if multitoss == 1:
            toss = CoinToss.throw_coin()
            result = f"You tossed the coin and it landed on {toss}."

        elif multitoss > 1:
            # let's set up the list for all the coin tosses
            multi_result = []

            # remember the second parameter in range() is NOT included in the resulting range of numbers,
            # so we need to add one to it to get the range of coin toss count we want
            cointosses = range(1, multitoss + 1)

            for toss in cointosses:
                result = CoinToss.throw_coin()
                multi_result.append(result)

            # count everything
            heads = multi_result.count("heads")
            tails = multi_result.count("tails")

            # if you throw the coin even number of times, you might not get a clear result
            if heads == tails:
                return f"The number of heads and tails were the same. The fate is undecided."

            # set the proper winner to be used laters
            winner = "heads" if heads > tails else "tails"

            # maybe you want to know how many times the winner landed
            winner_count = heads if heads > tails else tails

            result = f"You tossed a coin {multitoss} times and the results are in: \nThe {winner} have it. " \
                     f"The coin landed on {winner} {winner_count} times."

        # because some people are like this
        elif multitoss == 0:
            result = "You did not even throw the coin. What are you waiting for?"

        elif multitoss < 0:
            result = "You attempted to throw the coin a negative number of times and destroyed the universe."

        else:
            result = "I don't even know what you tried to do."

        print(result)

    @classmethod
    def get_number_of_tosses(cls):
        try:
            number = int(input("How many times do you want to toss the coin?\n"))
        except ValueError:
            print("The coin just got stuck in mid-air, levitating, looking confused.")

        return number


if __name__ == "__main__":
    CoinToss.toss(CoinToss.get_number_of_tosses())
