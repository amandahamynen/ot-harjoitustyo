# Arkkitehtuurikuvaus

## Käyttöliittymä

Sovelluksen käyttöliittymässä on neljä erillista näkymää:
-	Kirjautumisnäkymä, jossa käyttäjä voi kirjautua sovellukseen jo olemassa olevalla käyttäjätunnuksella ja salasanalla
-	Rekisteröitymisnäkymä, jossa käyttäjä voi luoda uuden käyttäjän 
-	Kotinäyttö, jossa käyttäjä voi tehdä valinnat peliin liittyvistä asetuksista ja alkaa pelaamaan peliä
-	Pelinäkymä, jossa itse peli tapahtuu

Jokainen näkymistä on toteutettu omina luokkinaan, jotta niiden päivittäminen tulevaisuudessa olisi luontevaa. Jokainen näkymä on esillä kerrallaan, ja joiden näkymisestä ja vaihtumisesta huolehtii UI-luokka. Sovelluslogiikasta huolehtii QuizzyService, ja käyttöliittymä on pyritty pitämään erillään sovelluslogiikasta.

## Sovelluslogiikka

Quizzy-sovelluksen loogisen tietomallin muodostavat luokat User ja Question, jotka kuvaavat käyttäjiä ja pelin kysymyksiä

Sovelluksen toiminnallisuuksista vastaa luokan QuizzyService ainoa olio, joka tarjoaa kaikille käyttöliittymän toiminnoille oman metodin. 

QuizzyService pääsee käsiksi käyttäjiin ja kysymyksiin tietojen tallennuksesta vastaavan pakkauksessa repositories sijaitsevien UserRepository ja QuestionRepository kautta. 

QuizzyService-luokan ja sovelluksen muiden osien luokka/pakkauskaavio:

![Luokkakaavio](https://user-images.githubusercontent.com/55439398/117054060-6599be80-ad22-11eb-8c83-6fdb888d7681.jpg)


## Tietojen pysyväistallennus

Sovelluksen pakkauksen repositories luokat UserRepository ja QuestionRepository huolehtivat käyttäjien ja kysymysten tallentamisesta ja lukemisesta. UserRepository-luokka tallentaa tietoa käyttäjistä SQLite-tietokantaan. QuestionRepository puolestaan lukee tietoa kysymyksistä pakkauksen data CSV-tiedostosta.

### Tiedostot

Sovellus lukee ja tallentaa tietoa käyttäjistä ja kysymyksistä eri tiedostoista, joiden nimet ovat määritelty sovelluksen juuressa olevasta .env konfiguraatiotiedostosta.

Tiedot käyttäjistä tallennetaan SQLite-tietokantaan, joka alustetaan initialize_database.py-tiedostossa.

Kysymykset ovat tallennettu CSV-tiedostoon seuraavassa muodossa:

```bash
What is the capital city of Albania,Sofia,Tirana,Lisbon,Riga,Tirana
What is the capital city of Austria,Vienna,Monaco,Warsaw,Madrid,Vienna
```
Kysymys,vastausvaihtoehto[0],vastausvaihtoehto[1],vastausvaihtoehto[2],vastausvaihtoehto[3],vastaus. Kenttien arvot erotellaan toisistaan pilkulla.

## Päätoiminnallisuudet

### Kirjautuminen

Käyttäjän syötettyään käyttäjätunnus ja salasana kirjautumisnäkymässä ja klikattuaan Login-painiketta, sovelluksen kontrolli etenee seuraavanlaisesti: 

![20210425_145816000_iOS](https://user-images.githubusercontent.com/55439398/117053992-4bf87700-ad22-11eb-9066-e61491938f0b.jpg)


Painikkeen klikkaukseen reagoiva tapahtumankäsittelijä kutsuu QuizzyServicen metodia login parametrein käyttäjän syöttämää käyttäjätunnusta ja salasanaa. Sovelluslogiikka selvittää UserRepositoryn avulla onko käyttäjätunnus olemassa ja jos on, tarkistetaan vastaako sen salasana käyttäjän syöttämää salasanaa. Kirjautuminen onnistuu, jos käyttäjätunnus on olemassa ja salasana on oikein. Seurauksena tästä näkymäksi vaihtuu HomeScreen ja käyttäjä kirjataan sisälle.

### Uuden käyttäjän luominen

Käyttäjän tulee syöttää valitsemansa etunimi, sukunimi, käyttäjätunnus ja salasana. Uuden käyttäjän luonti onnistuu, jos kyseinen käyttäjätunnus ei ole jo käytössä ja salasana ei ole tyhjä merkkijono. Käyttäjän klikattuaan Create a new user-painiketta sovelluksen kontrolli etenee seuraavanlaisesti:

![20210425_145835000_iOS](https://user-images.githubusercontent.com/55439398/117054047-5f0b4700-ad22-11eb-8ad1-30e5eb9f6fa7.jpg)


Tapahtumakäsittelijä kutsuu metodia create_user parametrinä tiedot käyttäjästä. Sovelluslogiikka selvittää metodin find_by_username avulla, onko käyttäjätunnusta jo olemassa. Jos käyttäjätunnusta ei ole jo olemassa, sovelluslogiikka luo uuden User-olion ja tallentaa sen UserRepositoryn metodin create-avulla. Seurauksena näkymäksi vaihtuu HomeScreen ja luotu käyttäjä kirjataan sisälle.
