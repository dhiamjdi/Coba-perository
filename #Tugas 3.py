#Tugas 3

siswa = ["dhia", "raffa", "mail", "fizi", "jarjit"]

hadir = []
jumlah = int(input("berapa jumlah siswa yang hadir: "))

#loop 1 : masuk daftar hadir
for i in range(jumlah):
    nama = input(f"masukan nama siswa ke-{i+1} yang hadir: ")


    if nama in siswa:
        konfirmasi = input("apakah kamu sudah absen? (ya/tidak)")
        if konfirmasi == "ya":
            tugas = input("apakah sudah mengumpulkan tugas hari ini? (ya/tidak)")
            if tugas == "ya":
                print("mantap,selamat kau")
            else:
                print("matilah kau, cepat kerjakan sekarang!")
        else:
            print("absen dulu sebelum terlambat")
    else:
        print("kamu bukan siswa kelas ini")
        