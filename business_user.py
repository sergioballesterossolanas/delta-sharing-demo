import tkinter as tk
from tkinter import messagebox
import delta_sharing
import pandas

# Delta sharing
share_file_path = 'data/config.share'
client = delta_sharing.SharingClient(share_file_path)
shares = client.list_shares()



share = shares[0]
schema = client.list_schemas(share)[0] 
tables = client.list_tables(schema)

options = [table.name for table in tables]

# Function to be called when the button is clicked
def button_click():
    selected_option = drop_var.get()

    # Download the last table and save it as CSV
    table_url = f"{share_file_path}#{share.name}.{schema.name}.{selected_option}"
    print(table_url)
    # Use delta sharing client to load data
    pandas_df = delta_sharing.load_as_pandas(table_url)
    download_name = f"downloads/{share.name}-{schema.name}-{selected_option}.csv"
    pandas_df.to_csv(download_name)
    messagebox.showinfo("Download finished!", f"You have donwloaded: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Databricks Download files")

# Set the size of the window
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create a dropdown
drop_var = tk.StringVar(root)
drop_var.set(options[0])  # default value
dropdown = tk.OptionMenu(root, drop_var, *options)
dropdown.pack(pady=10)

# Create a button
button = tk.Button(root, text="Download", command=button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
