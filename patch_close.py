import re

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'r') as f:
    text = f.read()

# Fix deactiveBook logic to clear style.transform and hide close button properly
deactive_func = """function deactiveBook(book){
    close.classList.add('hide'); // Menyembunyikan tombol close
    if (currentState > 0){
        let flips = currentState;
        for (let i = 0; i < flips; i++){
            goPrevious();
        }
    }
    // Tunggu sampai animasi balik halaman selesai sebelum menutup buku sepenuhnya
    setTimeout(() => {
        deletePage(currentBook);
        currentBook.style.transform = ""; // Menghapus style inline agar transform kelas deactive bisa berjalan!
        
        let allBooks = document.querySelectorAll('.book');
        allBooks.forEach(div =>{
            div.classList.remove('hide');
            div.classList.add('deactive'); // Mengembalikan class deactive ke semua buku
            setTimeout(() => {div.classList.remove('down')}, 50);
        });
        chooses.forEach(ch => {ch.classList.remove('hide')});
    }, 1300); // Waktu yang cukup untuk halaman membalik kembali
}"""

text = re.sub(r'function deactiveBook\(book\)\{.*?\n\}\n(?=function deletePage)', deactive_func + '\n', text, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'w') as f:
    f.write(text)

# Now fix the symbols in index.html
with open('/home/azsig/repos/MeetUpAlbum/index.html', 'r') as f:
    html_text = f.read()

html_text = html_text.replace('<div class="bg-shape shape1">❤️</div>', '<div class="bg-shape shape1">🎀</div>')
html_text = html_text.replace('<div class="love-badge">♥</div>', '<div class="love-badge">✦</div>')

with open('/home/azsig/repos/MeetUpAlbum/index.html', 'w') as f:
    f.write(html_text)

