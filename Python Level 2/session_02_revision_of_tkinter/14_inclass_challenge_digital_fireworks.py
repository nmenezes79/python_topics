import tkinter as tk
import random

class FireworksApp:
	def __init__(self, master):
		self.master = master
		self.master.title("Fireworks Display")

		self.canvas = tk.Canvas(self.master, width=800, height=600, bg="black")
		self.canvas.pack(fill=tk.BOTH, expand=True)

		self.canvas.bind("<Button-1>", self.launch_firework)

	def launch_firework(self, event):
		colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
		for _ in range(random.randint(50, 100)):
			x = event.x + random.randint(-20, 20)
			y = event.y + random.randint(-20, 20)
			size = random.randint(2, 6)
			color = random.choice(colors)
			self.canvas.create_oval(x, y, x + size, y + size, fill=color)

# 🔥 main() should be outside the class
def main():
		root = tk.Tk()
		app = FireworksApp(root)
		root.mainloop()

if __name__ == "__main__":
		main()