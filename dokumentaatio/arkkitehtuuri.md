# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on rakennettu kolmelle kerrokselle: käyttöliittymä, logiikkapalvelut ja repositoriot.

![Rakenne](Kuvat/packing.png)

Koodi on pakattu hakemistoihin käyttötarkoituksen mukaan: ui sisältää käyttöliittymän, services sovelluslogiikan ja repositories tiedon lataamisen ja tallettamisen käsittävän koodin. Entities sisältää sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kuusi erillistä näkymää:
* Aloitus
* Valmiina pelin aloitukseen
* Kolmen vaikeustason pelinäkymät
* Parhaat pisteet

Kaikki näkymät on toteutettu omina luokkinaan. Ui-luokka huolehtii yksi kerrallaan näkyvissä olevien näkymien vaihdosta. Käyttöliittymä on eroteltu sovelluslogiikasta, jota hoitaa luokka GameService.

## Sovelluslogiikka

Sovelluksen tietomallin muodostavat luokat Question ja Player, jotka kuvaavat pelin kysymyksiä ja pelaajaa. Pelin kysymykset luodaan kysymys-olioiksi ja pelin pelaajalle talletetaan nimimerkki ja pisteet.

GameService vastaa kaikesta peliin ja pisteisiin liittyvästä logiikasta. Luokka tarjoaa käyttöliittymän kaikki peliin liittyvät metodit, esimerkiksi:
* create_question()
* check_capital()
* save_score()
* get_highscores()

GameServicella on yhteys luokkiin QuestionRepository ja PlayerRepository, joiden kautta haetaan tiedot kysymyksiin ja hoidetaan pistetilaston haku ja talletus. Luokkien toteutus injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

![Luokkakaavio][Kuvat/luokkakaavio.png)

## Tietojen tallennus

PlayerRepository-luokka huolehtii pisteiden talletuksesta CSV-tiedostoon. Molemmat repository-luokat myös lukevat tietoa CSV-tiedostoista.


## Päätoiminnallisuudet

Kahdessa aloitusnäkymässä valitaan pelin reunaehdot (ensimmäisessä perustiedot ja toisessa pelitapa). Pelaajan painettua ALOITA-näppäintä siirrytään pelinäkymään.  Pelinäkymässä kutsutaan GameServiceä, jonka kautta luodaan uusi kysymys ja napin painalluksesta tarkistetaan vastaus. Palaute vastauksesta (oikein/väärin) tulee vastausvaihtoehdon klikkauksen jälkeen tekstilaatikossa näkyviin. Peruspelissä laatikon nappivahtoehtoja yes tai no klikkaamalla peli joko jatkuu tai päättyy. Pelin lopuksi pelaajan pisteet tulevat näkyviin infotekstilaatikkoon. OK klikattuaan siirrytään parhaat pisteet -näkymään ja pelaaja voi palata alkunäkymään klikkaamalla "PELAA UUDELLEEN".

Pelin aloittamisen ja yhden kysymyksen pelaamisen sovelluslogiikka:

![Sovelluslogiikka](Kuvat/pelilogiikka.png)

## Ohjelman rakenteeseen jääneet heikkoudet

Graafisen sovellusliittymän pelinäkymissä on melko paljonkin toisteista koodia, jota olisi voinut toteuttaa kaikille kolmelle peliluokalle yhteisenäkin.
