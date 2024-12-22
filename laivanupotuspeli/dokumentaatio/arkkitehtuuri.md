# Arkkitehtuuri

## Sovelluslogiikka

```mermaid
 classDiagram

    Board "1" --|> "*" Ship
    Board "1" --|> "*" Guess
    GameController "1" --|> "2" Player
    GameController "1" --|> "2" Board
    Ship "1" --|> "1" ShipType

    class Guess{
        bool hitShip
    }
    class Player{
        
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
        Board player1_board
        Board player2_board
    }
    class ShipType{
        List<tuple> shipTilesCoordinates
    }
```


`GameController`-luokka sisältää pelaaja oliot sekää huolehtii pelin vuoroista ja niiden käsittelystä.


`Player`-luokka sisältää pelilaudan, johon pelaaja on asettanut omat aluksensa. Pelaaja voi joko saada joko käyttäjältä tai tekoälyltä komentoja.


`Board`-luokka sisältää aluksia sekä vastustajan tekemät arvaukset ja osumat. Se myös huolehtii pelilautaan liittyvistä ominaisuuksista,
kuten mihin tietynlaisen aluksen voi asettaa.


`Ship`-luokka sisältää tietoa aluksesta, kuten minkä tyyppinen se on tai onko se upotettu.


`Guess`-luokka sisältää tietoa yhdestä pelaajan arvauksesta, kuten osuiko se alukseen vai ei.


`ShipType`-luokka sisältää tietoa yhdestä alustyypistä, kuten minkä muotoinen alus on.
