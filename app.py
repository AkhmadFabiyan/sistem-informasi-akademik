import os

# Definisikan struktur folder dan file
structure = {
    "Driver calculation": {
        "app": {
            "__init__.py": "",
            "routes.py": "",
            "utils.py": "",
            "templates": {
                "index.html": "",
            },
            "static": {
                "styles.css": "",
                "script.js": "",
            },
        },
        "app.py": "",
        "requirements.txt": "",
    }
}

# Fungsi untuk membuat folder dan file sesuai struktur
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Jika konten adalah dict, buat folder dan isi foldernya
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Jika konten adalah string, buat file
            with open(path, "w") as f:
                f.write(content)

# Jalankan fungsi
base_path = os.getcwd()  # Folder kerja saat ini
create_structure(base_path, structure)

print("Struktur folder dan file berhasil dibuat!")
