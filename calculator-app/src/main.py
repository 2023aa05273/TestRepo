# main.py

from ui.interface import CalculatorUI

def main():
    app = CalculatorUI()
    app.create_window()
    app.run()

if __name__ == "__main__":
    main()