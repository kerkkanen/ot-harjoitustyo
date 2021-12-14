# Pääkaupunkipeli

Pääkaupunkitietovisa, jossa voi harjoitella eri mantereiden tai koko maailman maiden pääkaupunkeja kahden pelimoodin avulla.

## Releaset

* [Ensimmäinen release](https://github.com/kerkkanen/ot-harjoitustyo/releases/tag/viikko5)
* [Toinen release](https://github.com/kerkkanen/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuuri](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
* [Tuntikirjanpito](https.://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kirjanpito.md)

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

