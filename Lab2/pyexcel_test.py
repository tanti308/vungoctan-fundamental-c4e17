import pyexcel

data = [
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Huyen",
        "Age": 23
    },
    {
        "Name": "Huyen",
        "Age": 23
    }
]
pyexcel.save_as(records=data,dest_file_name="test.xlsx")
