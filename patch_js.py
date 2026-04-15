import re

with open('/home/azsig/repos/MeetUpAlbum/main.js', 'r') as f:
    text = f.read()

# For front
front_cases = """
            case 4:
                for(let k=0; k<4; k++) {
                    let im = document.createElement('img');
                    im.id = 'img' + (k+1);
                    im.src = file + `${i+1}.jpg`;
                    front.appendChild(im);
                    i++;
                }
                break;
            case 3:
                for(let k=0; k<3; k++) {
                    let im = document.createElement('img');
                    im.id = 'img' + (k+1);
                    im.src = file + `${i+1}.jpg`;
                    front.appendChild(im);
                    i++;
                }
                break;
"""

# For back
back_cases = """
            case 4:
                for(let k=0; k<4; k++) {
                    let im = document.createElement('img');
                    im.id = 'img' + (k+1);
                    im.src = file + `${i+1}.jpg`;
                    back.appendChild(im);
                    i++;
                }
                break;
            case 3:
                for(let k=0; k<3; k++) {
                    let im = document.createElement('img');
                    im.id = 'img' + (k+1);
                    im.src = file + `${i+1}.jpg`;
                    back.appendChild(im);
                    i++;
                }
                break;
"""

text = text.replace("case 2:\n                let img1 = document.createElement('img');\n                img1.id = 'img1';", front_cases + "            case 2:\n                let img1 = document.createElement('img');\n                img1.id = 'img1';", 1)

# we need to be careful. Let's just rewrite makeBook using sed or a python script replacing the whole function.

