<h1>
    2048
</h1>
I developed an engaging <b>2048 game</b> in python, using <b>kivy</b> to implement a user-friendly graphical interface that enhances
player experience.
I created algorithms to manage game mechanics, including tile merging and scoring, ensuring a responsive and challenging gameplay experience and
integrated features such as undo and resume
functionalities and game-over conditions.
<br> </br>
<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img.png">
</p>
<h3>
    Game rules
</h3>
2048 is played on a 4×4 grid featuring numbered tiles that move smoothly when directed by the four arrow keys. Each time the tiles are shifted, a new tile appears randomly in one of the empty spaces
on the board. Tiles move as far as they can in the chosen direction, stopping only when they collide with another tile or reach the edge of the grid. If two tiles with the same number collide during
the move, they merge into a single tile with a value equal to the sum of the two. This merged tile cannot combine with any other tile in the same move. I have implemented <b>specific features</b> in
the game, such as a <b>resume</b> function that allows the player to continue from where they left off, and an <b>automatic</b> move system that activates after a period of inactivity, selecting the
best possible move. The game is won when a tile with the value of 2048 is created. You lose when no more valid moves are possible, meaning no tiles can be combined or moved.
