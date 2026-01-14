# Simulator Automat Finit Nondeterminist cu λ-tranziții

## Descriere
Acest proiect implementează un **program care simulează funcționarea unui automat finit nedeterminist cu λ-tranziții**, conform cerințelor din cadrul disciplinei **Compilatoare**.

Programul citește dintr-un fișier definiția completă a unui automat finit nedeterminist cu λ-tranziții (stări, stare inițială, stări finale, alfabetul automatului, tranzițiile) și permite testarea unui număr oarecare de șiruri de intrare.  
Pentru fiecare șir introdus, programul determină dacă acesta este **acceptat (DA)** sau **respins (NU)** de automat.

---

## Cerință (enunț)
Se cere realizarea unui program care:
- simulează funcționarea unui automat finit nedeterminist cu λ-tranziții;
- citește dintr-un fișier elementele automatului (stările, starea inițială, stările finale, alfabetul automatului, tranzițiile);
- permite citirea unui număr oarecare de șiruri peste alfabetul de intrare al automatului;
- pentru fiecare șir afișează **DA** sau **NU**, în funcție de faptul că șirul aparține sau nu limbajului acceptat de automat.

---

## Format fișier automat 
Fișierul de intrare conține:

- `states:` lista stărilor
- `start:` starea inițială
- `final:` lista stărilor finale
- `in:` alfabetul de intrare
- `out:` alfabetul de ieșire (dacă este folosit)
- apoi tranzițiile, câte una pe linie, în formatul:

`stare_curentă simbol_intrare simbol_iesire stare_următoare`

Unde:
- `lambda` reprezintă tranziție ε (nu consumă simbol din intrare) sau ieșire ε (nu produce simbol în ieșire)
