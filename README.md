# L’intèrpret de λ-càlcul AChurch
Repositori de la Practica de Llenguatges de Programació, feta el quatrimestre de primavera del curs 2022-2023. La pràctica és un Bot de Telegram que traballa amb expressions de lambda càlcul. Fa α-conversions i β-reduccions

## Fitxers del repositori
* ```lc.g4```: Gramàtica de l'interpret
* ```achurch.py```: Intèrpret amb el bot
* ```README.md```: el fitxer des d'on llegiu això

## Instrucions d'execució
Abans que res, aquest treball s'ha fet amb Python 3.10 i antlr. Necessiteu tenir-los instal·lats els dos abans d'executar. La intal·lació està explicada a les transparències de l'assignatura.

Primer de tot compilem el fitxer ```lc.g4```, creant així alguns fitxers complementaris que necessitarem pel següent pas.

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4
```

Seguidament podrem executar el bot amb la comanda següent

```bash
python achurch.py
```

**Important: Per executar el bot necessitareu el token d'un bot de Telegram**. Podeu aconseguir-lo molt facilment mitjançant la web de la mateixa plataforma, que ja té les instruccions. **El token l'heu de posar a un fitxer que es digui ```token.txt```** a la mateixa carpeta dels arxius. Seguidament executar bot.

## Opcions del bot
Per començar a fer servir el bot des de *Telegram* heu de fer servir la comanda ```/start```. Seguidament teniu vàries opcions:
1. ```/help``` per veure tot el que podeu fer amb el bot.
2. ```/author``` per veure informació sobre l'autora del bot.
3. ```/macros``` per veure la llista de macros que té el bot guardat, en cas que en tingui alguna.
4. **Una expressió de lambda càlcul**: Per escriure la lletra lambda podeu fer servir "λ" o bé "\\". Pel que fa les variables, seran caràcters en minúscula. L'expressió pot contenir macros, simbolitzades sempre en lletres  majúscules o símbols (en cas de les macro infixes).
5. Per introduir una **nova macro** farem servir: ```MACRO ≡ expressio```. En cas que es tracti d'una macro infixa també podrem fer servir: ```MACRO = expressio```
