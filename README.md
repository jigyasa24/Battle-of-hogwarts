Problem Statement:
You are a board game designer and programmer who knows problem-solving
strategies, and you have been assigned the task of creating a board game that will
help students review coding content in a fun and interesting way!

About the game:
This is a Harry Potter trivia game, in which you help harry destroy the horcruxes and
finally Voldemort by giving the correct answers.

Rules of the game:
• A total of 18 questions available to finish the game.
• One horcrux will get destroyed with every 2 correct answers
• After the first 14 questions which will help in destroying all the horcruxes there
will be 4 questions left to finally kill Voldemort.
• Even one wrong answer will kill harry (you) and the game will be over.

Summary:
We were instructed to ideate an original board game with proper logics and
functioning. We had help from the instructor throughout the project which helped a
lot through the process. To make the game I used the usual approach of first
decomposing the problem and then going ahead solving them, which made the
problem much more approachable. After decomposing the problem I researched
about the packages that I can use and went ahead writing the code.

Decomposition:
• Complete the ideation and conceptualising of your game.
• Create a rough plan for your game by analysing the concept.
• Define how your game is going to work.
• Define the rules of the game.
• Create a prototype of your idea.
• Developing a logic of your game
• Doing proper research about the technical requirements of your game.
• Properly arrange your code so that it works.

Pattern recognition:
After properly studying all the decomposed problems and the logic of the game I
realized that the logics in my game are really repetitive, like every 2 correct answers
destroy a horcrux and answering even one question wrong can result in Harry’s
death and game will be over. This logic has been repeated in every question.

Algorithm:
• I used the tkinter package in python for GUI
• Made a canvas for the main window(home screen of the game) and defined
its dimensions and background colour.
• Added background image and buttons to the main window.
• Defined functions to display information about the game and the rules and
added their repective commands to the buttons.
• Created a new window for starting the game by defining another function and
linking it with the start game button using command.
• Defined the function “game over” if the user selects any wrong answers.
• Defined a new window for displaying the next question if user selects the right
answer.

Abstraction:
We don’t need to concentrate on the broad concept of the game as it can make you
confused. We just need to follow the decomposition of the game that we have done,
i.e focus on smaller sub problems and solving them in sequence as they are based
on the main logic of the game which has been derived from the concept of the game.

Code design:
The code has been designed in a very basic manner and is easy to understand,
every process is clearly explained and performed, every part of the code is inter
connected to each other. And the user defined functions have been named such that
their function can be understood just by looking at the name.

Logics:
• If the answer is correct, new window will be opened with the next question.
• Else the game will be over
• All the buttons serve the function respective to their names by linking them
with user defined functions by command function call.
• Start game button calls the function of the main window of the game with the
first question.
• Score is shown after the 1st horcrux is destroyed.
