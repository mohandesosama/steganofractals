# Steganographic Fractals
The objective is to embedd a secure message into tree fractals.  
The secure message is in binary form "010100011000" and the carrier image is an image created with tree fractals algorithm  
the idea is to descritize angles and branch lengthes to go with the values of the secure message. For example obtuse angle can represent 1   
and acute angle represents 0. Each branch in the tree has two sub-branches, if the left branch is smaller than right branch this represents 0 otherwise it represents 1   
  
The figure contains an illustration of the scheme  
![attractor](https://github.com/mohandesosama/steganofractals/blob/master/figures/fractal_attractor.png)  
  
first, the secure message is created randomly with the following line of code 
```python
self.data=[randint(0,1) for b in range(1,self.bits_capacity+1)]
```
to build up the tree, the most important function is "calc_vertices" which creates the full list of vertices of the fractal tree  
```python
 def calc_vertices(self,point,source_direction,lth,depth,b_angle):
 ```
 it takes the b_angle (the beginning angle) and the level of the tree "depth" and the startup length of the branches "lth" and the source direction "source_direction" which is the direction of the root branch. the output of the function is the list of the created tree. OpenGL will take this list and draw it on the screen. 
the following part of the code 
```python
 #left branch
  left_branch_direction=self.norma(self.get_rotated_vec(source_direction,b_angle))
  leftb_center_point=point + lth*left_branch_direction
  leftb_Larm_direction=self.get_rotated_vec(left_branch_direction,b_angle*self.angle_reduction_ratio)
  self.branch_vertices.append([point,leftb_center_point])
  leftb_Larm_point=leftb_center_point + leftb_Larm_lth*leftb_Larm_direction
  self.branch_vertices.append([leftb_center_point,leftb_Larm_point])
  leftb_Rarm_direction=self.get_rotated_vec(left_branch_direction,-b_angle*self.angle_reduction_ratio)
  leftb_Rarm_point=leftb_center_point +leftb_Rarm_lth*leftb_Rarm_direction
  self.branch_vertices.append([leftb_center_point,leftb_Rarm_point])
```
the vertices of  
..* center of the left branch, leftb_center_point
..* vertex of end of left sub branch(arm),leftb_Larm_point
..* vertex of end of right sub branch(arm),leftb_Rarm_point  
Notice that they are changed according to the b_angle
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
