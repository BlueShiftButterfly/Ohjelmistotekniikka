# Laivanupotuspeli

## Python-versio

Sovellus on luotu Python-versiolla `3.10`. Sovelluksen toimivuudesta ei ole takuuta vanhemilla Python-versiolla.

## Dokumentaatio

 - [Alustava määrittelydokumentti](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/vaatimusmaarittely.md)
 - [Changelog](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/changelog.md)
 - [Tuntikirjanpito](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/tuntikirjanpito.md) 
 - [Arkkitehtuuri](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/arkkitehtuuri.md) 
 - [Testausdokumentti](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/testausdokumentti.md) 
 - [Käyttöohje](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/kayttoohje.md) 

## Komentorivitoiminnot

__Kaikki alla listatut komennot on suoritettava `/laivanupotuspeli/` alihakemistosta!__

### Asennus

Riippuvuudet voi asentaa komennolla:

```
poetry install
```

### Ohjelman suorittaminen

Sovelluksen voi käynnistää komennolla:

```
poetry run invoke start
```

### Testaus

Sovelluksen testit voi suorittaa komennolla:

```
poetry run invoke test
```

Sovelluksen kattavuusraportin voi luoda komennolla:

```
poetry run invoke coverage
```

Sovelluksen linttauksen voi suorittaa komennolla:

```
poetry run invoke lint
```