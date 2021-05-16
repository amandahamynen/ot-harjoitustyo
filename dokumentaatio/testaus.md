# Testausdokumentti

Ohjelmaa on testattu automatisoidun yksikkö- ja integraatiotestein unittestilla.

## Yksikkö -ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa QuizzyService-luokkaa testataan TestQuizzyService-testiluokalla.
Testissä on käytössä luokat FakeQuestionRepository ja FakeUserRepository.

### Repository-luokat

Repository-luokkia QuestionRepository ja UserRepository testataan tiedostoilla, joiden nimet
on konfiguroitu .env.test-tiedostoon. QuestionRepository-luokkaa testataan TestQuestionRepository-testiluokalla
ja UserRepository-luokkaa TestUserRepository-testiluokalla.

### Testikatettavuus

Sovelluksen haarautumakatettavuus on 78%

<img width="959" alt="Testauskatettavuus" src="https://user-images.githubusercontent.com/55439398/118407258-a7aef280-b688-11eb-8619-3e1784a4d0ee.png">

Testaamatta jäi useita kohtia sovelluslogiikasta huolehtivasta QuizzyService-luokasta ajan puutteen vuoksi.
