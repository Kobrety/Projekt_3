# Volební výsledky - Scraper

## Popis projektu

Tento Python skript slouží k extrahování volebních výsledků z webu [www.volby.cz](https://www.volby.cz/pls/ps2017nss/) pro konkrétní obec v České republice. Výsledky jsou následně uloženy do CSV souboru.

## Instalace knihoven

Knihovny, které jsou použity v kódu, jsou uložené v souboru `requirements.txt`. Pro instalaci doporučuji použít virtuální prostředí. Následuj tyto kroky pro instalaci:

1. **Vytvoření virtuálního prostředí:**

   Pokud ještě nemáš virtuální prostředí pro Python, vytvoř ho pomocí následujících příkazů.

   ### Windows:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

   ### macOS / Linux:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. **Instalace požadovaných knihoven:**

   S aktivním virtuálním prostředím nainstaluj všechny potřebné knihovny, které jsou specifikovány v souboru `requirements.txt`. To provedeš pomocí následujícího příkazu:
   
   ```bash
   pip install -r requirements.txt
   ```

## Spuštění projektu

Pro spuštění skriptu je třeba zadat dva povinné argumenty:

```bash
python main.py <odkaz-na-uzemni-celek> <nazev-vysledneho-souboru>
```

### Příklad:

Pokud chceš stáhnout volební výsledky pro obec v Středočeském kraji (Praha-východ), použij tento příkaz:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" vysledky_praha_vychod.csv
```

Tento příkaz stáhne výsledky pro specifikovanou obec a uloží je do souboru `vysledky_praha_vychod.csv`.

## Ukázka použití

### Argumenty:
1. Odkaz na volební výsledky pro Brno: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=5525

2. Název souboru pro výstup: vysledky_brno.csv

### Spuštění programu:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=5525" vysledky_brno.csv
```

### Průběh stahování:
Po spuštění skriptu se stáhnou data a uloží do souboru `vysledky_hodonin.csv`.

```bash
Downloading data from selected URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6205
Saving data to file: vysledky_hodonin.csv
All done, closing...
```

### Částečný výstup v CSV:

Soubor CSV bude obsahovat následující sloupce:

```csv
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,Česká pirátská strana,Komunistická strana Čech a Moravy,...
586030,Archlebov,752,415,415,25,0,0,47,1,12,49,9,2,3,1,1,39,1,10,89,0,0,73,0,3,1,0,46,3,0
586048,Blatnice pod Svatým Antonínkem,1733,1066,1055,101,1,1,70,4,50,61,7,9,42,0,2,74,2,40,247,0,2,199,0,7,2,1,133,0,0
586056,Blatnička,356,239,238,16,0,0,14,0,10,17,3,0,1,0,0,23,0,4,58,0,5,42,0,0,0,2,43,0,0
...
```

## Licence

Tento projekt je distribuován pod [MIT licencí](https://opensource.org/licenses/MIT).
