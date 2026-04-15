import re
with open('/home/azsig/repos/MeetUpAlbum/style.css', 'r') as f:
    content = f.read()

# Replace the max-width: 768px sections to the end
new_media = """@media (max-width: 768px) {
    .table { height: 70vh; }
    .book { width: 40vw; height: 55vw; max-width: 250px; max-height: 340px; }
    .deactive { margin: 8px; transform: rotateX(15deg) rotateY(-20deg) scale(0.6); }
    button { margin: 0 5px; font-size: 0.9rem; padding: 10px 14px; }
}

@media (max-width: 480px) {
    .bg-shape { display: none; }
    
    /* Make the base book fit exactly inside the mobile screen without scrolling when opened */
    /* When opened, right side moves 50% = 22.5vw. Left side flips to -45vw. Total width = 90vw. */
    .book { width: 44vw; height: 60vw; }
    
    /* Overlap the deactive books so they look cute and don't take up too much width */
    .table { display: flex; flex-direction: row; flex-wrap: wrap; height: 75vh; }
    
    /* They remain books, we just scale them down further and overlap them */
    .deactive { 
        transform: rotateX(10deg) rotateY(-10deg) scale(0.5) rotate(calc(var(--angle, 0) * 10deg));
        margin: -4vw; /* Overlap them */
    }
    
    .deactive:nth-child(1) { --angle: -2; z-index: 1; }
    .deactive:nth-child(2) { --angle: 0.5; z-index: 3; margin-top: 5vh; }
    .deactive:nth-child(3) { --angle: 2; z-index: 2; }
    
    .pilihan { flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; width: 100%; }
    button { padding: 8px 14px; font-size: 0.8rem; margin: 2px; }   
    
    /* Resize Cover Elements */
    .cover-design { font-size: 1.8rem; }
    .cover-design span { font-size: 0.9rem; }
    
    /* Adjust tape for tiny polaroids */
    .tape { height: 10px; width: 35px; top: -5px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
}"""

content_new = re.sub(r'@media \(max-width: 768px\).*', new_media, content, flags=re.DOTALL)

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'w') as f:
    f.write(content_new)

