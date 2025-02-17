import numpy as np
from rich.table import Table
from rich.console import Console
console = Console()
def CreateMatrix():
    matrix = np.random.randint(10, size=(3, 3))
    print("Matrix:\n", matrix)
    Mat = matrix
    # print(Mat)
        # Matrix rows numbers
    Mat_R1_C1 = Mat[0,0]
    Mat_R1_C2 = Mat[0,1]
    Mat_R1_C3 = Mat[0,2]
    

    Mat_R2_C1 = Mat[1,0]
    Mat_R2_C2 = Mat[1,1]
    Mat_R2_C3 = Mat[1,2]

    Mat_R3_C1 = Mat[2,0]
    Mat_R3_C2 = Mat[2,1]
    Mat_R3_C3 = Mat[2,2]


    #convert matrix to string
    Mat_R1_C1_Str = str(Mat_R1_C1)
    Mat_R1_C2_Str = str(Mat_R1_C2)
    Mat_R1_C3_Str = str(Mat_R1_C3)

    Mat_R2_C1_Str = str(Mat_R2_C1)
    Mat_R2_C2_Str = str(Mat_R2_C2)
    Mat_R2_C3_Str = str(Mat_R2_C3)

    Mat_R3_C1_Str = str(Mat_R3_C1)
    Mat_R3_C2_Str = str(Mat_R3_C2)
    Mat_R3_C3_Str = str(Mat_R3_C3)

    # MatStr = str(MatR)
    table = Table(title="Matrix Table")


    table.add_row(Mat_R1_C1_Str, Mat_R1_C2_Str, Mat_R1_C3_Str)
    table.add_row(Mat_R2_C1_Str, Mat_R2_C2_Str, Mat_R2_C3_Str)
    table.add_row(Mat_R3_C1_Str, Mat_R3_C2_Str, Mat_R3_C3_Str)

    console.print(table)
CreateMatrix()



    









