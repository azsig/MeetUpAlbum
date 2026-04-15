import re

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'r') as f:
    text = f.read()

# Replace the ID based image styles with structurally styled ones based on front/back photos-X classes
new_css = """
.front img,
.back img {
    position: absolute;
    box-shadow: 2px 4px 8px rgba(0,0,0,0.3);
    transition: transform 0.3s;
    background: white;
}

.front img:hover,
.back img:hover {
    transform: scale(1.1) translateZ(10px);
    z-index: 10;
}

/* 1 Photo Layout */
.photos-1 img {
    width: 65%;
    border: 5px solid white;
}

/* 2 Photos Layout */
.photos-2 img {
    width: 38%;
    border: 5px solid white;
}
.photos-2 img:nth-child(1) {
    left: 6%;
    top: 6%;
    transform: rotate(-15deg);
}
.photos-2 img:nth-child(2) {
    right: 6%;
    bottom: 6%;
    transform: rotate(15deg);
}

/* 3 Photos Layout */
.photos-3 img {
    width: 34%;
    border: 4px solid white;
}
.photos-3 img:nth-child(1) {
    left: 6%;
    top: 6%;
    transform: rotate(-12deg);
}
.photos-3 img:nth-child(2) {
    right: 6%;
    top: 6%;
    transform: rotate(8deg);
}
.photos-3 img:nth-child(3) {
    right: 6%;
    bottom: 6%;
    transform: rotate(-10deg);
}

/* 4 Photos Layout */
.photos-4 img {
    width: 28%;
    border: 4px solid white;
}
.photos-4 img:nth-child(1) {
    left: 6%;
    top: 6%;
    transform: rotate(-10deg);
}
.photos-4 img:nth-child(2) {
    right: 6%;
    top: 6%;
    transform: rotate(15deg);
}
.photos-4 img:nth-child(3) {
    left: 6%;
    bottom: 6%;
    transform: rotate(-5deg);
}
.photos-4 img:nth-child(4) {
    right: 6%;
    bottom: 6%;
    transform: rotate(10deg);
}

.front,
"""

# The original has `#img1, #img2, #img { ... }` down to `.front, \n.back{`
import re
text = re.sub(r'#img1,\n#img2,\n#img\{\n.*?\.front,\n\.back\{', new_css + '.back{', text, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'w') as f:
    f.write(text)
