#!/usrbin/env python

f = open("three_line_file.txt")

for line in f:
    print line.strip()

f.seek(0)
my_lines = f.readlines()
for line in my_lines:
    print line.strip()

f.seek(0)
my_lines = f.read()
for line in my_lines.splitlines():
    print line

f.close()

#Step 2

with open("three_line_file.txt") as f:
    for line in f:
        print line.strip()

#Step 3
f = open("three_line_file_write.txt", "w")
f.write('New_Line_X\n')
f.close()

#Step 4
with open("three_line_file_write.txt", "a") as f:
    f.write('New_Line_Text\n')
