import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
from PIL import Image, ImageTk, ImageDraw
import sys
import math
import VPN_GUI
import VLAN_Routing

try:
    from Main_GUI import NetworkApp
except ImportError:
    class MockBackend:
        def run_dns_config_logic(self, *args):
            import time
            time.sleep(1)
            return ["Mock configuration applied."]
    backendFinalVersion = MockBackend()
    
    class NetworkApp:
        def __init__(self, root, back_callback):
            self.root = root
            self.back_callback = back_callback
            ctk.CTkLabel(root, text="Mock DHCP Interface").pack(pady=20)
            ctk.CTkButton(root, text="Back", command=back_callback).pack()

# إعدادات الواجهة المستقبلية
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# ألوان فضائية مستقبلية
SPACE_DARK = "#050b14"
SPACE_MID = "#0a1628"
SPACE_LIGHT = "#0f2138"
NEON_BLUE = "#00d4ff"
NEON_CYAN = "#00ffff"
NEON_PURPLE = "#b300ff"
SILVER = "#c0c0c0"
HOLO_GREEN = "#00ff88"
WARP_CORE = "#ff3366"
STAR_WHITE = "#e8eef2"
DEEP_SPACE = "#01050f"

def safe_load_image(path):
    try:
        return Image.open(path)
    except Exception:
        return None

def launch_vpn_interface():
    VPN_GUI.open_vpn_window(welcome_root)

def launch_advanced_automation():
    VLAN_Routing.open_automation_window(welcome_root)

# ---------------------------------------------------------
# دوال مساعدة للواجهة الفضائية
# ---------------------------------------------------------
def create_futuristic_canvas(parent):
    """إنشاء خلفية فضائية مع نجوم متحركة"""
    canvas = tk.Canvas(parent, highlightthickness=0, bg=DEEP_SPACE)
    
    # رسم نجوم ثابتة
    import random
    for _ in range(150):
        x = random.randint(0, 2000)
        y = random.randint(0, 2000)
        brightness = random.randint(100, 255)
        color = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
        canvas.create_oval(x-1, y-1, x+1, y+1, fill=color, outline="", tags="star")
    
    # رسم سديم (Nebula) باستخدام دوائر شفافة
    canvas.create_oval(100, 100, 400, 400, fill="#003366", outline="", stipple="gray50", tags="nebula")
    canvas.create_oval(500, 400, 800, 700, fill="#330066", outline="", stipple="gray50", tags="nebula")
    canvas.create_oval(600, 100, 900, 350, fill="#006666", outline="", stipple="gray25", tags="nebula")
    
    return canvas

def create_futuristic_button(parent, text, command, color=NEON_BLUE):
    """إنشاء زر مستقبلي بتأثير توهج"""
    btn_frame = tk.Frame(parent, bg=DEEP_SPACE)
    
    # زر رئيسي
    button = ctk.CTkButton(
        btn_frame,
        text=text,
        font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
        width=340,
        height=52,
        corner_radius=25,
        fg_color="transparent",
        hover_color=color + "33",
        text_color=color,
        border_width=2,
        border_color=color
    )
    button.configure(command=command)
    button.pack()
    
    return btn_frame

def create_hologram_card(parent, title):
    """إنشاء بطاقة هولوغرام مستقبلية"""
    card = tk.Frame(parent, bg=DEEP_SPACE, highlightthickness=0)
    
    # إطار خارجي مضيء
    outer_frame = tk.Frame(card, bg=NEON_BLUE, highlightthickness=0)
    outer_frame.pack(fill="both", expand=True, padx=1, pady=1)
    
    # إطار داخلي
    inner_frame = tk.Frame(outer_frame, bg=SPACE_MID, highlightthickness=0)
    inner_frame.pack(fill="both", expand=True, padx=1, pady=1)
    
    # رأس البطاقة
    header = tk.Frame(inner_frame, bg=SPACE_LIGHT, height=45)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    # خط توهج في الأعلى
    glow_line = tk.Frame(header, bg=NEON_BLUE, height=2)
    glow_line.pack(fill="x")
    
    title_label = tk.Label(
        header,
        text=f"◆ {title} ◆",
        font=("Segoe UI", 13, "bold"),
        bg=SPACE_LIGHT,
        fg=NEON_CYAN
    )
    title_label.pack(pady=10)
    
    return inner_frame

