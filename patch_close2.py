with open('/home/azsig/repos/MeetUpAlbum/main.js', 'r') as f:
    text = f.read()

old_deac = """function deactiveBook(book){
    if (currentState > 0){
        for (let i = 0; i < currentState; i++){
            goPrevious();
        }
    }
    setTimeout(() => {
        deletePage(currentBook);
        let deactive = document.querySelectorAll('.deactive');
        deactive.forEach(div =>{
            div.classList.remove('hide');
            setTimeout(() => {div.classList.remove('down')}, 100);
        });
        book.classList.add('deactive');
        chooses.forEach(ch => {ch.classList.remove('hide')});
    }, 1000);
}"""

new_deac = """function deactiveBook(book){
    close.classList.add('hide'); // Menyembunyikan tombol close
    
    // Simpan hitungan halaman ke variabel sementara
    let flips = currentState;
    
    if (flips > 0){
        // Kembalikan halaman satu per satu dengan delay atau langsung
        for (let i = 0; i < flips; i++){
            goPrevious();
        }
    }
    
    // Tunggu sampai animasi balik halaman selesai sebelum menutup buku sepenuhnya
    setTimeout(() => {
        deletePage(currentBook);
        
        // Hapus styling inline dari JS yang menyebabkan stuck
        currentBook.style.transform = ""; 
        
        // Kita juga harus reset buku-buku lain untuk tampil lagi
        let allBooks = document.querySelectorAll('.book');
        allBooks.forEach(div => {
            div.classList.remove('hide');
            div.classList.add('deactive'); // Mengembalikan miring 3D kelas deactive ke semua buku
            setTimeout(() => {div.classList.remove('down')}, 50);
        });
        
        // Munculkan kembali tombol pilihan
        chooses.forEach(ch => {ch.classList.remove('hide')});
    }, 800); // Tunggu sampai animasi balik (goPrevious) selesai
}"""

text = text.replace(old_deac, new_deac)

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'w') as f:
    f.write(text)

