# Ohjelmistotekniikka, kevät 2021

# Quizzy

Quizzy-sovelluksella rekisteröityneet käyttäjät voivat kirjautua sisään sovellukseen ja pelata tietovisapeliä.

- [Release 1](https://github.com/amandahamynen/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/amandahamynen/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/amandahamynen/ot-harjoitustyo/releases/tag/loppupalautus)

## Huomio Python-versiosta
Sovelluksen toiminta on testattu Python-versiolla 3.6.0. Vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Käyttöohje](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Testaus](https://github.com/amandahamynen/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
 ```
 
3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu htmlcov-hakemistoon.

### Pylint

Pylintin tarkastelun saa suorittamalla komennon:

```bash
poetry run invoke lint
```

## Credits

[Ohjelman taustalla käytetty kuva](https://pixabay.com/illustrations/boat-rowing-lake-water-travel-5889919/)
