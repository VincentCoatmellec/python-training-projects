from PySide6 import QtWidgets, QtCore

from movie import Movie, get_movies


class App(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.main_layout = None
		self.le_movie_title = None
		self.btn_add_movie = None
		self.lw_movies = None
		self.btn_remove_movie = None

		self.setWindowTitle("Movie Club")
		self.init_ui()
		self.resize(400, 700)
		self.populate_movies()
		self.setup_connections()

	def init_ui(self):
		""" Initialize the user interface with a vertical layout
		"""
		self.main_layout = QtWidgets.QVBoxLayout(self)
		self.le_movie_title = QtWidgets.QLineEdit(self)
		self.btn_add_movie = QtWidgets.QPushButton("Add Movie", self)
		self.lw_movies = QtWidgets.QListWidget(self)
		self.lw_movies.setSelectionMode(
			QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
		self.btn_remove_movie = QtWidgets.QPushButton("Remove Movie", self)
		self.main_layout.addWidget(self.le_movie_title)
		self.main_layout.addWidget(self.btn_add_movie)
		self.main_layout.addWidget(self.lw_movies)
		self.main_layout.addWidget(self.btn_remove_movie)

	def populate_movies(self):
		""" Populate the list widget with movies from the data source
		"""
		movies = get_movies()

		for movie in movies:
			lw_item = QtWidgets.QListWidgetItem(movie.title)
			# Store the movie object in the item
			lw_item.setData(QtCore.Qt.ItemDataRole.UserRole, movie)
			self.lw_movies.addItem(lw_item)

	def setup_connections(self):
		""" Set up signal-slot connections for buttons
		"""
		self.btn_add_movie.clicked.connect(self.add_movie)
		self.btn_remove_movie.clicked.connect(self.remove_movie)
		self.le_movie_title.returnPressed.connect(self.add_movie)

	def add_movie(self):
		""" Add a new movie to the list and data source
		"""
		title = self.le_movie_title.text().strip()
		if title:
			movie = Movie(title=title)
			if movie.add_to_movies():
				lw_item = QtWidgets.QListWidgetItem(movie.title)
				lw_item.setData(QtCore.Qt.ItemDataRole.UserRole, movie)
				self.lw_movies.addItem(lw_item)
				self.le_movie_title.clear()
			else:
				QtWidgets.QMessageBox.warning(
					self, "Duplicate Movie", f"{movie.title} is already in the list.")
		else:
			QtWidgets.QMessageBox.warning(
				self, "Input Error", "Please enter a movie title.")

	def remove_movie(self):
		""" Remove selected movies from the list and data source
		"""
		selected_items = self.lw_movies.selectedItems()
		if selected_items:
			for item in selected_items:
				movie = item.data(QtCore.Qt.ItemDataRole.UserRole)
				if movie.remove_from_movies():
					self.lw_movies.takeItem(self.lw_movies.row(item))
				else:
					QtWidgets.QMessageBox.warning(
						self, "Error", f"Could not remove {movie.title}.")
		else:
			QtWidgets.QMessageBox.warning(
				self, "Selection Error", "Please select a movie to remove.")


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = App()
	window.show()
	app.exec()
