import time;

createdAt = time.time();

for i in range(1, 1000000) :
    print(i);

endedAt = time.time();

print(f"\n\033[90;1mProcess Completed in {endedAt - createdAt :.3f} seconds.\033[0m\n")
