## Käyttöohje

Lataa projektin viimeisin release. lisää linkki.


### Pelin asennus


Ennen kuin käynnistät pelin ensimmäistä kertaa, asenna riippuvuudet komennolla:

```bash
poetry install
```
Ja suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

### Pelin käynnistäminen


Asennuksen ja alustustoimenpiteiden jälkeen voit käynnistää pelin komennolla:

```bash
poetry run invoke start
```

### Peliohjeet


Peli aukeaa päävalikkoon:

![päävalikko](.kuvat/paavalikko.png)

Aloita uusi peli painalla enter tai katso pelistä saatuja parhaita tuloksia painamalla välilyöntiä. Pääset tulostaulukosta takaisin päävalikkoon painamalla välilyöntiä.

### Pelaaminen


Uusi peli käynnistyy automaattisesti. Liikutettava palikka generoituu/ilmestyy ruudun keskiosaan ja putoaa alas kunnes törmää pelialustan pohjaan tai toiseen palikkaan.

![pelinäkymä](.kuvat/pelinakyma.png)

Voit liikuttaa ja kääntää palikkaa seuraavasti:

| Näppäin | Tapahtuma |
|---------|-----------|
| vasen-nuoli | siirrä palikkaa vasemmalle |
| oikea-nuoli | siirrä palikkaa oikealle |
| ylös-nuoli | kierrä palikkaa myötäpäivään |
| alas-nuoli | siirtää palikkaa alas |

Pelinäkymän oikeassa laidassa näkyy pistetilanne ja poistettujen rivien määrä.

### Pelin päättyminen


Peli päättyy kun uusi palikka ei enää mahdu peliruutuun. Pelinäkymään ilmestyy Game over -ilmoitus. Pelin päätyttyä pääset takaisin päävalikkoon välilyönnillä.

### Pelin sulkeminen


Voit sulkea pelin painamalla escapea tai oikeasta yläkulmasta missä tahansa näkymässä.
