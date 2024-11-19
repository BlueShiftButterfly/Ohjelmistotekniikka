# Laivanupotuspelin vaatimusmäärittelydokumentti


## Sovelluksen tarkoitus

Sovelluksen tarkoitus on mahdollistaa käyttäjän pelata klassista laivanupotuspeliä. Pelin alussa pelaaja voi asettaa aluksensa pelikentälle, jonka jälkeen vuoroittain pelaaja ja vastustaja voivat hyökätä toistensa aluksia vastaan.

## Suunnitellut perustoiminnallisuudet

 - Pelin alussa 
    - Pelaaja voi asetella alukset haluamallaan tavalla
    - Pelissä on ruudukko, johon pelaaja voi asettaa erikokoisia aluksia, kuten 1x4, 3x1 jne.
    - Aluksen on mahduttava valittuun paikkaan, eikä se voi olla toisten alusten päällä
    - Pelaajan on aseteltava kaikki alukset ennen kuin pelin seuraava vaihe voi alkaa
 - Kun pelaajan alukset ovat paikoillaan
    - Pelaaja voi omalla vuorollaan valita neliön mihin hän yrittää osua
    - Valittuaan neliön, pelaaja saa tiedon osuiko hän vastustajan alukseen vai ei
    - Jos pelaaja osui alukseen, hän voi valita uuden neliön, mutta jos hän ei osunut, vastustajan vuoro alkaa
    - Jos pelaaja upottaa aluksen, hän saa siitä tiedon
 - Vastustajan vuorolla
    - Pelissä on yksinkertainen tekoäly, jota vastaan pelaaja voi pelata
    - Tekoäly yrittää omalla vuorollaan upottaa pelaajan alukset
    - Tekoäly erittäin yksinkertaisesti valitsee ruudukon satunnaisesti
 - Pelin loppu
    - Kun pelaaja tai tekoäly voittaa, tulee tieto siitä pelaajalle


## Suunnitellut jatkokehitettävät toiminnallisuudet
 
 - Tekoäly on älykkäämpi ja muistaa mihin se on aikaisemmin osunut, sekä mitä aluksia pelaajalla on jäljellä
 - Pelillä on päävalikko, jossa pelaaja voi muuttaa asetuksia tai lopettaa pelin/sovelluksen suorituksen
 - Pelaaja voi muuttaa pelin asetuksia, kuten pelin resoluutiota, sekä tekoälyn vaikeutta
 - Tekoälyllä on eri vaikeusasteita
 - Pelin loputtua pelaaja voi aloittaa uuden pelin
 - Pelissä voi valita erilaisia ruudukoita jossa pelata, tavallisen neliömäisen ruudukon lisäksi
