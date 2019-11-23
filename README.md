# Steganographic Fractals
The objective is to embedd a secure message into tree fractals.  
The secure message is in binary form "010100011000" and the carrier image is an image created with tree fractals algorithm  
the idea is to descritize angles and branch lengthes to go with the values of the secure message. For example obtuse angle can represent 1   
and acute angle represents 0. Each branch in the tree has two sub-branches, if the left branch is smaller than right branch this represents 0 otherwise it represents 1   
The figure contains an illustration of the scheme  
![attractor](https://github.com/mohandesosama/steganofractals/blob/master/figures/fractal_attractor.png)

## Steganogrpahic Fractal Paper
To cite our work use   
_Hosam, O. (2018, December). Hiding Bitcoins in Steganographic Fractals. In 2018 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT) (pp. 512-519). IEEE._  
Download PDF version of the paper at https://www.researchgate.net/profile/Osama_Hosam2/publication/331204356_Hiding_Bitcoins_in_Steganographic_Fractals/links/5c727639a6fdcc47159670d0/Hiding-Bitcoins-in-Steganographic-Fractals.pdf

## Instructions
•	Learn openGL with python  
https://code.visualstudio.com/docs/python/python-tutorial   
•	Make sure to download freeglut.dll (freeglut 3.0.0 MSVC Package) from https://www.transmissionzero.co.uk/software/freeglut-devel/  
go to /bin folder and use x64 version in 64 bit operating system and 64 based processor
https://noobtuts.com/python/opengl-introduction  
•	Make sure of using this sentence , pass bytes instead of string  
```python
window = glutCreateWindow(b"I like this")  
```
## References
Markdown cheatsheet https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
