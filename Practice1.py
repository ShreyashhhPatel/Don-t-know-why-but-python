# //1. Read a line; **while** it's non-empty, print its **length** using `:=` and prompt again.  
#    _Expected_: prints lengths until blank line.

# ---

# x = input("A whole lonng line.")
# y = join(sorted(set(x)));
while (line := input("Write a line: ")):
    print(f"Length of line is {len(line)}")

print("Done")