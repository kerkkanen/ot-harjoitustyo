# Arkkitehtuurikuvaus

## Rakenne

Ohjelma rakentuu kolmelle kerrokselle: käyttöliittymä, logiikkapalvelut ja repositoriot.

![Pakkauskaavio](pakkauskaavio.png)

Kansio ui sisältää käyttöliittymästä, services logiikasta ja repositories tietojen tallennuksesta vastaavan koodin. Entities sisältää sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kuusi erillistä näkymää:
* Aloitus
* Valmiina pelin aloitukseen
* Kolmen vaikeustason pelinäkymät
* Parhaat pisteet

Kaikki näkymät on toteutettu omina luokkina. Ui-luokka huolehtii yksi kerrallaan näkyvissä olevien näkymien vaihdosta. Käyttöliittymä on eroteltu sovelluslogiikasta, jota hoitaa luokka GameService.

## Sovelluslogiikka

Sovelluksen tietomallin muodostavat luokat Question ja Player, jotka kuvaavat pelin kysymyksiä ja pelaajaa. Pelin kysymykset luodaan kysymys-olioiksi ja pelin pelaajalle talletetaan nimimerkki ja pisteet.

GameService vastaa kaikesta peliin ja pisteisiin liittyvästä logiikasta. Luokka tarjoaa käyttöliittymän kaikki peliin liittyvät metodit, esimerkiksi:
* create_question()
* check_capital()
* save_score()
* get_highscores()
GameServicella on yhteys luokkiin QuestionRepository ja PlayerRepository, joiden kautta haetaan tiedot kysymyksiin ja hoidetaan pistetilaston haku ja talletus. Luokkien toteutus injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

## Tietojen tallennus

PlayerRepository-luokka huolehtii pisteiden talletuksesta CSV-tiedostoon. Molemmat repository-luokat myös lukevat tietoa CSV-tiedostoista.


## Päätoiminnallisuudet

Päänäkmyässä pelaaja voi syöttää oman nimimerkin ja valita pelin vaikeustason (2, 3 tai 6 vastausvaihtoehtoa). Jos tiedot jättää tyhjiksi, nimeksi tulee Pelaaja 1 ja vaikeustasoksi 3. Seuraavassa näkymäsäs vahvistetaan valinnat painamalla "Aloita peli" tai palaamalla aloitusnäkmyään. Peli alkaa ja kestää 10 kierrosta ellei pelaaja keskeytä peliä aiemmin. Pelinäkymässä kutsutaan GameServiceä, jonka kautta luodaan uusi kysymys ja napin painalluksesta tarkistetaan vastaus.

![Sekvenssikaavio](sekvenssikaavio.png)

Palaute vastauksesta (oikein/väärin) tulee vastausvaihtoehdon klikkauksen jälkeen tekstilaatikossa näkyviin. Laatikos on nappivahtoehdot yes ja no, joita klikkaamalla peli joko jatkuu tai päättyy. Pelin lopuksi pelaajan pisteet tulevat näkyviin infotekstilaatikkoon. OK klikattuaan näykviin tulee parhaat pisteet -tilasto ja pelaaja voi palata alkunäkymään klikkaamalla "Pelaa uudelleen".
