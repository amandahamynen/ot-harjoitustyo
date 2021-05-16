# Käyttöohje

Lataa projektin viimeisin versio (Loppupalautus).

## Konfigurointi

Tallennuksessa käytyttyjen tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa .env-tiedostossa. Tiedostot luodaan automaattisesti data-kansioon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```bash
DATABASE_FILENAME=database.sqlite
QUESTIONS_FILENAME=questions.csv
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna projektin riippuvuudet komennolla:

```bash
poetry install
```

Tämän jälkeen suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
 ```

Nyt ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Kirjautuminen

Quizzy-sovellukseen käynnistäminen avaa kirjautumisnäkymän:

<img width="1199" alt="Login" src="https://user-images.githubusercontent.com/55439398/117054684-0ab49700-ad23-11eb-923a-d7c3bec5d436.png">

Kirjautmisnäkymässä käyttäjä voi syöttää käyttäjätunnuksen ja salasanan, jolloin sovellukseen kirjautuminen onnistuu painamalla Login-painiketta. Jos käyttäjä haluaa luoda uuden käyttäjän sovellukseen, tulee klikata painiketta Create a new User.

## Uuden käyttäjän luominen

Uuden käyttäjän luomisnäkymään pääsee kirjautumisnäkymästä klikkaamalla painiketta Create a new User. Uusi käyttäjä luodaan syöttämällä etunimi, sukunimi, käyttäjätunnus ja salasana.

<img width="1199" alt="Create" src="https://user-images.githubusercontent.com/55439398/117054860-3899db80-ad23-11eb-8929-1e2073bb1b17.png">

Jos uuden käyttäjän luonti onnistui, siirrytään kotinäyttöön painikkeesta Create.
Takaisin kirjautumisnäkymään onnistuu klikkaamalla painiketta Back.

## Kotinäyttö ja pelin aloittaminen

Kotinäytöltä käyttäjä pystyy kirjautumaan sovelluksesta ulos näytön oikealta yläkulmasta.
Ennen pelin alkua käyttäjä voi valita kysymysten aihealueen ja kuinka monta kysymystä haluaa.
Peli alkaa painikkeesta "Start the quiz"

<img width="1199" alt="Homescreen" src="https://user-images.githubusercontent.com/55439398/117055090-6ed75b00-ad23-11eb-8855-921dd1e7a6dc.png">

## Peli

Pelinäykymässä pelaajalla on neljä eri vastausvaihtoehtoa, joista voidaan valita yksi ja klikata "Submit" painiketta. 
Painettuaan "Submit" näppäintä pelaaja näkee oliko vastaus oikein ja jos ei ollut, oikea vastaus tulee näkyviin. 
Pelaajan voi tämän jälkeen siirtyä seuraavaan kysymykseen.

<img width="1199" alt="Quiz" src="https://user-images.githubusercontent.com/55439398/117055357-be1d8b80-ad23-11eb-8c74-51520e122353.png">

Vastattuaan kaikkiin kysymyksiin pelaaja näkee saamansa pistemäärän ja voi siirtyä takaisin kotinäytölle.
