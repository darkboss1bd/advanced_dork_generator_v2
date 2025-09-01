import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import pyperclip

class DorkGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 darkboss1bd - Advanced Dork Generator")
        self.root.geometry("800x700")
        self.root.resizable(False, False)

        # Themes
        self.themes = {
            "Dark": {
                "bg": "#121212",
                "fg": "#ffffff",
                "text_bg": "#1e1e1e",
                "text_fg": "#00ff00",
                "btn": "#00ff00",
                "btn_fg": "#000000",
                "highlight": "#00ff00"
            },
            "Hacker": {
                "bg": "#000000",
                "fg": "#00ff00",
                "text_bg": "#000000",
                "text_fg": "#00ff00",
                "btn": "#00ff00",
                "btn_fg": "#000000",
                "highlight": "#00ff00"
            },
            "Light": {
                "bg": "#f0f0f0",
                "fg": "#000000",
                "text_bg": "#ffffff",
                "text_fg": "#0000ff",
                "btn": "#0066cc",
                "btn_fg": "#ffffff",
                "highlight": "#0066cc"
            }
        }
        self.current_theme = "Hacker"
        self.style = self.themes[self.current_theme]

        self.create_widgets()
        self.create_banner()
        self.create_animation_canvas()
        self.start_animation()

    def create_widgets(self):
        self.root.configure(bg=self.style["bg"])

        # Theme Selector
        theme_frame = tk.Frame(self.root, bg=self.style["bg"])
        theme_frame.place(x=10, y=650, width=300, height=40)

        tk.Label(
            theme_frame,
            text="Theme:",
            font=("Arial", 10),
            bg=self.style["bg"],
            fg=self.style["fg"]
        ).pack(side="left")

        self.theme_combo = ttk.Combobox(
            theme_frame,
            values=list(self.themes.keys()),
            state="readonly",
            font=("Arial", 10)
        )
        self.theme_combo.set(self.current_theme)
        self.theme_combo.pack(side="left", padx=5)
        self.theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

        # URL Input
        input_frame = tk.LabelFrame(
            self.root,
            text="🌐 Enter Website URL",
            font=("Arial", 12, "bold"),
            bg=self.style["bg"],
            fg=self.style["highlight"],
            bd=2,
            relief="groove"
        )
        input_frame.place(x=10, y=80, width=780, height=70)

        self.url_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg=self.style["text_bg"],
            fg=self.style["fg"],
            insertbackground=self.style["highlight"]
        )
        self.url_entry.pack(pady=10, padx=10, fill="x")

        # Generate Button
        generate_btn = tk.Button(
            self.root,
            text="⚡ Generate Dorks",
            font=("Arial", 12, "bold"),
            bg=self.style["btn"],
            fg=self.style["btn_fg"],
            command=self.generate_dorks
        )
        generate_btn.place(x=320, y=160, width=160, height=40)

        # Output Frame
        output_frame = tk.LabelFrame(
            self.root,
            text="🔍 Generated Dorks",
            font=("Arial", 12, "bold"),
            bg=self.style["bg"],
            fg=self.style["highlight"],
            bd=2,
            relief="groove"
        )
        output_frame.place(x=10, y=210, width=780, height=430)

        # Canvas for scrollable dorks
        self.canvas = tk.Canvas(output_frame, bg=self.style["text_bg"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.style["text_bg"])

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Copy All Button
        copy_btn = tk.Button(
            self.root,
            text="📋 Copy All",
            font=("Arial", 10, "bold"),
            bg=self.style["highlight"],
            fg=self.style["btn_fg"],
            command=self.copy_dorks
        )
        copy_btn.place(x=680, y=655, width=100, height=30)

    def create_banner(self):
        banner_frame = tk.Frame(self.root, bg=self.style["bg"], bd=2, relief="solid")
        banner_frame.place(x=10, y=10, width=780, height=60)

        banner_label = tk.Label(
            banner_frame,
            text="🔐 darkboss1bd - ADVANCED DORK GENERATOR 🔐",
            font=("Courier", 14, "bold"),
            bg=self.style["bg"],
            fg=self.style["highlight"]
        )
        banner_label.pack(expand=True)

    def create_animation_canvas(self):
        self.anim_canvas = tk.Canvas(self.root, bg=self.style["bg"], height=20, highlightthickness=0)
        self.anim_canvas.place(x=10, y=60, width=780)

        self.anim_text = "ACCESSING SYSTEM... BYPASSING FIREWALL... DECRYPTING DATA... ROOT ACCESS GRANTED... "
        self.anim_text += self.anim_text
        self.anim_pos = 800
        self.anim_id = self.anim_canvas.create_text(
            self.anim_pos, 10,
            text=self.anim_text,
            font=("Courier", 10, "bold"),
            fill=self.style["highlight"],
            anchor="w"
        )

    def start_animation(self):
        self.animate_text()

    def animate_text(self):
        self.anim_pos -= 2
        if self.anim_pos < -len(self.anim_text) * 8:
            self.anim_pos = 800
        self.anim_canvas.coords(self.anim_id, self.anim_pos, 10)
        self.root.after(50, self.animate_text)

    def change_theme(self, event=None):
        self.current_theme = self.theme_combo.get()
        self.style = self.themes[self.current_theme]
        self.create_widgets()
        self.generate_dorks()  # Refresh dorks with new theme

    def generate_dorks(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a valid website URL!")
            return

        # Clean URL
        if url.startswith(("http://", "https://")):
            url = url.split("://")[1]
        if url.endswith("/"):
            url = url[:-1]

        dorks = [
            f'inurl:"{url}"',
            f'intitle:"index of" site:{url}',
            f'filetype:pdf site:{url}',
            f'filetype:doc site:{url}',
            f'intext:"admin" site:{url}',
            f'intext:"login" site:{url}',
            f'site:{url} ext:php | ext:asp | ext:aspx | ext:js',
            f'cache:{url}',
            f'link:{url}',
            f'related:{url}'
        ]

        for dork in dorks:
            dork_frame = tk.Frame(self.scrollable_frame, bg=self.style["text_bg"])
            dork_frame.pack(fill="x", pady=2)

            dork_label = tk.Label(
                dork_frame,
                text=dork,
                font=("Consolas", 10),
                bg=self.style["text_bg"],
                fg=self.style["text_fg"],
                wraplength=600,
                anchor="w",
                justify="left"
            )
            dork_label.pack(side="left", padx=(5, 10))

            search_btn = tk.Button(
                dork_frame,
                text="🔍 Search",
                font=("Arial", 9, "bold"),
                bg=self.style["highlight"],
                fg=self.style["btn_fg"],
                width=10,
                command=lambda d=dork: self.search_google(d)
            )
            search_btn.pack(side="right", padx=5)

    def search_google(self, dork):
        query = dork.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(url)

    def copy_dorks(self):
        content = ""
        for widget in self.scrollable_frame.winfo_children():
            label = widget.winfo_children()[0]
            if isinstance(label, tk.Label):
                content += label.cget("text") + "\n"

        if content.strip():
            pyperclip.copy(content)
            messagebox.showinfo("Copied!", "All dorks copied to clipboard!")
        else:
            messagebox.showwarning("Empty", "No dorks to copy!")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DorkGeneratorApp(root)
    root.mainloop()