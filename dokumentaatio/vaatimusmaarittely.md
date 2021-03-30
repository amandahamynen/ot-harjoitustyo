## Sovelluksen tarkoitus
Quizzy-sovelluksella rekisteröityneet käyttäjät voivat kirjautua sisään sovellukseen ja pelata tietovisapeliä.

### Käyttäjät
Uudet käyttäjät tulee aluksi rekisteröidä sovellukseen, jonka jälkeen sovellukseen voidaan kirjautua käyttämällä rekisteröimisessä luotua käyttäjätunnusta ja salasanaa. Sovelluksessa on vain yhden tyyppisiä käyttäjiä, ja he voivat pelata tietovisaa kirjauduttuaan sisään.

### Perusversion tarjoama toiminnallisuus
- Käyttäjä voi luoda uuden käyttäjän järjestelmään
  - Kahdella käyttäjällä ei voi olla samaa käyttäjätunnusta
  - Salasana ja käyttäjätunnus eivät voi olla tyhjiä syötteitä
- Käyttäjä voi kirjautua sovellukseen jo rekisteröityneellä käyttäjätunnuksella ja salasanalla
- Kirjautuminen johtaa sovelluksen kotinäytölle, jossa käyttäjä voi:
  - Kirjautua ulos sovelluksesta
  - Alkaa pelaamaan tietovisaa
- Tietovisassa on kysymyksiä ja jokaiseen neljä vastausvaihdoehtoa, joista käyttäjä voi valita yhden. Lukittuaan vastauksen käyttäjä näkee oliko vastaus oikein (jos ei, oikea vastaus ilmestyy näytölle) ja siihen asti kertyneet pisteet tietovisasta.
  - Tietovisan päätettyä käyttäjä näkee montako pistettä hän sai yhteensä ja voi palata takaisin kotinäytölle

### Jatkokehitysideoita
- Aluksi kysymykset ovat ennalta määrättyjä, joista sovellus valitsee 10 satunnaista kysymystä. Sovelluksen kehittyessä käyttäjä voi valita kuinka monta kysymystä haluaa tietovisaan.
- Käyttäjä näkee parhaimman tuloksensa kotinäytöltä
- Käyttäjä voi lisätä omia kysymyksiä sovellukseen
