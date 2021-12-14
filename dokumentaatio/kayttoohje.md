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

Sovellus käynnistää aloitusnäkymään: (KUVA TULOSSA, KUN UI LOPULLISESSA MUODOSSAAN)

Peli on mahdollista aloittaa oletusarvoilla (nimimerkki Pelaaja 1 ja vaikeustaso 3, koko maailma), mutta pelaaja voi valita oman nimimerkin, vaikeustason ja alueen, jolta kysymykset tulevat. Vaikeustasojen erona on vastausvaihtoehtojen määrä sekä pisteytys: tason kasvaessa pisteitä voi saada enemmän.

## Pelivalintojen vahvistaminen

Aloitusnäkymästä siirrytään pelivalintojen vahvistamiseen. Peli näyttää valitut peliasetukset ja nimimerkin: (KUVA TULOSSA MYÖHEMMIN)

Pelissä on valittavana kaksi pelimoodia: äkkikuolema, jossa peli päättyy väärästä vastauksesta, tai kymmenen kierroksen peruspeli. Pelin voi valita painamalla kyseisen moodin aloitusnappia.Vaihtoehtona on myös palata näkymään.

## Pelin pelaaminen

Pelin alkaessa näkyviin tulee valitun tason mukainen pelinäkymä: (KUVA TULOSSA MYÖHEMMIN)

Peruspelissä pelataan kymmenen kierrosta, ellei pelaaja valitse pelin lopettamista aiemmin. Viimeisen kysymyksen vastauksen (tai äkkikuolemassa väärän vastauksen) jälkeen peli päättyy: (KUVA TULOSSA MYÖHEMMIN)

 OK-painiketta painamalla sovellus siirtyy pistenäkymään.

## Pistetilasto

Näkyvillä on kolmen parhaan pelaajan pelin tiedot ja pisteet: (KUVA TULOSSA MYÖHEMMIN)

Pelin voi pelata uudelleen klikkaamalla "PELAA UUDELLEEN" -painiketta.
