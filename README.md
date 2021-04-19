# Ohjelmistotekniikka, kevät 2021

# Quizzy

Quizzy-sovelluksella rekisteröityneet käyttäjät voivat kirjautua sisään sovellukseen ja pelata tietovisapeliä.

## Huomio Python-versiosta
Sovelluksen toiminta on testattu Python-versiolla 3.6.0. Vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

- [Arkkitehtuurikuvaus](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)


## Asennus

1. Asenna riippuvuudet komennolla:

> poetry install

2. Suorita vaadittavat alustustoimenpiteet komennolla:

> poetry run invoke build
 
3. Käynnistä sovellus komennolla:

>poetry run invoke start

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

> poetry run invoke start

### Testaus

Testit suoritetaan komennolla:

> poetry run invoke test

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

> poetry run invoke coverage-report

Raportti generoituu htmlcov-hakemistoon.
