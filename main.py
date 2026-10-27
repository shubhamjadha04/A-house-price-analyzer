import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt




class HousepriceAnalyser:

    def __init__(self, file_path):

        self.file_path = file_path
        self.df = None
        

    def load_data(self):
        try:

            self.df = pd.read_csv(self.file_path)
            print(self.df.head())
            print(f"The shape of the dataset is {self.df.shape}")

        except FileNotFoundError:
            print("The file is not found.")

        except Exception as e:
            print("something is wrong",e)


    def explore_data(self):

        if self.df is None:
            print("The dataset is not loaded")
            return

        print(f"There are {self.df.shape[0]} rows in the dataset.")
        print(f"There are {self.df.shape[1]} column in the dataset.")
        print("All the column information is as follows:")
        self.df.info()

    def check_missing_values(self):
        print(self.df.isnull().sum())













analyse = HousepriceAnalyser(r"C:\Users\shubham jadhao\OneDrive\Desktop\project\Bengaluru_House_Data.csv")

analyse.load_data()
# analyse.explore_data()
analyse.check_missing_values()



        