# scripts/mock_motorcad.py

import random


class MockMotorCAD:
    def __init__(self):
        self.variables = {
            "StatorDiameter": 100,
            "Torque": 200,
            "Efficiency": 90,
            "Losses": 500
        }

    def LoadFromFile(self, filename):
        print(f"📂 Mock Load: {filename}")

    def SetVariable(self, name, value):
        self.variables[name] = value

    def SolveDesign(self):
        dia = self.variables["StatorDiameter"]
        self.variables["Torque"] = dia * 2 + random.uniform(-5, 5)
        self.variables["Efficiency"] = 85 + (dia - 100) * 0.1 + random.uniform(-0.5, 0.5)
        self.variables["Losses"] = 600 - (dia - 100) * 3 + random.uniform(-10, 10)

    def GetVariable(self, name):
        return self.variables.get(name, None)
