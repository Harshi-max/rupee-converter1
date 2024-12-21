import tkinter as tk

def dollar_to_rupee():
    dollars = entry_dollars.get()
    dollars = float(dollars)  
    exchange_rate = 83.0  
    rupees = dollars * exchange_rate
    result_text = f"{dollars} USD = {rupees:.2f} INR"  
    label_result.delete(1.0, tk.END)
    label_result.insert(tk.END, result_text)
root = tk.Tk()
root.title("Dollar to Rupee Converter")

label_title = tk.Label(root, text="Dollar to Rupee Converter", font=("Arial", 16))
label_dollars = tk.Label(root, text="Enter amount in USD:")
entry_dollars = tk.Entry(root)
button_convert = tk.Button(root, text="Convert", command=dollar_to_rupee)
label_result = tk.Text(root, height=2, width=30) 

label_title.grid(row=0, column=0, columnspan=2, pady=10)
label_dollars.grid(row=1, column=0, padx=5)
entry_dollars.grid(row=1, column=0, padx=5)
button_convert.grid(row=1, column=1, columnspan=2, pady=5)
label_result.grid(row=3, column=0, columnspan=2)


root.mainloop()
