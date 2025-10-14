# Hero Class Challenge

A JavaScript implementation of a hero class system with different character types and attack methods.

## Overview

This project implements a `heroi` (hero) class that creates characters with different types and corresponding attack abilities.

## Class Structure

### `heroi` Class

**Constructor Parameters:**
- `nome` (string): Hero's name
- `idade` (number): Hero's age  
- `tipo` (string): Hero's type/class

**Methods:**
- `atacar()`: Executes an attack based on the hero's type

## Hero Types and Attacks

| Type | Attack Method |
|------|---------------|
| mago | magia |
| guerreiro | espada |
| monge | artes marciais |
| ninja | shuriken |

## Usage Example

```javascript
// Create a warrior hero
const calebe = new heroi("Calebe", 9, "guerreiro");
calebe.atacar(); // Output: O guerreiro Calebe atacou usando espada

// Create a monk hero
const maxwell = new heroi("Maxwell", 46, "monge");
maxwell.atacar(); // Output: O monge Maxwell atacou usando artes marciais
```

## Running the Code

```bash
node index.js
```

## Output

The program creates two heroes and demonstrates their attack methods:
- Calebe (warrior) attacks with sword
- Maxwell (monk) attacks with martial arts