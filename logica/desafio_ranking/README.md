# Hero Ranking Calculator

A simple JavaScript function that calculates a hero's ranking based on their victories and defeats.

## Description

This script contains a function `calculateRanking()` that takes two parameters:
- victories: Number of victories the hero has achieved
- defeats: Number of defeats the hero has suffered

It calculates the balance (victories - defeats) and determines the hero's ranking tier based on the following criteria:

| Victories | Ranking |
|-----------|---------|
| 0-10 | Ferro |
| 11-20 | Bronze |
| 21-50 | Prata |
| 51-80 | Ouro |
| 81-90 | Diamante |
| 91-100 | Lendário |
| 101+ | Imortal |

## Usage
javascript
calculateRanking(victories, defeats)
Example:
```javascript
console.log(calculateRanking(100, 5))
```