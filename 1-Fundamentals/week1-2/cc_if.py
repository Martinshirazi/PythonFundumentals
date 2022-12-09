"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
gradetotest = 0
if gradetotest == 100:
    print("A+")
elif gradetotest >= 90:
    print("A")
elif gradetotest >= 80:
    print("B")
elif gradetotest >= 70:
    print("C")
elif gradetotest >= 50:
    print("D")
else:
    print("F")