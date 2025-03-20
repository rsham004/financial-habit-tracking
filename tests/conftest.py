import os
import sys

# project_root = "C:\NotBackedUp\codebasics\myproject-expense-tracking"
project_root = os.path.join(os.path.dirname(__file__),'..')
print("***File***   ", project_root)
sys.path.insert(0, project_root)
print("****SYS PATH****", sys.path)
