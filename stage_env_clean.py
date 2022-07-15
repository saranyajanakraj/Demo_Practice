import os
import sys
import psycopg2
from configparser import ConfigParser
def main():
#   input1 =os.environ['Branch']
   input2 =os.environ['ENV']
#   print(input1)
   print(input2)
   if (input2=='PRE-PROD'):
      print('It is PRE-PROD ENVIRONMENT')
      exec(open("stage_db_clean.py").read())
      print('Clean stage completed')
   else:
        exec(open("stage_db_uvt_clean.py").read())
        print('stage_db_uvt_clean completed')
if __name__ == "__main__":
   print('Welcome to Redshift STAGEDB CLEAN')
main()
