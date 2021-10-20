import numpy as np

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for tx4t
    h = 1
    d = 256

    # The value of h would be "pow(d, M-1)%q"

    while i < (M-1):
        h = (h * d) % q
        i+=1

    # Calculate the hash value of pattern and first window
    # of text
    i = 0
    while i < M:
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
        i+=1

    # Slide the pattern over text one by one
    i = 0
    while i < (N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            j = 0
            while j < M:
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
                j +=1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
        i+=1

def calaculate_plagiarism_rate(self, hash_table):
        th_a = len(hash_table["a"])
        th_b = len(hash_table["b"])
        a = hash_table["a"]
        b = hash_table["b"]
        sh = len(np.intersect1d(a, b))
        p = (float(2 * sh) / (th_a + th_b)) * 100
        return p


# Driver Code
txt = "nt=*funsgi=*icvect|cc.sizei=i+*coutccvect|cc.sizeccendlMatrice=vect|cc[i]Pixel=vect|cc[i]Pixel=vect|cc[i]bo=testLinePixel.getX,Pixel.getY,Pixel.getX,Pixel.getY,Matriceifbortntnt=nt+*rt-*"
pat = "ixel=vect|cc[i]Pixel=vect|cc[i]bo=testLinePixel.getX,Pixel.getY,Pixel.getX,Pixel.getY,Matriceifbortntnt=nt+*rt-*"

# A prime number
q = 101

# Function Call
search(pat, txt, q)
