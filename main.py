import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# def save_options():
#     selected_resources = [resource for resource, var in resource_vars.items() if var.get()]
#     selected_action = action_var.get()
#     email = email_entry.get()
#     frequency = frequency_entry.get()

#     if not email:
#         messagebox.showerror("Error", "Please enter an email address.")
#         return

#     # Display or save options
#     messagebox.showinfo("Success", "Options saved successfully.")
#     root.destroy()

def save_options():
    selected_resources = [resource for resource, var in resource_vars.items() if var.get()]
    selected_action = action_var.get()
    email = email_entry.get()
    frequency = frequency_entry.get()

    if not email:
        messagebox.showerror("Error", "Please enter an email address.")
        return

    # Save options to constants.py
    with open('constants.py', 'w') as f:
        f.write(f"resource_list = {selected_resources}\n")
        f.write(f"action = '{selected_action}'\n")
        f.write(f"email = '{email}'\n")
        f.write(f"frequency = '{frequency}'\n")

    messagebox.showinfo("Success", "Options saved successfully.")
    root.destroy()



root = tk.Tk()
root.title("AWS Cost Optimizer")
root.geometry("500x700")
root.configure(bg="#CBC3E3")

# Main Title
title = tk.Label(root, text="AWS Cost Optimizer", font=("Helvetica", 20, "bold"), bg="#CBC3E3", fg="black")
title.pack(pady=10)

# Resources Section
resources_frame = tk.Frame(root, bg="#CBC3E3")
resources_frame.pack(pady=20, fill='x', padx=20)

heading_2 = tk.Label(resources_frame, text="Select the Services to Optimize:", font=("Helvetica", 14), bg="#CBC3E3", fg="black")
heading_2.pack(anchor="w")

resource_vars = {}
resources = ["EC2", "EBS", "DynamoDB","RDS"]
for resource in resources:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(resources_frame, text=resource, variable=var, font=("Helvetica", 12), bg="#CBC3E3", fg="black", selectcolor="#CBC3E3")
    checkbox.pack(anchor='w', padx=20)
    resource_vars[resource] = var

# Action Section
action_frame = tk.Frame(root, bg="#CBC3E3")
action_frame.pack(pady=20, fill='x', padx=20)

action_label = tk.Label(action_frame, text="What kind of action you prefer:", font=("Helvetica", 14), bg="#CBC3E3", fg="black")
action_label.pack(anchor="w")

action_var = tk.StringVar(value="stop and notify")
stop_and_notify_radio = tk.Radiobutton(action_frame, text="Stop the Service", variable=action_var, value="stop and notify", font=("Helvetica", 12), bg="#CBC3E3", fg="black", selectcolor="#CBC3E3")
stop_and_notify_radio.pack(anchor='w', padx=20)

notify_radio = tk.Radiobutton(action_frame, text="Notify via Mail", variable=action_var, value="notify", font=("Helvetica", 12), bg="#CBC3E3", fg="black", selectcolor="#CBC3E3")
notify_radio.pack(anchor='w', padx=20)

# Email Input Section
email_frame = tk.Frame(root, bg="#CBC3E3")
email_frame.pack(pady=20, fill='x', padx=20)

email_label = tk.Label(email_frame, text="E-Mail Address you want to get the Alerts:", font=("Helvetica", 14), bg="#CBC3E3", fg="black")
email_label.pack(anchor="w")

email_entry = tk.Entry(email_frame, width=30, font=("Helvetica", 12))
email_entry.pack(pady=5, padx=20)

# # Frequency Input Section
# frequency_frame = tk.Frame(root, bg="#CBC3E3")
# frequency_frame.pack(pady=20, fill='x', padx=20)

# frequency_label = tk.Label(frequency_frame, text="How frequently you want to perform the scan:", font=("Helvetica", 14), bg="#CBC3E3", fg="black")
# frequency_label.pack(anchor="w")

# frequency_entry = tk.Entry(frequency_frame, width=10, font=("Helvetica", 12))
# frequency_entry.pack(pady=5, padx=20)
# frequency_unit = tk.Label(frequency_frame, text="No. of Hours", font=("Helvetica", 12), bg="#CBC3E3", fg="gray")
# frequency_unit.pack(anchor="w", padx=20)

# Frequency Input Section
frequency_frame = tk.Frame(root, bg="#CBC3E3")
frequency_frame.pack(pady=20, fill='x', padx=20)

frequency_label = tk.Label(frequency_frame, text="How frequently you want to perform the scan:", font=("Helvetica", 14), bg="#CBC3E3", fg="black")
frequency_label.pack(anchor="w")

# Frame for input and unit label
frequency_input_frame = tk.Frame(frequency_frame, bg="#CBC3E3")
frequency_input_frame.pack(anchor="w", padx=20, pady=5)



frequency_unit = tk.Label(frequency_input_frame, text="No. of Hours", font=("Helvetica", 12,"bold"), bg="#CBC3E3", fg="gray",)
frequency_unit.grid(row=0, column=0)

frequency_entry = tk.Entry(frequency_input_frame, width=10, font=("Helvetica", 12))
frequency_entry.grid(row=0, column=1, padx=(0, 5))  # Add some padding to the right

# Save Button
save_button = tk.Button(root, text="Save Options", command=save_options, bg="#C3B1E1", fg="black", font=("Helvetica", 14, "bold"), activebackground="white")
save_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
