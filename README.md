# Alice and Bob Game

## Introduction

This project implements a turn-based game between Alice and Bob, where they take turns selecting numbers from an array based on specific rules. The game follows positional game theory principles and the winner is determined based on their accumulated sums.

## Rules of the Game

1. Alice starts first.
2. On their first turn, each player picks the largest number from the array.
3. On subsequent turns, each player must pick the largest available number that has a different parity (odd/even) from their previous choice.
4. If a player cannot make a valid move, they stop playing, and the other player continues if possible.
5. The game ends when all numbers are picked or no valid moves remain.
6. The player with the higher sum wins.
