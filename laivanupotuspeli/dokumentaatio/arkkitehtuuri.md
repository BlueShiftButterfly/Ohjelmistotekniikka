# Arkkitehtuuri

## Sovelluslogiikka

```mermaid
 classDiagram

    Player "1" --|> "1" Board
    Board "1" --|> "*" Ship
    Board "1" --|> "*" Guess
    GameController "1" --|> "2" Player
    Ship "1" --|> "1" ShipType

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
        int direction
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
    class ShipType{
        List<tuple> shipTilesCoordinates
    }
```
