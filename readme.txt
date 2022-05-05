Pfeifenreiniger (https://github.com/Pfeifenreiniger), May 2022
__________________________

This is my fourth PyGame based (arcady) game project.

Building up onto the concepts of some of my previous game projects (as 2.5D overlapping sprites, sprite scaling, or multiplayer gameplay),
I've added a self-written computer ai a single player can compete against (file cpu_opponent.py).
The computer ai works with a dynamic priority list, which can be - depending on the cpu difficulty the player has chosen before - ignored by the cpu in favor of a random priority to move next to.
The likelihood of choosing a random value changes with the difficulty level (easy, hard, very hard) as well as the size of the surrounding area the cpu checkes for each priority calculation.

The graphics are made again in a combination of using Adobe Illustrator (drawing) and Photoshop (pixelate).

It took me about one and a half months to complete the project with actuall coding-/design time of about 40 hours in total.

Please consider the docstring of the main.py file for further information about the actual game.