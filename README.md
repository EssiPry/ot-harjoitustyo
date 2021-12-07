## Tetris

Sovellus on tetris-klooni eli hauska tietokonepeli, jossa pelaaja yrittää pudottaa eri muotoisia palikoita niin, että ne täyttävät pelialueen vaakasuunnassa ja katoavat. Peli päättyy, kun palikka koskee pelialueen kattoon.

### Dokumentaatio

* [Arkkitehtuurikuvaus](https://github.com/EssiPry/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [Vaatimusmäärittely](https://github.com/EssiPry/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/EssiPry/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)


### Käyttöohje

Asenna riippuvuudet komennolla:
```bash
poetry install
```

Sovelluksen saa käyntiin kommennolla:

```bash
poetry run invoke start
```
### Ohjelman testaus

```bash
poetry run invoke test
```

### Testikattavuusraportin generointi

```bash
poetry run invoke coverage-report
```

### Pylint

```bash
poetry run invoke lint
```
