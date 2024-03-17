# Toy Robot Challenge in Python

Toy Robot Challenge implementation in Python. Simulates a Toy Robot traversing across a table with dimension of 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.


## Rules and Constraints

- The tabletop is a square with dimensions 5 units x 5 units.
- The origin (0,0) can be considered to the SOUTH WEST most corner.
- It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command.
- The toy robot must not fall off the table during movement.
- The initial placement of the robot should be inside the table.
- A robot that is not on the table can choose to ignore MOVE, LEFT, RIGHT, and REPOT commands.
- Invalid commands are ignored.

## Commands

The robot accepts the following commands in the command line:

- `PLACE X,Y,F`: Put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST, or WEST.
- `MOVE`: Move the robot one unit forward in the direction it is currently facing.
- `LEFT`: Rotate the robot 90 degrees left without changin position.
- `RIGHT`: Rotate the robot 90 degrees right without changin position.
- `REPORT`: Announce the X,Y,F of the robot.

## Example Input and Output:

```
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
```

```
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
```

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

## Design Decisions
I chose to represent the table, robot, and game, as an object. The game having a table and robot instance, modeling how it would be in real life. The table having dimensions with min and max to be resizeable, but set default to 5 units by 5 units as per specifications. The robot, has its position attribute representing where it is and where it is facing (X,Y,F).

I implemented rotation by having simulated a 'compass' of sorts using a double ended queue as a reference. Taking the idea that North, East, South, and West is a circulart list. Only that in this compass implementation, the compass needle (which is the index) is fixed, while it is the compass face below that is moving by rotating the deque in a specific direction.

For the folder structure, just made a game(src) and inside it the source files, and test, for my tests. Containerized the app with Docker and added a Makefile for easier app and test run. The requirements are not really needed, just mainly for testing.

Tests are done with pytest, tried to cover as much as I could except for the actual CLI, as it runs in a forever while loop and there are limitations with testing that, tried it with timeout, and other python testing libraries but couldn't get it to work. Chose to manually verify the CLI input/output instead, but all other classes are covered. Made the unit tests per class with each scenarios as subtests within the test.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/jonrod1693/toy-robot-challenge.git
```

2. Navigate to the project directory:

```bash
cd toy-robot-challenge
```

3. Install dependencies (only for running tests locally):

```bash
# Sample with pip
pip install -r requirements.txt
```

## Usage

### With Makefile
---
If you have [Docker](https://docs.docker.com/) installed locally you can use the makefile:

1. In the main project directory, run the main app inside a container with make:
```bash
make start
```
2. To exit/stop the script:
```bash
Ctrl+C
```
3. Or in another terminal, in the main project directory:
```bash
make stop
```

### Manual Run
---
Alternatively you may run the script manually with the following

1. In the main project directory, run the following:
```bash
python ./game/main
```
2. To exit/stop the script:
```bash
Ctrl+C
```

## Run Tests

### With Makefile
---
If you have [Docker](https://docs.docker.com/) installed locally you can use the makefile:

1. In the main project directory, run the pytest inside the container with make:
```bash
make test
```

### Manual Run
---
Alternatively you may run the script manually with the following

1. In the main project directory, create a virtual environment:
```bash
python -m venv .venv
```
2. Activate the virtual environment you created:
```bash
source .venv/bin/activate
```
3. Install the requirements needed for testing:
```bash
pip install -r requirements.txt
```
4. Now you can run the tests manually inside the .venv with:
```bash
pytest
```
