import tkinter as tk

window = tk.Tk()

window.title("Goal Planner")

window.state("zoomed")

window.configure(bg='#230b8f')

def submit_card():
    # Get the entered text from the Entry widget
    text = entry.get()
    
    # Create a new card with the entered text
    card_label = tk.Label(frame, text=text)
    card_label.pack()

    # Clear the text in the Entry widget
    entry.delete(0, tk.END)


# Create a frame to hold the cards
frame = tk.Frame(window)
frame.pack()

# Create an Entry widget for text input
entry = tk.Entry(window)
entry.pack()

# Create a Button widget to submit the card
submit_button = tk.Button(window, text="Submit", command=submit_card)
submit_button.pack()

# Run the Tkinter event loop
window.mainloop()


window.mainloop()