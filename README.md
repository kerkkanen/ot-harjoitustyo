# Pääkaupunkipeli

Pääkaupunkipeli, jossa pelaajan on yhdistettävä oikea pääkaupunki kysyttyyn maahan. Pelissä on kolme vaikeustasoa ja kaksi erilaista pelimahdollisuutta. Pelialueeksi on mahdollista valita yksittäinen manner tai kaikki maailman maat.

## Releaset

* [Loppupalautus]()
* [Toinen release](https://github.com/kerkkanen/ot-harjoitustyo/releases/tag/viikko6)
* [Ensimmäinen release](https://github.com/kerkkanen/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuuri](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
* [Tuntikirjanpito](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kirjanpito.md)

## Asennus

Aseta riippuvuudet sovellus-kansiossa komennolla:

```
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```

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

