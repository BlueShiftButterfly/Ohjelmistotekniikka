## Monopoli, luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu
    Ruutu "1" -- "*" Toiminto
    Katu "1" -- "1" Pelaaja
    Katu "1" -- "1" Kadunnimi
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
    Sattuma "*" -- "*" Sattumakortti
    Yhteismaa "*" -- "*" Yhteismaakortti
    Pelinappula "1" -- "*" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "*" Rahaa
```
