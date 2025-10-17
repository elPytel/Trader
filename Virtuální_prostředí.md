# Virtuální prostředí
Jak vytvořit, aktivovat a opustit virtuální prostředí na Windows.

## Virtuální prostředí v Pythonu

Vytvářejí se pomocí modulu `venv`, který je součástí standardní knihovny Pythonu od verze 3.3. Jako cílovou složku virtuálního prostředí můžete použít libovolné jméno a umístění.

### Vytvoření (ve složce projektu)
```
python -m venv .venv
```

### Aktivace
PowerShell:
```powershell
.\.venv\Scripts\activate
```
CMD:
```cmd
.\.venv\Scripts\activate
```
Git Bash / Bash:
```bash
source .venv/Scripts/activate
```

### Opustit / deaktivovat
```
deactivate
```

## conda

Ve výchozím nastavení conda vytvoří prostředí do složky `envs` v rámci instalace Anaconda/Miniconda, např.
`C:\Users\<UŽIVATEL>\anaconda3\envs\tws_env` nebo `C:\Users\<UŽIVATEL>\miniconda3\envs\tws_env`. Můžete však také určit vlastní umístění pro nové prostředí zadáním úplné cesty.

### Vytvoření
```
conda create -n tws_env python=3.9
```

### Aktivace
```
conda activate tws_env
```

### Deaktivace
```
conda deactivate
```

### Odstranění
```
conda remove -n tws_env --all
```