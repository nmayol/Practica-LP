# L’intèrpret de λ-càlcul AChurch
Repositori de la Practica de Llenguatges de Programació, feta el quatrimestre de primavera del curs 2022-2023. La pràctica és un Bot de Telegram que traballa amb expressions de lambda càlcul. Fa α-conversions i β-reduccions

## Fitxers del repositori
* lc.g4: Gramàtica de l'interpret
* achurch.py: Intèrpret
* bot.py: Fitxer intèrpret + bot 
* la resta de fitxers són bé fitxers que es creen al compilar o bé coses meves.

## Instrucions d'execució

He posat els fitxers de dos maneres diferents: Podeu executar l'intèrpret o el bot sencer.

### Execució de l'intèrpret
Primer de tot hem de compilar la gramàtica creada amb antlr4, que conté

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
```
 

Per executar només l'intèrpret:
```bash
python achurch.py
```

### Execució del bot
**Important: Per executar el bot necessitareu el token d'un bot de Telegram**. Podeu aconseguir-lo molt facilment mitjançant la web de la mateixa plataforma, que ja té les instruccions. El token l'heu de posar a un fitxer que es digui token.txt a la mateixa carpeta dels arxius. Seguidament executar la mateixa seqüència de comandes.

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
```

Ara però, farem servir el fitxer bot.py
```bash
python bot.py
```
