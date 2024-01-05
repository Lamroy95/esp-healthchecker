from machine import SoftI2C

from healthchecker.lib.lum import Bh1750, I2cAdapter


class LumAdapter:
    def __init__(self, i2c: SoftI2C, device_addr: int, measure_delay_ms: int):
        self.measure_delay_ms = measure_delay_ms
        self.sol = Bh1750(I2cAdapter(i2c), address=device_addr)

    def start(self):
        self.sol.power(True)
        self.sol.set_mode(continuously=False, high_resolution=True)

    def stop(self):
        self.sol.power(False)

    def __enter__(self) -> "LumAdapter":
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()

    def read_value(self) -> float:
        return self.sol.get_illumination()
