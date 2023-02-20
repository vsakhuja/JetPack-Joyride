# 2018114007
##  OBJECTIVE 
The game must simulate a basic version of jetpack joyride. We need to defend the boss before the time specifies.The objective of the game is to collect as many coins as possible, fight the obstacles on the way, defeat the boss enemy.

RUNNING THE GAME
```
python3 is required 
python3 main.py
```
## FEATURES
- The game is implemented in Python3.6
- The code is modular and follows PEP8 standards
- Uses only core Python3 packages
- Player can move right, left, fly, shoot, use shield
- Enemies are placed in between.
- You can shoot the fire beam, enemy 
- Colors are implemented using the colorama package of python

## MOVEMENT
- a - Move Backwards
- d - Move forward
- w - Fly
- space - implement shield
- b - generate bullets 
- n - for nitros(speeding of the frame of game as well as the player)

## OOP
- #### Inheritance
    - Player and Enemy class inherit from the Person class . Also the slant class inherits all the properties of the Obstacles class.
- #### Polymorphism
   - In the Obstacles class the cleaner function is modified in its child slant.
- #### Encapsulation
    - Class and object based approach for all the functionality implemented
- #### Abstraction
    - Properties of the every class are hidden from the user using abstraction and used by getter-setter method

## OBSTACLES
- three types of beam, enemy, coin, magnet, power booster, and boss enemy

## BACKGROUND AND SCENERY
- • The scenery and the obstacles must change as you move in and out of the window. There is a ground/platform and the sky, and the Mandalorian can’t go below the ground or above the sky.

## SCORE
- The final score is calculated as:
```
It is represented by coins in the top left corner

```
