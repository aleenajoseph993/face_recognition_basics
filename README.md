# face_recognition_basics
Sample python programs to recognize the faces using openCV in google colab and vscode editor.
The given program is face recognition problem that :

* Helps crop the face portion from the given input image.(Refer:p1.py)
* Identifies the face portion and highlight it with a geometrical rectangle.(Refer: p2.py)
Note: The program p3.py does both the functions described above in a single program in Google colab.

cv2.imshow() is disabled in Colab, because it causes Jupyter sessions to crash; see https://github.com/jupyter/notebook/issues/3935. 
As a substitution, consider using: 
from google.colab.patches import cv2_imshow
