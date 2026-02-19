To run in windows cmd:
```powershell
python export_tree.py C:\Users\Astrxgore\Desktop\Obsidian\Productivity-OS\ -o structure.md
```

to run in linux bash:
```sh
python3 export_tree.py ~/Рабочий\ Стол/Obsidian -o structure.md
```

Примеры флагов:
```sh
python export_tree.py . -o tree.md --max-depth 3
python export_tree.py . -o tree.md --ignore-dir dist --ignore-dir build
python export_tree.py . -o tree.md --ignore-file .env --ignore-file secrets.txt
```
