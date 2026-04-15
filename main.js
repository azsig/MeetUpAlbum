let books = document.querySelectorAll('.book');
const chooses = document.querySelectorAll('.choose');
let close = document.querySelector('.close');

let currentBook;
let paper; 
let numOfPapers;
let currentState = 0;

let maks = [71, 21, 37];
let files = 'Image/';
let open = [];

function renderBook(bok){
    let file;
    switch(bok.id){
        case 'b1': file = files + '1/'; makeBook(maks[0], bok, file); break;
        case 'b2': file = files + '2/'; makeBook(maks[1], bok, file); break;
        case 'b3': file = files + '3/'; makeBook(maks[2], bok, file); break;
    }
    setTimeout(()=>{
        paper = currentBook.querySelectorAll('.paper');
        numOfPapers = paper.length;
        let frontNodes = bok.querySelectorAll('.front');
        frontNodes.forEach(btn => btn.addEventListener('click', goNext));
        let backNodes = bok.querySelectorAll('.back');
        backNodes.forEach(btn => btn.addEventListener('click', goPrevious));
    }, 1100);
}

close.addEventListener('click', ()=>{
    deactiveBook(currentBook);
});

chooses.forEach(choose =>{
    choose.addEventListener('click', () => {
        let bok;
        switch (choose.id){
            case 'c1': bok = document.querySelector('#b1'); open.push('1'); break;
            case 'c2': bok = document.querySelector('#b2'); open.push('2'); break;
            case 'c3': bok = document.querySelector('#b3'); open.push('3'); break;
        }
        activeBook(bok);
        chooses.forEach(ch => {ch.classList.add('hide')});
        close.classList.remove('hide');
        setTimeout(()=>{ renderBook(currentBook) }, 1000); 
    })
});

function activeBook(book){
    currentBook = book;
    book.classList.remove('deactive');
    let deactive = document.querySelectorAll('.deactive');
    deactive.forEach(div =>{
        div.classList.add('down');
        setTimeout(() => {div.classList.add('hide')}, 1000);
    });
}

function deactiveBook(book){
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
}

function deletePage(book){
    let pages = book.querySelectorAll('.page');
    pages.forEach(pa => { book.removeChild(pa); });
    let bC = book.querySelector('.backCover');
    if(bC) book.removeChild(bC);
    currentState = 0;
}

function openBook() {
    currentBook.style.transform = "translateX(50%)";
}

function closeBook(isFirstPage) {
    if(isFirstPage) {
        currentBook.style.transform = "translateX(0%)";
    } else {
        currentBook.style.transform = "translateX(100%)";
    }
}

function goNext(){
    if (currentState === 0){
        openBook();
        paper[currentState].classList.add('flipped');
        paper[currentState].style.zIndex = currentState + 1;
    }
    else if(currentState === numOfPapers - 1){
        closeBook(false);
        paper[currentState].classList.add("flipped");
        paper[currentState].style.zIndex = currentState + 1;
    }
    else{
        paper[currentState].classList.add('flipped');
        paper[currentState].style.zIndex = currentState + 1;
    }
    currentState++;
}

function goPrevious(){
    if (currentState === 1){
        closeBook(true);
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
    }
    else if(currentState === numOfPapers){
        openBook();
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
    }
    else{
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
    }
    currentState -= 1;
}

const makeBook = (maks, bok, file) => {
    let page = 1;
    let cover = bok.querySelector('.cover');
    let coverFront = cover.querySelector('.front');
    if(coverFront) coverFront.classList.add('cover-part');

    let backCover = document.createElement('div');
    backCover.className = 'paper backCover';
    let depan = document.createElement('div');
    let belakang = document.createElement('div');
    depan.className = 'front';
    belakang.className = 'back';
    backCover.appendChild(depan);
    backCover.appendChild(belakang);
    backCover.style.zIndex = page;
    backCover.id = page;
    
    let papers = [];
    let i = 1;
    
    while(i <= maks){
        let paper = document.createElement('div');
        paper.className = 'paper page';
        
        // Front Face
        let front = document.createElement('div');
        let numFront = Math.min(maks - i + 1, Math.floor(Math.random() * 4) + 1); // 1 to 4
        front.className = 'front layout-' + numFront;
        
        for (let j = 0; j < numFront; j++) {
            let pol = document.createElement('div');
            pol.className = 'polaroid';
            let tape = document.createElement('div'); tape.className = 'tape';
            let img = document.createElement('img'); img.src = file + `${i}.jpg`;
            pol.appendChild(tape); pol.appendChild(img);
            front.appendChild(pol);
            i++;
        }

        // Back Face
        let back = document.createElement('div');
        if (i <= maks) {
            let numBack = Math.min(maks - i + 1, Math.floor(Math.random() * 4) + 1); // 1 to 4
            back.className = 'back layout-' + numBack;
            for (let j = 0; j < numBack; j++) {
                let pol = document.createElement('div');
                pol.className = 'polaroid';
                let tape = document.createElement('div'); tape.className = 'tape';
                let img = document.createElement('img'); img.src = file + `${i}.jpg`;
                pol.appendChild(tape); pol.appendChild(img);
                back.appendChild(pol);
                i++;
            }
        } else {
            back.className = 'back';
        }
        
        paper.appendChild(front);
        paper.appendChild(back);
        
        page++;
        paper.id = page;
        paper.style.zIndex = page;
        papers.push(paper);
    }
    
    page++;
    cover.id = page;
    cover.style.zIndex = page;
    
    setTimeout(()=>{
        for (let p = papers.length - 1; p >= 0; p--){
            bok.appendChild(papers[p]);
        }
        bok.appendChild(backCover);
    }, 800)
};