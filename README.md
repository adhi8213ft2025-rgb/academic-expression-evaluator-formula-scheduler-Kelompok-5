# ACADEMIC EXPRESSION EVALUATOR & FORMULA SCHEDULER 
Academic Expression Evaluator Formula Scheduler Kelompok 5
Langkah-Langkah Pembuatan Projek Algoritma Dan Struktur Data :
# 🎓ACADEMIC EXPRESSION EVALUATOR & FORMULA SCHEDULER 
python 3.8+ Mata Kuliah Algoritma & Struktur Data Status In Progress

Proyek Academic Expression Evaluator & Formula Scheduler ini dikembangkan sebagai pemenuhan tugas Team Based Project (TA 2025/2026) untuk mata kuliah ELT60213 Algoritma dan Struktur Data, Teknik Elektro, Universitas Negeri Yogyakarta.

Sistem ini dirancang untuk membantu dosen dan mahasiswa dalam mengevaluasi ekspresi akademik serta menyusun penjadwalan formula secara otomatis. Evaluasi ekspresi mencakup analisis keterbacaan, validasi sintaks formula, dan pengukuran kompleksitas ekspresi matematika maupun logika.

Selain itu, modul Formula Scheduler memanfaatkan struktur data seperti Stack, Queue, Tree, dan Graph (DAG) untuk mengatur urutan evaluasi formula berdasarkan dependensi dan prioritas proses. Seluruh struktur data dibangun secara murni (from scratch) tanpa menggunakan pustaka koleksi bawaan Python guna mendemonstrasikan pemahaman fundamental algoritma.

👥 Tim Pengembang (Kelompok)
=======================================================
NIM                        Nama Lengkap                       
=======================================================
25051030093     Adhi Suryo Kuncoro                 
25051030097     Raihan fahreza augustha            
25051030106     MUHAMMAD FAUZAN NUR PRIBOWO        
25051030123     LUCKY MAYLANDRA NUR SALEH          
=======================================================

🧩 Modul Sistem (6 Modul Fungsional Terintegrasi)

Sistem ini dipecah menjadi 6 modul fungsional yang saling terintegrasi:

1. Modul 1: BST Tabel Variabel
Menggunakan Binary Search Tree (BST) untuk penyimpanan variabel secara terurut.
Mendukung operasi insert, search, dan update variabel.
Kompleksitas pencarian rata-rata:
O(logn)
2. Modul 2: CLI Kalkulator
Antarmuka berbasis Command Line Interface (CLI) untuk input ekspresi matematika.
Mendukung evaluasi formula interaktif dan penanganan error (error handling).
Memudahkan pengguna menjalankan operasi secara real-time.
3. Modul 3: Evaluasi_Postfix
Mengevaluasi ekspresi postfix menggunakan struktur data Stack.
Mendukung operator aritmatika dasar seperti +, -, *, /, dan ^.
Kompleksitas evaluasi ekspresi:
O(n)
4. Modul 4: Expression_Tree (Binary Tree)
Merepresentasikan ekspresi matematika dalam bentuk Binary Expression Tree.
Digunakan untuk proses traversal preorder, inorder, dan postorder.
Mempermudah visualisasi struktur operasi matematika.
5. Modul 5: Graph_Dependensi_Formula (DAG)
Menggunakan Directed Acyclic Graph (DAG) untuk memodelkan dependensi antar formula.
Mendukung proses topological sorting untuk menentukan urutan evaluasi formula.
Deteksi siklus digunakan untuk mencegah dependensi melingkar (cyclic dependency).
6. Modul 6: Konversi_Infix_Ke_Postfix
Mengimplementasikan algoritma Shunting-Yard untuk konversi ekspresi.
Mengubah ekspresi infix menjadi postfix berdasarkan prioritas operator.
Menggunakan struktur data Stack untuk pengelolaan operator.

📂 Struktur Direktori
📁 Academic-Expression-Evaluator-Formula-Scheduler/
├── 📄 README.md                 # Dokumentasi Proyek
├── 📁 src/                      # Source Code Utama
│   ├── 📄 main.py               # Entry Point 
│   ├── 📁 data_structures/      # Struktur Data Murni (From Scratch)
│   │   ├── linked_list.py
│   │   ├── stack.py
│   │   ├── queue_ll.py
|   |   |── bst.py
|   |   |──graph.py
│   ├── 📁 modules/              # Implementasi Algoritma
│   │   ├── modul_1_BST_Tabel_Variabel.py
│   │   ├── modul_2_CLI_Kalkulator.py
│   │   ├── modul_3_Evaluasi_Postfix.py
│   │   ├── modul_4_Expression_Tree(BinaryTree).py
│   │   ├── modul_5_Graph_Dependensi_Formula(GDF).py
|   |   |── MODUL_6_kONVERSI_Infix_Ke_Postfix.py
├── 📁 experiments/              # Skrip Uji Coba Performa
│   └── 📄 benchmark.py          
├── 📁 docs/                     # Berkas Laporan Laporan
│   ├── Laporan_Final.pdf
│   └── Slide_Presentasi.pdf
└── 📁 AI_Log/                   # Log Penggunaan AI Assistant
    ├── Log_prompt.txt
    └── screenshots/


