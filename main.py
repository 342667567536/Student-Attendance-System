import customtkinter as ctk
import cv2
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AttendanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Attendance System")
        self.geometry("1000x600")

        # --- Layout Grid ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="ADMIN PANEL", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=30)

        self.btn_start = ctk.CTkButton(self.sidebar, text="Start Camera", command=self.start_camera)
        self.btn_start.pack(padx=20, pady=10)

        self.btn_records = ctk.CTkButton(self.sidebar, text="View Records", fg_color="transparent", border_width=2)
        self.btn_records.pack(padx=20, pady=10)

        # --- Main Video Area ---
        self.video_frame = ctk.CTkFrame(self)
        self.video_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.video_label = ctk.CTkLabel(self.video_frame, text="Click 'Start Camera' to begin")
        self.video_label.pack(expand=True)

        self.cap = None

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Here is where you would insert the face recognition logic from the previous step
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            
            self.video_label.configure(image=img_tk, text="")
            self.video_label.image = img_tk
            
        self.after(10, self.update_frame)

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()
