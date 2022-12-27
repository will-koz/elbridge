# Elbridge

Elbridge is a TUI Gerrymandering game.

## Installation

### Linux / Unix / MacOS (I think)

`git clone` this repo. Upstream / main / master is `git clone https://github.com/will-koz/elbridge`

There are no additional requirements for installation (requirements.txt is just for Microsoft
Windows).

### Microsoft Windows

`git clone` this repo. Upstream / main / master is `git clone https://github.com/will-koz/elbridge`

Once you have downloaded the code, run `py -m pip install -r requirements.txt` to install windows
curses.

## Running

On *nix run `./main.py`, and on Microsoft Windows run `py main.py` or `python3 main.py` in the
directory you cloned to.

## TODO
- [x] Make a "You Lost" screen and a "Good Game" screen at the end of a game
  - [x] Make a scoring system
- [x] Make a menu for setting game information and opening more information in web browser about
gerrymandering
- [x] Add a new visual cue for selected blocks
- [x] Add a button for finishing a game (f button)
  - [x] Specify quit and finish buttons in configuration file
- [ ] Test on some other platforms
  - [x] Add Installation > Microsoft Windows
  - [x] Make this public
  - [ ] Finish making this a proper repo
    - [ ] Make a good README
- [x] Do the remaining TODOs
- [ ] Install Script?
