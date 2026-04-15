import re

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'r') as f:
    text = f.read()

def_makeBook = """const makeBook = (maks,bok, file) => {
    let page = 1;
    let cover = bok.querySelector('.cover');
    let backCover = document.createElement('div');
    backCover.classList.add('paper');
    backCover.classList.add('backCover')
    let depan = document.createElement('div');
    let belakang = document.createElement('div');
    depan.classList.add('front');
    belakang.classList.add('back');
    backCover.appendChild(depan);
    backCover.appendChild(belakang);
    backCover.style.zIndex = page;
    backCover.id = page;
    let papers = [];
    let i = 0;
    while(i<maks){
        let num = random();
        let num2 = random();
        let paper = document.createElement('div');
        paper.classList.add('paper');
        paper.classList.add('page');
        let front = document.createElement('div');
        front.classList.add('front');
        
        let remaining = maks - i;
        if(remaining < num) num = remaining;
        
        front.classList.add('photos-' + num);

        for (let j = 0; j < num; j++) {
            let img = document.createElement('img');
            img.src = file + `${i+1}.jpg`;
            front.appendChild(img);
            i++;
        }

        let back = document.createElement('div');
        back.classList.add('back');
        
        remaining = maks - i;
        if(remaining < num2) num2 = remaining;
        
        back.classList.add('photos-' + num2);

        for (let j = 0; j < num2; j++) {
            let img = document.createElement('img');
            img.src = file + `${i+1}.jpg`;
            back.appendChild(img);
            i++;
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
        for (i = papers.length - 1; i >=0; i--){
            bok.appendChild(papers[i]);
        }
        bok.appendChild(backCover);
    }, 1000)
}"""

text = re.sub(r'const makeBook = \(maks,bok, file\) => \{.*', def_makeBook, text, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'w') as f:
    f.write(text)
