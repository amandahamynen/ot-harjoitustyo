## Sovelluksen tarkoitus
Quizzy-sovelluksella rekisteröityneet käyttäjät voivat kirjautua sisään sovellukseen ja pelata tietovisapeliä.

### Käyttäjät
Uudet käyttäjät tulee aluksi rekisteröidä sovellukseen, jonka jälkeen sovellukseen voidaan kirjautua käyttämällä rekisteröimisessä luotua käyttäjätunnusta ja salasanaa. Sovelluksessa on vain yhden tyyppisiä käyttäjiä, ja he voivat pelata tietovisaa kirjauduttuaan sisään.

### Perusversion tarjoama toiminnallisuus
- [x] Käyttäjä voi luoda uuden käyttäjän järjestelmään
  - [x] Kahdella käyttäjällä ei voi olla samaa käyttäjätunnusta
  - [x] Salasana ja käyttäjätunnus eivät voi olla tyhjiä syötteitä
- [x] Käyttäjä voi kirjautua sovellukseen jo rekisteröityneellä käyttäjätunnuksella ja salasanalla
- [x] Kirjautuminen johtaa sovelluksen kotinäytölle, jossa käyttäjä voi:
  - [x] Kirjautua ulos sovelluksesta
  - [x] Alkaa pelaamaan tietovisaa
- [x] Tietovisassa on kysymyksiä ja jokaiseen neljä vastausvaihdoehtoa, joista käyttäjä voi valita yhden. Lukittuaan vastauksen käyttäjä näkee oliko vastaus oikein (jos ei, oikea vastaus ilmestyy näytölle).
  - [x] Tietovisan päätettyä käyttäjä näkee montako pistettä hän sai yhteensä ja voi palata takaisin kotinäytölle

### Jatkokehitysideoita
- Aluksi kysymykset ovat ennalta määrättyjä, joista sovellus valitsee 10 satunnaista kysymystä. Sovelluksen kehittyessä käyttäjä voi valita kuinka monta kysymystä haluaa tietovisaan.
- Kysymyksissä on eri kategorioita, joista käyttäjä voi valita kotinäytöllä minkä kategorian kysymyksiä haluaa tietovisaan
- Käyttäjä näkee parhaimman tuloksensa kotinäytöltä
- Käyttäjä voi lisätä omia kysymyksiä sovellukseen
- Tietovisasta voi valita perusversion tai version, jossa jokaiseen kysymykseen on vastattava tietyn aikarajan kuluessa
