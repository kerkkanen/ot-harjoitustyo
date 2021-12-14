# Pääkaupunkipeli

Pelin avulla voi harjoitella maailman maiden pääkaupunkeja.

## Release

* [Toinen release](https://github.com/kerkkanen/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kirjanpito.md)
* [Arkkitehtuuri](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Aseta riippuvuudet sovellus-kansiossa komennolla:

```
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```
Sovelluksessa on graafinen käyttöliittymä, joka tällä hetkellä ei tosin sulkeudu aina täysin oikein...

### Testaus

Testit suoritetaan komennolla:

```
poetry run invoke test
```
### Testikattavuus

Testikattavuuden voi generoida komennolla:

```
poetry run invoke coverage-report
```
Raportti generoituu htmlcov-hakemistoon

### Pylint

Pylintin saa ajettua komennolla:

```
poetry run invoke lint
```

