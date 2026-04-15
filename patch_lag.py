import re

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'r') as f:
    text = f.read()

def_makeBook = """const makeBook = (maks, bok, file) => {
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
};"""

text = re.sub(r'const makeBook = \(maks, bok, file\) => \{.*', def_makeBook, text, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'w') as f:
    f.write(text)

css_patch = """
/* POLAROID SCRAPBOOK STYLE */
.polaroid {
    background: #fff; padding: 6px 6px 25px 6px;
    box-shadow: 2px 4px 10px rgba(0,0,0,0.1);
    position: absolute; transition: transform 0.2s, z-index 0.2s;
    border: 1px solid #f5f5f5; display: flex; flex-direction: column; cursor: pointer;
}
.polaroid img {
    width: 100%; height: 100%; object-fit: cover; background: #fdfdfd; border: 1px solid #eee;
}

.tape {
    position: absolute; top: -8px; left: 50%; transform: translateX(-50%) rotate(-2deg);
    width: 40px; height: 15px; background-color: rgba(255, 182, 193, 0.8);
    z-index: 10; box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.polaroid:hover {
    transform: scale(1.15) translateZ(40px) !important;
    z-index: 50 !important; box-shadow: 5px 10px 20px rgba(255, 117, 140, 0.3);
}

/* 1 PHOTO */
.layout-1 .polaroid { width: 65%; height: 50%; top: 25%; left: 17.5%; transform: rotate(-2deg); }

/* 2 PHOTOS */
.layout-2 .polaroid { width: 45%; height: 35%; }
.layout-2 .polaroid:nth-child(1) { top: 10%; left: 10%; transform: rotate(-5deg); }
.layout-2 .polaroid:nth-child(2) { bottom: 10%; right: 10%; transform: rotate(5deg); }

/* 3 PHOTOS */
.layout-3 .polaroid { width: 35%; height: 30%; }
.layout-3 .polaroid:nth-child(1) { top: 5%; left: 10%; transform: rotate(-8deg); }
.layout-3 .polaroid:nth-child(2) { top: 35%; right: 8%; transform: rotate(6deg); }
.layout-3 .polaroid:nth-child(3) { bottom: 5%; left: 15%; transform: rotate(-3deg); }

/* 4 PHOTOS */
.layout-4 .polaroid { width: 32%; height: 28%; }
.layout-4 .polaroid:nth-child(1) { top: 7%; left: 7%; transform: rotate(-6deg); }
.layout-4 .polaroid:nth-child(2) { top: 15%; right: 7%; transform: rotate(8deg); }
.layout-4 .polaroid:nth-child(3) { bottom: 15%; left: 7%; transform: rotate(-4deg); }
.layout-4 .polaroid:nth-child(4) { bottom: 7%; right: 7%; transform: rotate(5deg); }
"""

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'r') as f:
    css_text = f.read()

css_text = re.sub(r'/\* POLAROID SCRAPBOOK STYLE \*/.*(@media \(max-width: 768px\))', css_patch + '\n\\1', css_text, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'w') as f:
    f.write(css_text)

