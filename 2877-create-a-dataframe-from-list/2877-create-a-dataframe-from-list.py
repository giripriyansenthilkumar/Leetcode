import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    c=["student_id","age"]
    df=pd.DataFrame(student_data,columns=c)
    return df