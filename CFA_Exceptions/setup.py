from cx_Freeze import setup, Executable

setup(name = "Exceptions" ,
      version = "0.1" ,
      description = "upload exceptions to google spreadsheets" ,
      executables = [Executable("CFA_Exceptions.py")]
    )
