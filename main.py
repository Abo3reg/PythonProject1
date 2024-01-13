import tkinter as tk
from tkinter import messagebox

class HotelReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation System")

        self.current_page = 0
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.country_city_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.people_var = tk.StringVar()
        self.kids_var = tk.StringVar()

        self.users = self.load_users()
        self.country_city_data = self.load_country_city()

        self.pages = [self.login_page, self.country_city_page, self.date_people_page]

        self.login_page()

    def load_users(self):
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                return dict(line.strip().split(",") for line in lines)
        except FileNotFoundError:
            self.show_error("User file not found.")
            self.root.destroy()

    def load_country_city(self):
        try:
            with open("country_city.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.show_error("Country-City file not found.")
            self.root.destroy()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def check_credentials(self):
        username = self.username.get()
        password = self.password.get()
        if username in self.users and self.users[username] == password:
            self.next_page()
        else:
            self.show_error("Invalid username or password.")

    def next_page(self):
        self.current_page += 1
        if self.current_page < len(self.pages):
            self.pages[self.current_page]()
        else:
            self.current_page = 0
            self.show_info("Reservation confirmed! Payment details will be sent to your email.")
            self.root.destroy()

    def show_info(self, message):
        messagebox.showinfo("Success", message)

    def login_page(self):
        login_frame = tk.Frame(self.root)
        login_frame.pack(padx=20, pady=20)

        tk.Label(login_frame, text="Username:").grid(row=0, column=0)
        tk.Entry(login_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(login_frame, text="Password:").grid(row=1, column=0)
        tk.Entry(login_frame, textvariable=self.password, show="*").grid(row=1, column=1)

        tk.Button(login_frame, text="Login", command=self.check_credentials).grid(row=2, columnspan=2)

    def country_city_page(self):
        country_city_frame = tk.Frame(self.root)
        country_city_frame.pack(padx=20, pady=20)

        tk.Label(country_city_frame, text="Select Country and City:").grid(row=0, column=0)
        tk.OptionMenu(country_city_frame, self.country_city_var, *self.country_city_data).grid(row=0, column=1)

        tk.Button(country_city_frame, text="Next", command=self.next_page).grid(row=1, columnspan=2)

    def date_people_page(self):
        date_people_frame = tk.Frame(self.root)
        date_people_frame.pack(padx=20, pady=20)

        tk.Label(date_people_frame, text="Select Date:").grid(row=0, column=0)
        tk.Entry(date_people_frame, textvariable=self.date_var).grid(row=0, column=1)
        tk.Label(date_people_frame, text="Number of adults:").grid(row=1, column=0)
        tk.Entry(date_people_frame, textvariable=self.people_var).grid(row=1, column=1)
        tk.Label(date_people_frame, text="Number of Kids:").grid(row=2, column=0)
        tk.Entry(date_people_frame, textvariable=self.kids_var).grid(row=2, column=1)

        tk.Button(date_people_frame, text="Next", command=self.next_page).grid(row=3, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = HotelReservationApp(root)
    root.mainloop()