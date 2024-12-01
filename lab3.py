import tkinter as tk
import random
import string

def generate_key():
    first_letter = random.choice(string.ascii_uppercase)
    second_letter = random.choice(string.ascii_uppercase)

    first_index = ord(first_letter) - ord('A') + 1
    second_index = ord(second_letter) - ord('A') + 1

    lower_bound = min(first_index, second_index)
    upper_bound = max(first_index, second_index)

    letters = ''.join(random.choices(string.ascii_uppercase[lower_bound-1:upper_bound], k=7))

    key = f"{lower_bound:02d} {letters} {upper_bound:02d}"
    key_entry.delete(0, tk.END)  
    key_entry.insert(0, key)  


root = tk.Tk()
root.title("Key Generator")
root.geometry("843x403")

background_image = tk.PhotoImage(file="homescapes.png")  
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

key_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
key_entry.pack(pady=20)

generate_button = tk.Button(root, text="Generate Key", command=generate_key, font=("Helvetica", 14))
generate_button.pack(pady=10)

root.mainloop()