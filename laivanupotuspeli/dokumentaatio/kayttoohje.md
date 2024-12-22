# Käyttöohje

## Ohjelman käynnistäminen

__Kaikki alla listatut komennot on suoritettava `/laivanupotuspeli/` alihakemistosta!__

### Riippuvuuksien Asennus

Ennen käynnistämistä on riippuvuudet asennettava seuraavalla komennolla:

```
poetry install
```

### Käynnistäminen

Sovelluksen käynnistyy komennolla:

```
poetry run invoke start
```

### Pelin pelaaminen


Pelin säännöt ovat melko samanlaisia kuin tavallisessa laivanupotuspelissä. Pelaaja voi lisätä yhden 2x1 kokoisen aluksen, kaksi 3x1 kokoista alusta ja yhden 4x1 kokoisen aluksen.


![](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/kuvat/ohje1.PNG)


Alukset asetetaan painamalla halutun aluksen nappia ja klikkaamalla haluttua ruutua. Aluksen voi poistaa painamalla hiiren oikeaa näppäintä aluksen päällä.
Kun alukset on asetettu, pelaaja voi siirtyä pelin seuraavaan vaiheeseen painamalla `Confirm`-nappia.


![](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/kuvat/ohje2.PNG)


Arvausvaiheessa omalla vuorolla pelaaja voi yrittää ampua yhtä neliötä painamalla hiiren vasenta näppäintä. Jos hän osuu, hän voi arvata uudelleen. Muuten vuoro vaihtuu. Punaiset merkit ovat osumia ja harmaat ohilaukauksia.

Vastustajan vuorolla tekoäly yrittää arvata aluksien paikan. Vastustajan arvaukset näkyvät laudalla.


![](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/kuvat/ohje3.PNG)

Jos pelaajan kaikki alukset on tuhottu, niin vastustaja voittaa. Pelaaja voittaa tuhoamalla kaikki vastustajan alukset.


![](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/kuvat/ohje4.PNG)
