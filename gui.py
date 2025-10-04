"""
GUI module for the Genre-Based File Organizer.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import queue
import logging
from pathlib import Path


class FileOrganizerGUI:
    """GUI for the Genre-Based File Organizer."""
    
    def __init__(self, root, organizer_callback):
        """Initialize the GUI.
        
        Args:
            root: Tkinter root window
            organizer_callback: Function to call for organizing files
        """
        self.root = root
        self.organizer_callback = organizer_callback
        self.processing = False
        self.message_queue = queue.Queue()
        
        # Configure root window
        self.root.title("Genre-Based File Organizer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set window icon (if available)
        try:
            # Try to set an icon - will fail gracefully if not available
            pass
        except:
            pass
        
        self._create_widgets()
        self._setup_queue_checker()
    
    def _create_widgets(self):
        """Create and layout GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="Genre-Based File Organizer",
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Intelligently organize your documents using semantic clustering",
            font=("Helvetica", 10)
        )
        desc_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Folder selection frame
        folder_frame = ttk.LabelFrame(main_frame, text="Select Folder", padding="10")
        folder_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        folder_frame.columnconfigure(1, weight=1)
        
        ttk.Label(folder_frame, text="Source Folder:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        self.folder_var = tk.StringVar()
        folder_entry = ttk.Entry(folder_frame, textvariable=self.folder_var, state="readonly")
        folder_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(folder_frame, text="Browse...", command=self._browse_folder)
        browse_btn.grid(row=0, column=2)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        options_frame.columnconfigure(1, weight=1)
        
        # Number of clusters
        ttk.Label(options_frame, text="Number of Groups:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        self.clusters_var = tk.StringVar(value="Auto")
        clusters_combo = ttk.Combobox(
            options_frame,
            textvariable=self.clusters_var,
            values=["Auto", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            state="readonly",
            width=15
        )
        clusters_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        
        # Copy/Move option
        self.copy_files_var = tk.BooleanVar(value=True)
        copy_check = ttk.Checkbutton(
            options_frame,
            text="Copy files (leave originals intact)",
            variable=self.copy_files_var
        )
        copy_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
        
        # Output log frame
        log_frame = ttk.LabelFrame(main_frame, text="Progress Log", padding="10")
        log_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            state="disabled"
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            main_frame,
            variable=self.progress_var,
            maximum=100,
            mode="indeterminate"
        )
        self.progress_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=(0, 0))
        
        self.organize_btn = ttk.Button(
            button_frame,
            text="Organize Files",
            command=self._organize_files,
            width=20
        )
        self.organize_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.cancel_btn = ttk.Button(
            button_frame,
            text="Cancel",
            command=self._cancel_operation,
            state="disabled",
            width=20
        )
        self.cancel_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(
            button_frame,
            text="Clear Log",
            command=self._clear_log,
            width=20
        )
        clear_btn.pack(side=tk.LEFT)
    
    def _browse_folder(self):
        """Open folder browser dialog."""
        folder = filedialog.askdirectory(title="Select Folder to Organize")
        if folder:
            self.folder_var.set(folder)
            self._log_message(f"Selected folder: {folder}")
    
    def _organize_files(self):
        """Start file organization in a separate thread."""
        folder = self.folder_var.get()
        
        if not folder:
            messagebox.showwarning("No Folder Selected", "Please select a folder to organize.")
            return
        
        if not Path(folder).exists():
            messagebox.showerror("Invalid Folder", f"The folder '{folder}' does not exist.")
            return
        
        # Get number of clusters
        clusters_str = self.clusters_var.get()
        n_clusters = None if clusters_str == "Auto" else int(clusters_str)
        
        # Get copy/move preference
        copy_files = self.copy_files_var.get()
        
        # Disable organize button, enable cancel
        self.organize_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        self.processing = True
        
        # Start progress bar
        self.progress_bar.start(10)
        
        # Clear log
        self._clear_log()
        self._log_message("=" * 60)
        self._log_message("Starting file organization...")
        self._log_message(f"Source folder: {folder}")
        self._log_message(f"Number of groups: {clusters_str}")
        self._log_message(f"Mode: {'Copy' if copy_files else 'Move'}")
        self._log_message("=" * 60)
        
        # Start organization in separate thread
        thread = threading.Thread(
            target=self._run_organizer,
            args=(folder, n_clusters, copy_files),
            daemon=True
        )
        thread.start()
    
    def _run_organizer(self, folder, n_clusters, copy_files):
        """Run the file organizer in a separate thread.
        
        Args:
            folder: Source folder path
            n_clusters: Number of clusters (None for auto)
            copy_files: Whether to copy (True) or move (False) files
        """
        try:
            # Run organizer with callback for progress updates
            result = self.organizer_callback(
                folder,
                n_clusters=n_clusters,
                copy_files=copy_files,
                progress_callback=self._progress_callback
            )
            
            # Show completion message
            if result:
                total_files = sum(len(files) for files in result.values())
                message = (
                    f"\n{'=' * 60}\n"
                    f"Organization Complete!\n"
                    f"Total files organized: {total_files}\n"
                    f"Number of groups: {len(result)}\n"
                    f"{'=' * 60}"
                )
                self.message_queue.put(("info", message))
                self.message_queue.put(("complete", result))
            else:
                self.message_queue.put(("warning", "No files were organized."))
                self.message_queue.put(("complete", None))
        
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            logging.error(error_msg, exc_info=True)
            self.message_queue.put(("error", error_msg))
            self.message_queue.put(("complete", None))
    
    def _progress_callback(self, message):
        """Callback for progress updates from organizer.
        
        Args:
            message: Progress message to display
        """
        self.message_queue.put(("info", message))
    
    def _cancel_operation(self):
        """Cancel the current operation."""
        if messagebox.askyesno("Cancel Operation", "Are you sure you want to cancel?"):
            self.processing = False
            self._log_message("\nOperation cancelled by user.")
            self._finish_processing()
    
    def _clear_log(self):
        """Clear the log text area."""
        self.log_text.config(state="normal")
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state="disabled")
    
    def _log_message(self, message):
        """Add a message to the log.
        
        Args:
            message: Message to log
        """
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
    
    def _setup_queue_checker(self):
        """Set up periodic checking of the message queue."""
        self._check_queue()
    
    def _check_queue(self):
        """Check the message queue for updates."""
        try:
            while True:
                msg_type, message = self.message_queue.get_nowait()
                
                if msg_type == "info":
                    self._log_message(message)
                elif msg_type == "warning":
                    self._log_message(f"WARNING: {message}")
                    messagebox.showwarning("Warning", message)
                elif msg_type == "error":
                    self._log_message(f"ERROR: {message}")
                    messagebox.showerror("Error", message)
                    self._finish_processing()
                elif msg_type == "complete":
                    self._finish_processing()
                    if message:
                        messagebox.showinfo(
                            "Success",
                            f"Files organized successfully!\n\n"
                            f"Total files: {sum(len(files) for files in message.values())}\n"
                            f"Groups created: {len(message)}"
                        )
        
        except queue.Empty:
            pass
        
        # Schedule next check
        self.root.after(100, self._check_queue)
    
    def _finish_processing(self):
        """Clean up after processing is complete."""
        self.processing = False
        self.progress_bar.stop()
        self.organize_btn.config(state="normal")
        self.cancel_btn.config(state="disabled")


def create_gui(organizer_callback):
    """Create and run the GUI.
    
    Args:
        organizer_callback: Function to call for organizing files
    """
    root = tk.Tk()
    app = FileOrganizerGUI(root, organizer_callback)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()
