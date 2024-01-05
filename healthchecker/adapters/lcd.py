from enum import Enum
from healthchecker.lib.lcd import LCD
from machine import SoftI2C


class AlignModifier(Enum):
    LEFT = "<"
    CENTER = "^"
    RIGHT = ">"


class LCDAdapter:
    def __init__(self, i2c: SoftI2C, device_addr: int, cols: int, rows: int) -> None:
        self._i2c = i2c
        self.cols, self.rows = cols, rows
        self.device_addr = device_addr
        self._lcd = None
        self._current_text = [""] * rows

    @property
    def _lcd(self) -> LCD:
        if self._lcd is None:
            raise RuntimeError(
                "LCD service is not started. Call LCDAdapter.start() or use context manager"
            )
        return self._lcd

    @_lcd.setter
    def _lcd(self, value: LCD):
        self._lcd = value

    def start(self):
        self._lcd = LCD(
            i2c_addr=self.device_addr,
            num_columns=self.cols,
            num_lines=self.rows,
            i2c=self._i2c,
        )
        self._lcd.display_on()

    def stop(self):
        self._lcd.clear()
        self._lcd.display_off()

    def __enter__(self) -> "LCDAdapter":
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()

    def _get_row(self, row_index: int) -> str:
        if row_index > self.rows - 1:
            raise ValueError(
                f"Can't get row {row_index}. Available rows: {list(range(self.rows))}"
            )
        return self._current_text[row_index]

    def _set_row(self, text: str, row_index: int):
        if len(text) > self.cols:
            raise ValueError(f"Line too long. Max chars: {self.cols}")
        if row_index > self.rows - 1:
            raise ValueError(
                f"Can't write to this row. Available rows: {list(range(self.rows))}"
            )

        self._current_text[row_index] = text

    def backlight_on(self):
        self._lcd.backlight_on()

    def backlight_off(self):
        self._lcd.backlight_off()

    def print_row(self, text: str, row_index: int):
        self._set_row(text, row_index)
        self._lcd.move_to(0, row_index)
        self._lcd.putstr(text)

    def rotate_row_right(self, row_index: int):
        current_row_text = self._get_row(row_index)
        rotated_text = current_row_text[-1] + current_row_text[:-1]
        self.print_row(rotated_text, row_index)

    def register_chars(self, char_maps: list[str]):
        for i, char_map in enumerate(char_maps):
            self._lcd.custom_char(i, char_map)

    def align_row(self, position: AlignModifier, row_index: int):
        stripped_text = self._get_row(row_index).strip()
        aligned_text = f"{stripped_text:{position.value}{self.cols}}"
        self.print_row(aligned_text, row_index)
