<h1>
    2048
</h1>
I developed an engaging 2048 game in Python, using Kivy to implement a user-friendly graphical interface that enhances the player experience. I designed algorithms to handle the game's mechanics, including tile merging and score calculation, ensuring a responsive and challenging gameplay experience. Additionally, I integrated features such as undo, resume, and game-over conditions to improve playability and user interaction.
<br> </br>
<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img.png">
</p>

<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img_1.png">
</p>

<h3>
    Game rules
</h3>
2048 is played on a 4×4 grid, containing numbered tiles that move smoothly when directed using the arrow keys. Each time the tiles are moved, a new tile randomly appears in one of the empty spaces on the board. The tiles slide as far as possible in the chosen direction, stopping only when they collide with another tile or reach the edge of the grid.

If two tiles with the same value collide during a move, they merge into a single tile with a value equal to the sum of the two. This merged tile cannot combine with another tile in the same move.
<br> </br>
<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img_2.png">
</p>

Jocul este câștigat atunci când se creează o piesă cu valoarea 2048. Pierzi atunci când nu mai sunt posibile mișcări valide, adică atunci când nicio piesă nu poate fi combinată sau mutată.
