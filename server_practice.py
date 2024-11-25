import tkinter as tk

# Create the main window
server_root = tk.Tk()
server_root.title("Server Code Window")
server_root.geometry("400x300")  # Set window size: width x height

# Add a label to the window
label = tk.Label(server_root, text="Server Code", font=("Arial", 16))
label.pack(pady=20)

# Add a button to close the window
close_button = tk.Button(server_root, text="Close", command=server_root.destroy)
close_button.pack(pady=10)

# Run the application
server_root.mainloop()
