# function c'est une function qui appel elle meme dans la meme function
def recursive(n, limit):
    if n > limit:
        return
    print("n : ", n)
    recursive(n * n, limit)


recursive(2, 300)
