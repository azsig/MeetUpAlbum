let books = document.querySelectorAll('.book');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
let chooses = document.querySelectorAll('.choose');
let close = document.querySelector('.close')

// prevBtn.addEventListener("click", goPrevious);
// nextBtn.addEventListener("click", goNext);

let currentBook;
let front;
let back;

let paper; 
let numOfPapers;

let currentState = 0;

let maks = [71,21,37]

let files = 'Image/'

function renderBook(bok){
    let file;
    switch(bok.id){
        case 'b1':
            file = files+'1/'
            makeBook(maks[0],bok,file);
            break;
        case 'b2':
            file = files+'2/'
            makeBook(maks[1],bok,file);
            break;
        case 'b3':
            file = files+'3/'
            makeBook(maks[2],bok,file);
            break;
    }
    setTimeout(()=>{
        paper = currentBook.querySelectorAll('.paper');
        numOfPapers = paper.length;
        front = bok.querySelectorAll('.front');
        front.forEach(btn => btn.addEventListener('click', goNext))
        back = bok.querySelectorAll('.back');
        back.forEach(btn => btn.addEventListener('click', goPrevious))
    }, 1100)
    
}

close.addEventListener('click', ()=>{
    deactiveBook(currentBook)
})

let open = []

chooses.forEach(choose =>{
    choose.addEventListener('click',() => {
        let bok;
        switch (choose.id){
            case 'c1':
                bok = document.querySelector('#b1');
                open.push('1');
                break;
            case 'c2':
                bok = document.querySelector('#b2');
                open.push('2');
                break;
            case 'c3':
                bok = document.querySelector('#b3');
                open.push('3');
                break;
        }
        activeBook(bok);
        chooses.forEach(ch => {ch.classList.add('hide')});
        close.classList.remove('hide');
        setTimeout(()=>{renderBook(currentBook)}, 2000);
    })
})


function activeBook(book){
        currentBook = book;
        book.classList.remove('deactive');
        let deactive = document.querySelectorAll('.deactive')
        deactive.forEach(div =>{
            div.classList.add('down');
            setTimeout(() => {div.classList.add('hide')}, 2000)
        })
}

function deactiveBook(book){
    if (currentState > 0){
        for (i = 0; i<currentState+1; i++){
            goPrevious()
        }
    }
    deletePage(currentBook)
    let deactive = document.querySelectorAll('.deactive')
    deactive.forEach(div =>{
        div.classList.remove('hide');
        setTimeout(() => {div.classList.remove('down')}, 2000)
    })
    book.classList.add('deactive');
    chooses.forEach(ch => {ch.classList.remove('hide')});
}

function deletePage(book){
    let pages = book.querySelectorAll('.page');
    pages.forEach(pa => {
        book.removeChild(pa);
    })
    let bC = book.querySelector('.backCover')
    book.removeChild(bC);
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

function random(){
    let number = Math.floor(Math.random() * 2 - 1 + 1 ) + 1 ;
    return number;
}


function goNext(){
    if (currentState == 0){
        openBook();
        paper[currentState].classList.add('flipped');
        paper[currentState].style.zIndex = currentState+1;
    }
    else if(currentState == numOfPapers-1){
        closeBook(false);
        paper[currentState].classList.add("flipped");
        paper[currentState].style.zIndex = currentState + 1;
    }
    else{
        paper[currentState].classList.add('flipped');
        paper[currentState].style.zIndex = currentState+1;
    }
    currentState++
}



 function goPrevious(){
     if (currentState == 1){
        closeBook(true)
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
     }
     else if(currentState == numOfPapers){
        openBook()
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
     }
     else{
        paper[currentState-1].classList.remove('flipped');
        paper[currentState-1].style.zIndex = paper[currentState-1].id;
     }
     currentState-=1
}

const makeBook = (maks,bok, file) => {
    let page = 1;
    let cover = bok.querySelector('.cover');
    let backCover = document.createElement('div');
    backCover.classList.add('paper');
    backCover.classList.add('backCover')
    let depan = document.createElement('div');
    let belakang = document.createElement('div')
    depan.classList.add('front')
    belakang.classList.add('back');
    backCover.appendChild(depan);
    backCover.appendChild(belakang)
    backCover.style.zIndex = page;
    backCover.id = page;
    let papers = []
    let i = 0
    while(i<maks){
        let num = random()
        let num2 = random()
        let paper = document.createElement('div');
        paper.classList.add('paper');
        paper.classList.add('page')
        let front = document.createElement('div');
        front.classList.add('front');
        if(maks - i == 2){
            num = 1;
            num2 = 1;
        }
        else if(maks -i == 1){
            num = 1
            num2 = 0
        }
        switch(num){
            case 2:
                let img1 = document.createElement('img');
                img1.id = 'img1';
                img1.src = file+`${i+1}.jpg`
                i++
                let img2 = document.createElement('img');
                img2.id = 'img2';
                img2.src = file+`${i+1}.jpg`
                i++
                front.appendChild(img1);
                front.appendChild(img2);
                break;
            case 1:
                let img = document.createElement('img');
                img.id = 'img';
                img.src = file + `${i+1}.jpg`
                front.appendChild(img)
                i++
                break;
            default:
                break;
        }
        let back = document.createElement('div');
        back.classList.add('back');
        switch(num2){
            case 2:
                let img1 = document.createElement('img');
                img1.id = 'img1';
                img1.src = file + `${i+1}.jpg`;
                i++
                let img2 = document.createElement('img');
                img2.id = 'img2';
                img2.src = file + `${i+1}.jpg`;
                i++
                back.appendChild(img1);
                back.appendChild(img2);
                break;
            case 1:
                let img = document.createElement('img');
                img.id = 'img';
                img.src = file + `${i+1}.jpg`;
                back.appendChild(img);
                i++
                break;
            default:
                break;
        }
        paper.appendChild(front);
        paper.appendChild(back);
        page++;
        paper.id = page
        paper.style.zIndex = page
        papers.push(paper);
    }
    page++
    cover.id = page
    cover.style.zIndex = page;
    setTimeout(()=>{
        for (i = papers.length - 1; i >=0; i--){
            bok.appendChild(papers[i]);
        }
        bok.appendChild(backCover);
    }, 1000)
    
}
