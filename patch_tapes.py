import re

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'r') as f:
    text = f.read()

# Make sure tape has backface-visibility: hidden too
text = re.sub(r'(\.tape \{\n.*?z-index: 10; box-shadow: 0 1px 2px rgba\(0,0,0,0\.1\);\n)', r'\1    backface-visibility: hidden;\n', text)

with open('/home/azsig/repos/MeetUpAlbum/style.css', 'w') as f:
    f.write(text)
