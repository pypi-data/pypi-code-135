import math
import statistics


class maths():
        @staticmethod
        def ExternalPromptMath():
            print("syntax: num operator num")
            print("+ is Addition, - is substration, * is Multiplication / is division")
            while True:
                try:
                    print(eval(input("Enter Question> ")))

                except ValueError:
                    print("Error, incorrect value given! Please enter a correct value")
        
        # Allowing the developer to perform calculations behind the scenes
        @staticmethod
        def add(num1, num2):
            print(num1 + num2)
            
        @staticmethod
        def subtract(num1, num2):
            print(num1 - num2)

        @staticmethod
        def multiply(num1, num2):
            print(num1 * num2)

        @staticmethod
        def divide(num1, num2):
            print(num1 / num2)
        

        @staticmethod
        def GetMean(MeanVal):
            print(statistics.mean(MeanVal))
        
        @staticmethod
        def GetMedian(MedianVal):
            print(statistics.median(MedianVal))
        
        @staticmethod
        def GetMode(ModeVal):
            print(statistics.mode(ModeVal))
