import random


class CoinToss:
    # multi sided coins to be added in the next update
    coin_sides = ["heads", "tails"]

    @classmethod
    def throw_coin(cls):
        result = random.choice(CoinToss.coin_sides)
        return result

    @classmethod
    def toss(cls, multitoss=0):

        result = ""
        multi_result = []

        if multitoss == 1:
            toss = CoinToss.throw_coin()

            result = f"You tossed the coin and it landed on {toss}."

        elif multitoss > 1:
            # remember the second parameter is NOT included, so we need to add to it to toss the coin
            # the number of times we want, not one toss less
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


if __name__ == "__main__":

    # of course some of you are going to try to toss it 1.5 times or toss it an elephant number of times
    try:
        number = int(input("How many times do you want to toss the coin?\n"))
    except ValueError:
        print("The coin just got stuck in mid-air, levitating, looking confused.")

    CoinToss.toss(number)
