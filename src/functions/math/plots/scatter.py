from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class Scatter(QWidget):
    def __init__(self, x_arr, y_arr, x_label='X', y_label='Y', title='Scatter Plot', show_regression=True):
        super().__init__()
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.show_regression = show_regression

        self.figure = Figure(figsize=(3, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(400, 300)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ax = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        self.canvas.mpl_connect('scroll_event', self._on_scroll)
        self.setLayout(layout)
        self._plot()

    def _plot(self):
        self.ax.clear()
        self.ax.scatter(self.x_arr, self.y_arr, color='blue', label='Data points')
        if self.show_regression:
            slope, intercept = np.polyfit(self.x_arr, self.y_arr, 1)
            y_fit = [slope * x + intercept for x in self.x_arr]
            self.ax.plot(self.x_arr, y_fit, color='red', label='Regression line')
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.set_title(self.title)
        self.ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='gray')
        self.ax.legend()
        self.canvas.draw()

    def _on_scroll(self, event):
        base_scale = 1.1
        ax = self.ax
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        xdata = event.xdata
        ydata = event.ydata
        if xdata is None or ydata is None:
            return

        if event.button == 'up':
            scale_factor = 1/base_scale
        elif event.button == 'down':
            scale_factor = base_scale
        else:
            scale_factor = 1
        
        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

        ax.set_xlim([xdata - new_width*(xdata-cur_xlim[0])/(cur_xlim[1]-cur_xlim[0]), xdata + new_width*(cur_xlim[1]-xdata)/(cur_xlim[1]-cur_xlim[0])])
        ax.set_ylim([ydata - new_height*(ydata-cur_ylim[0])/(cur_ylim[1]-cur_ylim[0]), ydata + new_height*(cur_ylim[1]-ydata)/(cur_ylim[1]-cur_ylim[0])])
        self.canvas.draw()