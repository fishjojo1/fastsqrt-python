# fastsqrt-python
Crude implementation of newton's sqrt approximation method

I was rather bored one night, and thus decided to try my hand at implementing a python version of newton's sqrt approximation method. This was *heavily* inspired by [quake's famous inverse square root function](https://betterexplained.com/articles/understanding-quakes-fast-inverse-square-root/).


The goal was not to use any "computationally expensive" operators such as ^ or sqrt()(duh), but math.log10 is still used, albeit not very computationally intensive(i might be wrong, but to my knowledge, cpu instruction sets make logarithm functions less computationally intensive than one would seem)

## The actual approximation function

Newton's approximation function is as follows: newGuess = 0.5 * (prevGuess + (N / prevGuess)), where N is the number to be squarerooted.

It might look a tad complex at first glance, but there really isn't much magic going on.

Dissecting the function, we have

> prevGuess + (N / prevGuess) 

Afterwhich, the resultant value is halved

To hopefully try to allow one to see the light, say that prevGuess is right on point, eg. N = 100, prevguess = 10

the function would then be as follows, 0.5 * (10 + (100/10) = 10

starting to see how it works now?

Should the guessed root be *lower* than the actual root, N/prevGuess would be a number *higher* than the previously guessed root AND the actual root, and thus the average of both the previously guessed root AND the actual root is used as a new approximation.

A few iterations of the function is than ran through, which *hopefully* produces a somewhat accurate result.

## The initial guess

Here's where things get hard.
Quake's engine makes use of the IEE standard, which standardises how the long data type in C works, for more info, check out the previously linked article, or [this](https://www.youtube.com/watch?v=p8u_k2LIZyo) beautifully animated video on the matter at hand - it'll explain it much better than I can.

*Unfortunately*, we do not get the luxury of such data types in python easily -- and besides, I wanted to have some fun without introducing some complex methods.

Therefore, after some fiddling around with the calculator, I realised that for relatively small numbers(eg 1-100000), where D is the digit count of the integer, an initial guess G of G = N/2^(D-2) yielded some promising results for an initial guess. However, I quickly realised that with VERY large numbers, this fell off a little. After some consideration, I decided to go for G = N/2^D, as it seemed to be a little better. (logic being, that the smaller numbers would take less iterations of the function to arrive at a somewhat accurate answer) 

*Wait a moment, isn't 2^D rather expensive and making use of the power operator?* - You may ask

Well, yes, but actually no.

You see, binary numbers have this neat little function about them, that allows for division of 2 easily and with virtually no computation cost.

How is this done you might ask?

Well, with the power of bitshifting.

By shifting the bits of a binary number to the left, we half the number, and to the right, we double the number.

Eg.

1111 = 8 + 4 + 2 + 1 = 15

111(a shift to the left) = 7

1010 = 8 + 2 = 10

101 = 4 + 1 = 5


101110 = 46

10111 = 23

Cool huh?

There is rounding with odd numbers, but we're willing to sacrifice this here.

Thus, with the power of log10, we can arrive at a decently good initial guess with

> initguess = x >> (int(math.log10(x)+1))

Note: the >> operator represents a shift to the left in bits and the << to the right

eg. 48 >> 2 would shift the binary form of the integer 48, 2 steps to the left, thereby halving it twice


And that's about it really, specify the iterations and watch it go!

PS: I have not thought of a way to come up with iteration counts for an accurate approximation...



Here's some stats

For the number 4238974, the function arrives at a root of 2058.877372071949 in 7 passes, the actual root being 2058.8768783, just approx 0.05% off the actual answer!

For the same number, the function is also faster than math.sqrt, by almost twice. (timed with timeit)

![image](https://user-images.githubusercontent.com/27218062/156592211-d7fabade-54f4-402b-9507-96b91bb7ec23.png)
Example given above

![image](https://user-images.githubusercontent.com/27218062/156592279-718b7a82-86d1-49a2-8702-ccbc49866b06.png)
timeit speeds of the approximation function(above) vs math.sqrt()(below)


