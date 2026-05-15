from PySide6 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("FX CONVERTER")
        self.setup_ui()
        self.resize(750, 100)
        self.setup_default_values()
        self.setup_connections()
        self.setup_css()

    def setup_ui(self):
        """Set up the user interface."""
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.cbb_curncyFrom = QtWidgets.QComboBox()
        self.spn_Amount = QtWidgets.QSpinBox()
        self.cbb_curncyTo = QtWidgets.QComboBox()
        self.spn_ConvertedAmount = QtWidgets.QSpinBox()
        self.btn_Inverser = QtWidgets.QPushButton("Inverse Currencies")

        self.main_layout.addWidget(self.cbb_curncyFrom)
        self.main_layout.addWidget(self.spn_Amount)
        self.main_layout.addWidget(self.cbb_curncyTo)
        self.main_layout.addWidget(self.spn_ConvertedAmount)
        self.main_layout.addWidget(self.btn_Inverser)

    def setup_default_values(self):
        """Set up the default values for the widgets."""
        currencies = self.c.currencies or []
        self.cbb_curncyFrom.addItems(sorted(list(currencies)))
        self.cbb_curncyTo.addItems(sorted(list(currencies)))
        self.cbb_curncyFrom.setCurrentText("EUR")
        self.cbb_curncyTo.setCurrentText("EUR")

        self.spn_Amount.setRange(1, 1000000)
        self.spn_ConvertedAmount.setRange(1, 1000000)

        self.spn_Amount.setValue(100)
        self.spn_ConvertedAmount.setValue(100)

    def setup_css(self):
        """Set up the CSS for the application."""
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: None;
        """)

    def setup_connections(self):
        """Set up the connections for the widgets."""
        self.cbb_curncyFrom.activated.connect(self.compute)
        self.cbb_curncyTo.activated.connect(self.compute)
        self.spn_Amount.valueChanged.connect(self.compute)
        self.btn_Inverser.clicked.connect(self.inversing_currencies)

    def compute(self):
        """Compute the converted amount."""
        amount = self.spn_Amount.value()
        from_currency = self.cbb_curncyFrom.currentText()
        to_currency = self.cbb_curncyTo.currentText()

        try:
            result = self.c.convert(amount, from_currency, to_currency)
        except currency_converter.currency_converter.RateNotFoundError:
            print("The conversion is not working!")
        else:
            self.spn_ConvertedAmount.setValue(int(result))

    def inversing_currencies(self):
        """Inverse the selected currencies."""
        from_currency = self.cbb_curncyFrom.currentText()
        to_currency = self.cbb_curncyTo.currentText()

        self.cbb_curncyFrom.setCurrentText(to_currency)
        self.cbb_curncyTo.setCurrentText(from_currency)

        self.compute()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec()
