from time import time
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

from enum import Enum
import math
import pickle

from vec2d import Vec2D

class CtrlState(Enum):
	DRAW = 1
	ERASE = 2
	START_POINT = 3

class GridFrame(QtWidgets.QFrame):
	BOX_SIZE = 30

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.grid_pos = Vec2D(0, 0)
		self.drag_pos = Vec2D(0, 0)

		self.grid_data = set()
		self.start_point = None

		self.ctrl_state = CtrlState.DRAW

		self.zoom = 1.0

	def testLoad(self):
		self.loadData("test.path")

	def loadData(self, file_name):
		with open(file_name, "rb") as f:
			self.grid_pos = pickle.load(f)
			self.drag_pos = pickle.load(f)
			self.grid_data = pickle.load(f)
			self.start_point = pickle.load(f)
			self.ctrl_state = pickle.load(f)

		self.update()

	def saveData(self):
		with open("test.path", "wb") as f:
			pickle.dump(self.grid_pos, f)
			pickle.dump(self.drag_pos, f)
			pickle.dump(self.grid_data, f)
			pickle.dump(self.start_point, f)
			pickle.dump(self.ctrl_state, f)

	def getGraphUtil(self, cur, nodes, adj, visited):
		if cur in visited:
			return

		visited.add(cur)

		adj[cur] = []

		next = cur + Vec2D(1, 0)
		if next in nodes:
			adj[cur].append(next)
			self.getGraphUtil(next, nodes, adj, visited)

		next = cur + Vec2D(0, 1)
		if next in nodes:
			adj[cur].append(next)
			self.getGraphUtil(next, nodes, adj, visited)

		next = cur + Vec2D(-1, 0)
		if next in nodes:
			adj[cur].append(next)
			self.getGraphUtil(next, nodes, adj, visited)

		next = cur + Vec2D(0, -1)
		if next in nodes:
			adj[cur].append(next)
			self.getGraphUtil(next, nodes, adj, visited)

	def getGraph(self):
		adj = {}

		nodes = self.grid_data.copy()
		nodes.add(self.start_point)

		visited = set()

		self.getGraphUtil(self.start_point, nodes, adj, visited)

		nodes = set()

		for node in adj.keys():
			nodes.add(node)

		return(nodes, adj)

	def getStartPoint(self):
		Vec2D(self.start_point.getX(), self.start_point.getY())

	def setStateDraw(self):
		self.ctrl_state = CtrlState.DRAW

	def setStateErase(self):
		self.ctrl_state = CtrlState.ERASE

	def setStateStartPoint(self):
		self.ctrl_state = CtrlState.START_POINT

	def clearGrid(self):
		self.grid_data = set()
		self.start_point = None
		self.update()

	def screenToGrid(self, x, y):
		px = (x - self.grid_pos.getX()) // self.BOX_SIZE
		py = (y - self.grid_pos.getY()) // self.BOX_SIZE

		return Vec2D(px, py)

	def gridToScreen(self, p):
		x = p.getX() * self.BOX_SIZE + self.grid_pos.getX()
		y = p.getY() * self.BOX_SIZE + self.grid_pos.getY()

		return (x, y)

	#this method is trash and needs to be rewritten
	def paintEvent(self, e):
		painter = QtGui.QPainter(self)

		w = self.frameGeometry().width()
		h = self.frameGeometry().height()

		#draw the grid
		for y in range(-1, h // self.BOX_SIZE + 1):
			for x in range(-1, w // self.BOX_SIZE + 1):
				px = x * self.BOX_SIZE + (self.grid_pos.getX() % self.BOX_SIZE)
				py = y * self.BOX_SIZE + (self.grid_pos.getY() % self.BOX_SIZE)

				painter.setPen(QtGui.QPen(Qt.black, 1, Qt.SolidLine))
				painter.setBrush(QtGui.QBrush(Qt.white, Qt.SolidPattern))
				painter.drawRect(px, py, self.BOX_SIZE, self.BOX_SIZE)

		#draw the points
		pmin = self.screenToGrid(0, 0)
		pmax = self.screenToGrid(w, h)

		for p in self.grid_data:
			if p.isInBounds(pmin, pmax):
				screen_coords = self.gridToScreen(p)

				painter.setPen(QtGui.QPen(Qt.black, 1, Qt.SolidLine))
				painter.setBrush(QtGui.QBrush(Qt.green, Qt.SolidPattern))
				painter.drawRect(screen_coords[0], screen_coords[1], self.BOX_SIZE, self.BOX_SIZE)

		if self.start_point is not None and self.start_point.isInBounds(pmin, pmax):
			screen_coords = self.gridToScreen(self.start_point)

			painter.setPen(QtGui.QPen(Qt.black, 1, Qt.SolidLine))
			painter.setBrush(QtGui.QBrush(Qt.blue, Qt.SolidPattern))
			painter.drawRect(screen_coords[0], screen_coords[1], self.BOX_SIZE, self.BOX_SIZE)

			painter.drawLine(screen_coords[0], screen_coords[1], screen_coords[0] + self.BOX_SIZE, screen_coords[1] + self.BOX_SIZE)
			painter.drawLine(screen_coords[0] + self.BOX_SIZE, screen_coords[1], screen_coords[0], screen_coords[1] + self.BOX_SIZE)

	def leftMouseButtonEvent(self, e):
		p = self.screenToGrid(e.x(), e.y())

		if self.ctrl_state == CtrlState.DRAW:
			self.grid_data.add(p)

		elif self.ctrl_state == CtrlState.ERASE:
			if p in self.grid_data:
				self.grid_data.remove(p)
			
			if self.start_point is not None and p == self.start_point:
				self.start_point = None

		elif self.ctrl_state == CtrlState.START_POINT:
			self.start_point = p

		self.update()

	def mouseMoveEvent(self, e):
		if e.buttons() & Qt.RightButton:
			cur = Vec2D(e.x(), e.y())

			self.grid_pos = self.grid_pos + (cur - self.drag_pos)
			self.drag_pos = cur

			self.update()

		if e.buttons() & Qt.LeftButton:
			w = self.frameGeometry().width()
			h = self.frameGeometry().height()

			if Vec2D(e.x(), e.y()).isInBounds(Vec2D(0, 0), Vec2D(w, h)):
				self.leftMouseButtonEvent(e)

	def mousePressEvent(self, e):
		if e.button() == Qt.RightButton:
			self.drag_pos = Vec2D(e.x(), e.y())

		if e.buttons() & Qt.LeftButton:
			self.leftMouseButtonEvent(e)

	def wheelEvent(self, e):
		self.zoom = self.zoom * math.pow(0.95, e.angleDelta().y()/120)