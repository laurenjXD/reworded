import customtkinter as ctk
from tkinter import messagebox, filedialog
from itertools import permutations, combinations
import os
from collections import defaultdict

# --- Configuration & Theme ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Color Palette
COLOR_BG = "#0D1117"        # Very dark background
COLOR_CARD = "#161B22"      # Dark grey/blue for cards
COLOR_ACCENT = "#8E44AD"    # Purple
COLOR_ACCENT_HOVER = "#9B59B6"
COLOR_TEXT_SUB = "#8B949E"  # Muted grey
COLOR_SUCCESS = "#2ECC71"   # Green

# --- Logic: Dictionary Loading ---
def load_dictionary(default_filename="words_alpha.txt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, default_filename)
    
    if not os.path.exists(file_path):
        response = messagebox.askyesno("File Not Found", f"Could not find '{default_filename}'.\n\nBrowse for it?")
        if response:
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if not file_path: return set()
        else:
            return set()

    try:
        with open(file_path, "r") as f:
            return set(word.strip().lower() for word in f if word.strip())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")
        return set()

DICTIONARY = load_dictionary()

# --- Logic: Functions ---
def generate_results():
    word = entry_input.get().strip().lower()
    try:
        min_len = int(entry_min_len.get())
    except ValueError:
        min_len = 2

    if not word.isalpha():
        messagebox.showerror("Invalid Input", "Please enter letters only.")
        return

    letters = list(word)
    all_perms_set = set()
    valid_words_set = set()
    
    # Generate Logic
    for r in range(min_len, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                joined = "".join(perm)
                all_perms_set.add(joined)
                if joined in DICTIONARY:
                    valid_words_set.add(joined)

    # Format "All Combinations"
    raw_text = f"(Total {len(all_perms_set)} unique strings)\n\n"
    raw_text += ", ".join(sorted(list(all_perms_set)))
    
    # Format "Valid Words"
    valid_grouped = defaultdict(list)
    for w in valid_words_set:
        valid_grouped[len(w)].append(w)
    
    valid_text = f"(Total {len(valid_words_set)} valid words)\n\n"
    for length in sorted(valid_grouped.keys()):
        words = sorted(valid_grouped[length])
        valid_text += f"{length}-Letter Words:\n" + ", ".join(words) + "\n\n"

    # Update Text Boxes (Populate both, visibility handled by toggle)
    textbox_all.configure(state="normal")
    textbox_all.delete("1.0", "end")
    textbox_all.insert("end", raw_text)
    textbox_all.configure(state="disabled")

    textbox_valid.configure(state="normal")
    textbox_valid.delete("1.0", "end")
    textbox_valid.insert("end", valid_text)
    textbox_valid.configure(state="disabled")

def clear_fields():
    entry_input.delete(0, "end")
    
    # Reset Textboxes
    for tb, msg in [(textbox_all, "Waiting for input..."), (textbox_valid, "Enter letters to see valid words...")]:
        tb.configure(state="normal")
        tb.delete("1.0", "end")
        tb.insert("1.0", msg)
        tb.configure(state="disabled")

def toggle_view(value):
    """Switches visibility between the two cards based on selection"""
    if value == "Valid Dictionary Words":
        card_all.grid_remove()  # Hide All
        card_valid.grid(row=1, column=0, sticky="nsew") # Show Valid
    else:
        card_valid.grid_remove() # Hide Valid
        card_all.grid(row=1, column=0, sticky="nsew")   # Show All

# --- GUI Construction ---
app = ctk.CTk(fg_color=COLOR_BG)
app.title("Re:Worded")
app.geometry("900x600")

# Layout Configuration
app.grid_columnconfigure(0, weight=1, minsize=300) 
app.grid_columnconfigure(1, weight=2)              
app.grid_rowconfigure(0, weight=1)

# === LEFT PANEL ===
frame_left = ctk.CTkFrame(app, fg_color=COLOR_CARD, corner_radius=20)
frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
frame_left.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(frame_left, text="INPUT & CONTROLS", text_color=COLOR_TEXT_SUB, font=("Arial", 12, "bold")).pack(pady=(30, 10), anchor="w", padx=20)
ctk.CTkLabel(frame_left, text="Re-Worded", text_color="white", font=("Arial", 32, "bold")).pack(anchor="w", padx=20)
ctk.CTkLabel(frame_left, text="Permutation Playground", text_color=COLOR_TEXT_SUB, font=("Arial", 12)).pack(anchor="w", padx=20, pady=(0, 20))

ctk.CTkLabel(frame_left, text="Enter Letters", text_color="white", font=("Arial", 14, "bold")).pack(anchor="w", padx=20, pady=(10, 5))
entry_input = ctk.CTkEntry(frame_left, placeholder_text="e.g. apple", height=40, border_color=COLOR_ACCENT, border_width=2, corner_radius=10)
entry_input.pack(fill="x", padx=20, pady=(0, 20))

ctk.CTkLabel(frame_left, text="Min. Word Length", text_color="white", font=("Arial", 14)).pack(anchor="w", padx=20, pady=(20, 5))
entry_min_len = ctk.CTkSegmentedButton(frame_left, values=["2", "3", "4", "5"], selected_color=COLOR_ACCENT)
entry_min_len.set("3")
entry_min_len.pack(fill="x", padx=20, pady=(0, 20))

# Generate Button
btn_generate = ctk.CTkButton(
    frame_left, text="GENERATE WORDS", fg_color=COLOR_ACCENT, hover_color=COLOR_ACCENT_HOVER, 
    height=50, corner_radius=25, font=("Arial", 14, "bold"), command=generate_results
)
btn_generate.pack(fill="x", padx=20, pady=(30, 10))

# Clear Button
btn_clear = ctk.CTkButton(
    frame_left, text="Clear / Reset", fg_color="transparent", border_width=1, border_color=COLOR_TEXT_SUB, 
    text_color=COLOR_TEXT_SUB, hover_color="#2c3e50", height=35, command=clear_fields
)
btn_clear.pack(fill="x", padx=20, pady=(0, 20))

# Credits
ctk.CTkLabel(frame_left, text="S-CSPC212 – Discrete Structures 1\nGuterless, Kriatien\nSantos, Andjhelyn", 
             text_color=COLOR_TEXT_SUB, font=("Arial", 10), justify="left").pack(side="bottom", anchor="w", padx=20, pady=30)

# === RIGHT PANEL (Swappable Views) ===
frame_right = ctk.CTkFrame(app, fg_color="transparent")
frame_right.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
frame_right.grid_rowconfigure(1, weight=1) # The cards in row 1 expand
frame_right.grid_columnconfigure(0, weight=1)

# 1. View Switcher (Tabs)
view_selector = ctk.CTkSegmentedButton(frame_right, values=["Valid Dictionary Words", "All Combinations"], 
                                       command=toggle_view, selected_color=COLOR_ACCENT, height=40)
view_selector.set("Valid Dictionary Words")
view_selector.grid(row=0, column=0, pady=(0, 10), sticky="ew")

# 2. Card: All Combinations (Hidden by default)
card_all = ctk.CTkFrame(frame_right, fg_color=COLOR_CARD, corner_radius=20)
# Note: We don't grid it yet. The toggle function handles it.

ctk.CTkLabel(card_all, text="All Possible Combinations", font=("Arial", 16, "bold")).pack(anchor="w", padx=20, pady=(20, 10))
textbox_all = ctk.CTkTextbox(card_all, text_color=COLOR_TEXT_SUB, font=("Consolas", 12), fg_color="transparent", wrap="word")
textbox_all.pack(fill="both", expand=True, padx=20, pady=(0, 20))
textbox_all.insert("1.0", "Waiting for input...")
textbox_all.configure(state="disabled")

# 3. Card: Valid Words (Visible by default)
card_valid = ctk.CTkFrame(frame_right, fg_color=COLOR_CARD, corner_radius=20)
card_valid.grid(row=1, column=0, sticky="nsew") # Default visible

header_frame = ctk.CTkFrame(card_valid, fg_color="transparent")
header_frame.pack(fill="x", padx=20, pady=(20, 10))
ctk.CTkLabel(header_frame, text="✔", text_color=COLOR_SUCCESS, font=("Arial", 18, "bold")).pack(side="left", padx=(0, 10))
ctk.CTkLabel(header_frame, text="Valid Dictionary Words", font=("Arial", 16, "bold")).pack(side="left")

textbox_valid = ctk.CTkTextbox(card_valid, text_color=COLOR_SUCCESS, font=("Consolas", 14), fg_color="transparent", wrap="word")
textbox_valid.pack(fill="both", expand=True, padx=20, pady=(0, 20))
textbox_valid.insert("1.0", "Enter letters to see valid words...")
textbox_valid.configure(state="disabled")

app.mainloop()