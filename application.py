import sys
import time
from pymodbus.client.sync import ModbusTcpClient
from modbus_visualizer_gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot

_REGISTER_TYPE_TO_READ_FUNCTION_CODE = {"Coils": 0x01,
                                        "Discrete Inputs": 0x02,
                                        "Input Registers": 0x04,
                                        "Holding Registers": 0x03}


class ModbusWorker(QObject):
    data_available = pyqtSignal(list)
    new_connection_available = pyqtSignal()
    console_message_available = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.client = None
        self.busy = False  # todo: maybe a decorator for this would be nice?

    def isBusy(self):
        return self.busy

    @pyqtSlot(dict)
    def configure_client(self, settings):
        self.busy = True
        if settings["network_type"] is "tcp":
            host = settings["host"]
            port = settings["port"]
            self.client = ModbusTcpClient(host, port)

        elif settings["network_type"] is "rtu":
            ...
        else:
            self.console_message_available.emit("Unknown Network Type")

        connected = self.client.connect()

        if connected:
            self.console_message_available.emit("Connection Successful")
        else:
            self.console_message_available.emit("Connection Failed")

        self.busy = False

    @pyqtSlot(int, int, int, dict)
    def act_on_poll_request(self, function_code, start_register, length, options):
        while self.busy:
            pass  # Wait for client to be configured if it is in the process.

        poll_interval = options.get("interval", 0)
        poll_duration = options.get("duration", 0)
        # poll_sample_count = options.get("sample_count", None)  # TODO: Implement something like this.

        timer = time.time()

        while time.time() - timer <= poll_duration:
            start = time.time()

            data = self.get_modbus_data(function_code, start_register, length)
            self.data_available.emit(data)

            elapsed = time.time() - start
            try:
                time.sleep(poll_interval - elapsed)
            except ValueError:
                time.sleep(poll_interval)

    def get_modbus_data(self, function_code, start_reg, length):
        # TODO: Handle Modbus error codes properly.
        modbus_functions = {0x01: self.client.read_coils,
                            0x02: self.client.read_discrete_inputs,
                            0x04: self.client.read_input_registers,
                            0x03: self.client.read_holding_registers}

        try:
            rr = modbus_functions[function_code](start_reg, length)

        except KeyError:
            self.console_message_available.emit(f"Function code not supported: {function_code}")
            return []
        except Exception as e:  # Todo: Make this a real exception
            print(e)
            return []

        try:
            data = rr.registers
        except AttributeError:
            data = rr.bits[:length]

        return data


class VisualizerApp(Ui_MainWindow, QObject):

    modbus_settings_changed = pyqtSignal(dict)
    polling_settings_available = pyqtSignal(int, int, str)
    poll_request = pyqtSignal(int, int, int, dict)

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)

        self.worker_thread = QThread()
        self.worker = ModbusWorker()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        self.connect_slots()
        self.init_poll_table()
        self.update_poll_table_column_headers()

        self.configure_modbus_client()

    def connect_slots(self):
        self.singlePollPushButton.clicked.connect(self.single_poll)
        self.startRegisterSpinBox.valueChanged.connect(self.update_poll_table_column_headers)

        self.modbus_settings_changed.connect(self.worker.configure_client)
        self.worker.console_message_available.connect(self.write_console)
        self.worker.data_available.connect(self.write_poll_table)
        self.poll_request.connect(self.worker.act_on_poll_request)

    def init_poll_table(self):
        """
        Initialize the table with QTableWidgetItem objects that are empty strings.
        """
        num_rows = self.pollTable.rowCount()
        num_cols = self.pollTable.columnCount()

        for j in range(num_cols):
            for i in range(num_rows):
                self.pollTable.setItem(i, j, QTableWidgetItem(""))

    def update_poll_table_column_headers(self):
        self.clear_poll_table()  # Avoids confusion

        start = self.startRegisterSpinBox.value()
        num_cols = self.pollTable.columnCount()
        num_rows = self.pollTable.rowCount()

        for i in range(num_cols):
            self.pollTable.horizontalHeaderItem(i).setText(str(start + i * num_rows))

    def clear_poll_table(self):
        num_rows = self.pollTable.rowCount()
        num_cols = self.pollTable.columnCount()

        for j in range(num_cols):
            for i in range(num_rows):
                self.pollTable.item(i, j).setText("")

    @pyqtSlot(list)
    def write_poll_table(self, data):
        self.clear_poll_table()
        num_rows = self.pollTable.rowCount()

        cur_col = 0
        for i, datum in enumerate(data):
            self.pollTable.item(i % 10, cur_col).setText(str(datum))
            # self.pollTable.setItem(i % 10, cur_col, QTableWidgetItem(str(datum)))
            if (i + 1) % num_rows == 0:
                cur_col += 1

    def configure_modbus_client(self):
        if not self.worker.isBusy():
            tcp_mode = self.tcpRadioButton.isChecked()
            rtu_mode = self.rtuRadioButton.isChecked()

            settings = {}
            if rtu_mode:
                pass
            elif tcp_mode:
                settings["network_type"] = "tcp"
                settings["host"] = self.tcpHostLineEdit.text()
                settings["port"] = self.tcpPortLineEdit.text()

            self.modbus_settings_changed.emit(settings)
        else:
            self.write_console("Busy...")

    def single_poll(self):
        self.configure_modbus_client()  # Will initiate client update on threaded worker.
        # Todo: Make the configure_modbus_client method fire on client settings change event.

        function_code = _REGISTER_TYPE_TO_READ_FUNCTION_CODE[self.registerTypeComboBox.currentText()]
        options = {}

        self.poll_request.emit(function_code,
                               self.startRegisterSpinBox.value(),
                               self.numberOfRegistersSpinBox.value(),
                               options)

    @pyqtSlot(str)
    def write_console(self, msg, *args, **kwargs):
        self.consoleLineEdit.setText("")
        time.sleep(0.05)  # Seems to be doing nothing now...
        self.consoleLineEdit.setText(msg)

    def exit(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window_obj = QMainWindow()
    window = VisualizerApp(main_window_obj)
    main_window_obj.show()
    sys.exit(app.exec_())
