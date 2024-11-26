# Arkkitehtuuri

## Sovelluslogiikka

```mermaid
 classDiagram

    Player "1" --|> "1" Board
    Board "1" --|> "*" Ship
    Board "1" --|> "*" Guess
    GameController "1" --|> "2" Player

    class Guess{
        bool hitShip
        tuple guessCoordinates
    }
    class Player{
        Board board
        +processTurn(List<Guess> playerGuesses) Guess
    }
    class Ship{
        ShipType shipType
        bool isSunk
        int tilesLeft
        List<tuple> shipTilesCoordinates
    }
    class Board{
        List<Ship> ships
        List<Guess> opponentGuesses
    }
    class GameController {
        Player player1        
        Player player2

        +processPlayerTurn(Player player)
        +checkWinCondition(Player player) bool
    }
```
