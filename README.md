# 2-2

Prompt was to use the same Intcode rules and input string to determine which two numbers when placed in positions 1 and 2 of the string would result in a target number being placed in position 0 by the evaluation of the code.

Had a rough time debugging this one, because occasionally values would break the intcomp function by attempting to write outside of the array. This was solved by adding a try-catch block that just continued with the loop when encountering an IndexError, but figuring out why that was happening took a lot of headaches. I also was less diligent about makinig my commits bite-sized when working on this problem, so the commits are a bit larger than I usually prefer.