# ---------------------------------------------------------
# نافذة DNS   
# ---------------------------------------------------------
def open_dns_interface_window():
    welcome_root.withdraw()
    dns_win = tk.Toplevel(welcome_root)
    dns_win.minsize(900, 700)
    dns_win.geometry("1000x700")
    dns_win.title("Unified Network Configuration Tool DNS")
    dns_win.configure(bg="#f0f8ff")

    def go_back_to_welcome():
        dns_win.destroy()
        welcome_root.deiconify()

    main_frame = tk.Frame(dns_win, bg="#f0f8ff", padx=30, pady=30)
    main_frame.pack(fill="both", expand=True)

    title_label = tk.Label(main_frame, text="🌐 Unified Network Settings (DNS)", 
                          font=('Segoe UI', 24, 'bold'), bg="#f0f8ff", fg="#1e88e5")
    title_label.pack(pady=(20, 40))

    network_config_frame = tk.LabelFrame(main_frame, text=" ⚙️ Core Network Configuration ",
                                        font=('Arial', 14, 'bold'), bg="#ffffff", fg="#34495e",
                                        padx=40, pady=40, highlightthickness=2)
    network_config_frame.pack(fill="x", padx=100, pady=20)

    tk.Label(network_config_frame, text="Router Gateway IP:", font=('Arial', 12, 'bold'), bg="#ffffff").grid(row=0, column=0, padx=20, pady=15, sticky="w")
    router_entry = tk.Entry(network_config_frame, width=35, font=('Arial', 12))
    router_entry.grid(row=0, column=1, padx=20, pady=15, sticky="we")

    tk.Label(network_config_frame, text="Primary DNS Server IP:", font=('Arial', 12, 'bold'), bg="#ffffff").grid(row=1, column=0, padx=20, pady=15, sticky="w")
    dns_entry = tk.Entry(network_config_frame, width=35, font=('Arial', 12))
    dns_entry.grid(row=1, column=1, padx=20, pady=15, sticky="we")

    def apply_config():
        router_ip = router_entry.get()
        primary_dns = dns_entry.get()
        def run_thread():
            apply_button.config(state=tk.DISABLED, text="Applying...")
            try:
                logs = backendFinalVersion.run_dns_config_logic(router_ip, primary_dns, "admin", "cisco123", "cisco")
                messagebox.showinfo("Result", "\n".join(logs))
            finally:
                apply_button.config(state=tk.NORMAL, text="🚀 Apply All Settings")
        threading.Thread(target=run_thread).start()

    apply_button = tk.Button(network_config_frame, text="🚀 Apply All Settings", command=apply_config,
                            font=('Arial', 13, 'bold'), bg="#2ecc71", fg="white", pady=8)
    apply_button.grid(row=2, column=0, columnspan=2, pady=30)

    tk.Button(dns_win, text="⬅️ Back", font=('Arial', 11, 'bold'), bg="#e74c3c", fg="white",
              command=go_back_to_welcome).place(relx=0.97, rely=0.97, anchor="se")
