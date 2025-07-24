import tkinter as tk
from app.views.login_view import LoginView
from app.views.menu_view import MenuView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x150")
        self.resizable(False, False)
        self._frame = None
        self.mostrar_login()

    def mostrar_login(self):
        self.mudar_frame(LoginView, on_login_success=self.mostrar_menu)

    def mostrar_menu(self):
        self.geometry("300x300")
        self.mudar_frame(MenuView)

    def mudar_frame(self, FrameClass, **kwargs):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = FrameClass(self, **kwargs)
        self._frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
