import random
from models import ResultSet, CoinToss


class TossACoin:
    # TODO: multi sided coins to be added in the next update
    # TODO: figure out if multi sided coin is still a coin or if it becomes a cube

    @classmethod
    def toss(cls, multitoss):

        # lets init the thing that keeps track of all those billions of coins you tossed
        result_set = ResultSet()
        result_set.save()

        if multitoss == 1:
            heads_result = random.choice([True, False])
            tails_result = False if heads_result else True

            toss = CoinToss(result_set=result_set, heads=heads_result, tails=tails_result)
            toss.save()

            winner = 'heads' if toss.heads else 'tails'

            result = f"You tossed the coin and it landed on {winner}."

        elif multitoss > 1:
            # remember the second parameter in range() is NOT included in the resulting range of numbers,
            # so we need to add one to it to get the range of coin toss count we want
            cointosses = range(1, multitoss + 1)

            for _ in cointosses:
                heads_result = random.choice([True, False])
                tails_result = False if heads_result else True

                toss = CoinToss(result_set=result_set, heads=heads_result, tails=tails_result)
                toss.save()

            # count everything
            heads = CoinToss.select().join(ResultSet).where(ResultSet.id == result_set.id).where(CoinToss.heads == "heads").count()
            tails = CoinToss.select().join(ResultSet).where(ResultSet.id == result_set.id).where(CoinToss.tails == "tails").count()

            # if you throw the coin even number of times, you might not get a clear result
            if heads == tails:
                print("The number of heads and tails were the same. The fate is undecided.")
                return

            # set the proper winner to be used laters
            winner = "heads" if heads > tails else "tails"

            # maybe you want to know how many times the winner landed
            winner_count = heads if heads > tails else tails
            loser_count = tails if heads > tails else heads

            result = f"You tossed a coin {multitoss} times and the results are in: \nThe {winner} have it. " \
                     f"The coin landed on {winner} {winner_count} times. " \
                     f"It fell on the other side {loser_count} times."

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
    TossACoin.toss(TossACoin.get_number_of_tosses())