# ---------------------------------------------------------
# النافذة الرئيسية - تصميم مستقبلي فضائي
# ---------------------------------------------------------
if __name__ == "__main__":
    welcome_root = ctk.CTk()
    welcome_root.title("◆ SPACE NETWORK COMMAND CENTER ◆")
    WINDOW_WIDTH, WINDOW_HEIGHT = 850, 750
    welcome_root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    welcome_root.configure(fg_color=DEEP_SPACE)
    welcome_root.minsize(750, 650)
    
    # خلفية فضائية متحركة
    space_canvas = create_futuristic_canvas(welcome_root)
    space_canvas.pack(fill="both", expand=True)
    
    # إطار شفاف رئيسي
    main_frame = tk.Frame(space_canvas, bg=DEEP_SPACE)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.9)
    
    # رأس القيادة
    command_header = tk.Frame(main_frame, bg=SPACE_MID, highlightthickness=0)
    command_header.pack(fill="x", pady=(0, 25))
    
    # خطوط زخرفية
    top_line = tk.Frame(command_header, bg=NEON_BLUE, height=2)
    top_line.pack(fill="x")
    
    header_content = tk.Frame(command_header, bg=SPACE_MID)
    header_content.pack(pady=15)
    
    # عنوان رئيسي
    main_title = tk.Label(
        header_content,
        text="◢ SPACE NETWORK COMMAND CENTER ◣",
        font=("Segoe UI", 24, "bold"),
        bg=SPACE_MID,
        fg=NEON_CYAN
    )
    main_title.pack()
    
    subtitle = tk.Label(
        header_content,
        text="◆ ADVANCED NETWORK CONTROL SYSTEM ◆ v2.6 ◆",
        font=("Courier New", 11),
        bg=SPACE_MID,
        fg=SILVER
    )
    subtitle.pack(pady=(5, 0))
    
    bottom_line = tk.Frame(command_header, bg=NEON_BLUE, height=1)
    bottom_line.pack(fill="x")
    
    # بطاقة الأزرار المستقبلية
    console_frame = tk.Frame(main_frame, bg=DEEP_SPACE)
    console_frame.pack(fill="both", expand=True)
    
    # نافذة DHCP
    network_app_root = tk.Tk()
    network_app_root.withdraw()
    app_instance = NetworkApp(network_app_root, back_callback=lambda: [network_app_root.withdraw(), welcome_root.deiconify()])
    
    # أزرار فضائية
    btn_dhcp = create_futuristic_button(
        console_frame,
        "🛸  DHCP CONFIGURATION MODULE",
        lambda: [welcome_root.withdraw(), network_app_root.deiconify()],
        HOLO_GREEN
    )
    btn_dhcp.pack(pady=40)
    
    btn_dns = create_futuristic_button(
        console_frame,
        "🌌  DNS CONFIGURATION MODULE",
        open_dns_interface_window,
        NEON_BLUE
    )
    btn_dns.pack(pady=40)
    
    btn_vpn = create_futuristic_button(
        console_frame,
        "🔮  VPN CONFIGURATION MODULE",
        launch_vpn_interface,
        NEON_PURPLE
    )
    btn_vpn.pack(pady=40)
    
    btn_vlan = create_futuristic_button(
        console_frame,
        "⚡  VLAN & OSPF AUTOMATION",
        launch_advanced_automation,
        WARP_CORE
    )
    btn_vlan.pack(pady=40)
    
    # لوحة تحكم سفلية
    control_panel = tk.Frame(main_frame, bg=SPACE_MID, height=50)
    control_panel.pack(fill="x", pady=(20, 0))
    control_panel.pack_propagate(False)
    
    # أزرار تحكم
    exit_button = ctk.CTkButton(
        control_panel,
        text="◆ POWER OFF ◆",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        width=100,
        height=30,
        corner_radius=15,
        fg_color="transparent",
        hover_color=WARP_CORE + "33",
        text_color=WARP_CORE,
        border_width=1,
        border_color=WARP_CORE,
        command=lambda: sys.exit()
    )
    exit_button.pack(side="right", padx=15)
    
    # مؤشرات حالة
    status_text = tk.Label(
        control_panel,
        text="◆ ALL SYSTEMS OPERATIONAL ◆",
        font=("Courier New", 10),
        bg=SPACE_MID,
        fg=HOLO_GREEN
    )
    status_text.pack(side="left", padx=15)
    
    # مؤشر وامض (blinking dot)
    def blink():
        current = status_text.cget("fg")
        next_color = HOLO_GREEN if current == DEEP_SPACE else DEEP_SPACE
        status_text.configure(fg=next_color)
        space_canvas.after(800, blink)
    
    blink()
    
    welcome_root.mainloop()