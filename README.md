# Nmap Recon Wrapper

Python wrapper pro Nmap scan.  
Umožňuje snadno zadat target, porty, rychlost a NSE skripty a automaticky ukládá výstupy.

## 🛠 Požadavky

- Python 3.x
- Nmap nainstalovaný lokálně
- Windows / Linux / Mac (cesta k nmapu se liší)

## ⚙️ Setup

1. Zkopírujte soubor `nmap_dir.txt.example` → `nmap_dir.txt`
2. Do `nmap_dir.txt` napište cestu k `nmap.exe` (např. `C:\Program Files (x86)\Nmap\nmap.exe`)
3. Vytvořte složku `scans/` (pokud neexistuje)

## 🚀 Použití

```bash
python recon.py
