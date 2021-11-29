# Pääkaupunkipeli

Pelin avulla voi harjoitella maailman maiden pääkaupunkeja.

## Dokumentaatio

* [Vaatimusmäärittely](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/kirjanpito.md)
* [Arkkitehtuuri](https://github.com/kerkkanen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Aseta riippuvuudet komennolla:

```
poetry install
```

2. Suorita vaadittavat aloitustoimenpiteet komennolla:

```
poetry run invoke build
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```
Tällä hetkellä sovelluksessa on käytössä tekstikäyttöliittymä, jonka avulla pelin perustoiminnallisuutta voi testata.

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



