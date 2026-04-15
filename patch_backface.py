import re

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'r') as f:
    text = f.read()

# Remove transform-style: preserve-3d; from .front, .back
text = re.sub(r'text-align: center; transform-style: preserve-3d;', 'text-align: center;', text)

# Ensure backface visibility is hidden for polaroids too
text = re.sub(r'(\.polaroid \{\n.*?cursor: pointer;\n)', r'\1    backface-visibility: hidden;\n', text)

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'w') as f:
    f.write(text)
