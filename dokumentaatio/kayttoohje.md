# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla *Assets*-osion alta *Source code*.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelin aloittaminen

Sovellus käynnistää aloitusnäkymään:

Peli on mahdollista aloittaa oletusarvoilla (nimimerkki Pelaaja 1 ja vaikeustaso 3), mutta pelaaja voi valita oman nimimerkin ja vaikeustason. Vaikeustasojen erona on vastausvaihtoehtojen määrä sekä pisteytys: tason kasvaessa pisteitä voi saada enemmän.

## Pelivalintojen vahvistaminen

Aloitusnäkymästä siirrytään pelivalintojen vahvistamiseen. Peli näyttää valitut peliasetukset ja nimimerkin:

Pelin voi aloittaa painamalla "Aloita peli" tai palaamalla edelliseen näkymään.

## Pelin pelaaminen

Pelin alkaessa näkyviin tulee valitun tason mukainen pelinäkymä:

Peliä pelataan kymmenen kierrosta, ellei pelaaja valitse pelin lopettamista aiemmin. Viimeisen kysymyksen vastauksen jälkeen peli päättyy:

 OK-painiketta painamalla sovellus siirtyy pistenäkymään.

## Pistetilasto

Näkyvillä on kolmen parhaan pelaajan pelin tiedot ja pisteet:

Pelin voi pelata uudelleen klikkaamalla "Pelaa uudelleen" -painiketta.
