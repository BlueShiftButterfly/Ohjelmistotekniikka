# Laivanupotuspeli

## Python-versio

Sovellus on luotu Python-versiolla `3.12`. Sovelluksen toimivuudesta ei ole takuuta vanhemilla Python-versiolla.

## Dokumentaatio

 - [Alustava määrittelydokumentti](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/vaatimusmaarittely.md)
 - [Changelog](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/changelog.md)
 - [Tuntikirjanpito](https://github.com/BlueShiftButterfly/Ohjelmistotekniikka/blob/main/laivanupotuspeli/dokumentaatio/tuntikirjanpito.md) 

## Komentorivitoiminnot

Kaikki alla listatut komennot on suoritettava `/laivanupotuspeli/` alihakemistosta!

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