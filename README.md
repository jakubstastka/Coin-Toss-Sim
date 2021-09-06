# Coin Toss Simulator

*Jaskier, don't even*

Tossing a coin for heads/tails is as old as coins themselves, I guess.

This allows you to throw really a lot of coins, even {insert a large number here}.

Now uses a sqlite3.

## Roadmap for Coin Toss Simulator project

- [X] Make a coin toss app to decide heads/tails when run. (DONE)
- [X] Make "best out of three" coin toss. (DONE)
- [X] User specifies how many tosses they want to do. The script tosses the coin N times (saves the result into a list), then counts occurences, compares and decides for a winner. (DONE)
- [X] Implement SQLite support for coin tosses, so it does not crash when you flip the coin 100 milion times. (DONE using Peewee ORM)
- [ ] The script should remember if you try to cheat it - toss the coin zero number of times, negative number of times, or you try to feed the input different data type other than INT. 
- [ ] Implement Lady Luck type of figure. There should be a chance that she would favour one side of coin over the other. 
- [ ] Lady Luck will remember if you try to toss the coin "wrong" amount of times (zero, negative number, etc.). With rising number of "wrong" tosses there will be a higher chance of her not allowing you to toss the coin. Also random events will occur - coin dissappears, turns into something else, etc. 
- [ ] Implement a formula, that will check "good" tosses against "wrong" tosses. 
- [ ] When treshhold in point 8 is reached, a text-based adventure game will open up. 

More to come.

### Credits and thanks
This project couldn't have been done without me, so I would like to thank me for writing it and navigating bravely the treatcherous waters of it all.

### Warnings
The coins lie, do not trust them.