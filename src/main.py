import sys
import os

from modules.CLI_Kalkulator import jalankan_kalkulator_cli

# Menambahkan path otomatis agar file bisa di-run dari folder mana saja
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.modules import CLI_Kalkulator
except ModuleNotFoundError:
    # FIX 1: Ditambah '# type: ignore' agar Pylance tidak protes di baris ini
    import cli_kalkulator # type: ignore

def main():
    """Pusat kendali utama untuk menjalankan aplikasi Kelompok 5."""
    print("-----------------------------------------------------")
    print("-----------ACADEMIC EXPRESSION CALCULATOR------------")
    print("-----------------------------------------------------")
    print("Sistem Terintegrasi: Stack, Queue, BST, & Expression Tree")
    print("---------------------------------------------------\n")
    
    # 💡 FIX 2: Menggunakan getattr dinamis agar Pylance tidak mengecek fungsi secara kaku
    fungsi_utama = None
    for nama_fungsi in ['run', 'main', 'menu', 'main_cli']:
        fungsi_utama = getattr(cli_kalkulator, nama_fungsi, None)
        if fungsi_utama is not None:
            break
            
    try:
        if fungsi_utama is not None:
            fungsi_utama()
        else:
            print("Error: Fungsi penggerak menu di cli_kalkulator.py tidak terdeteksi.")
            print("Silakan buka file src/modules/cli_kalkulator.py untuk melihat nama fungsinya.")
            
    except KeyboardInterrupt:
        print("\nAplikasi dihentikan oleh pengguna. Sampai jumpa!")
        sys.exit(0)
    except Exception as e:
        print(f"\nTerjadi kesalahan fatal pada sistem: {e}")
        sys.exit(1)
def main():
    jalankan_kalkulator_cli()
if __name__ == "__main__":
    jalankan_kalkulator_cli()