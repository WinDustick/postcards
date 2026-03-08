import streamlit as st
import time
import random
import html

# Настройка страницы (изменено на wide для широкого терминала)
st.set_page_config(page_title="SECURE TRANSMISSION", page_icon="🔒", layout="wide")

# CSS для имитации хакерского терминала
st.markdown("""
<style>
    .stApp {
        background-color: #0c0c0c;
    }
    .terminal-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        line-height: 1.2;
        margin-bottom: 0px;
        /* Жестко фиксируем пробелы и запрещаем перенос строк! */
        white-space: pre !important; 
        overflow-x: auto;
    }
    .green { color: #00ff00; }
    .pink { color: #ff77ff; }
    .cyan { color: #00ffff; }
    .yellow { color: #ffff00; }
    .red { color: #ff0000; }
    .white { color: #ffffff; }
    
    /* Стилизация кнопки Streamlit */
    div.stButton > button {
        background-color: #000000;
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        width: 100%;
        margin-top: 20px;
    }
    div.stButton > button:hover {
        background-color: #00ff00;
        color: #000000;
        border: 1px solid #00ff00;
    }
</style>
""", unsafe_allow_html=True)

class StreamlitAnimator:
    """Аниматор, адаптированный под рендеринг Streamlit"""
    
    def __init__(self):
        self.glitch_chars = "01#$%&<>?{}[]/~X@!|"
        self.rus_glitch = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"

    def type_text(self, text: str, color_class: str = "green", speed: float = 0.02):
        """Эффект печатной машинки"""
        placeholder = st.empty()
        current_text = ""
        for char in text:
            current_text += char
            safe_text = html.escape(current_text)
            placeholder.markdown(f"<div class='terminal-text {color_class}'>{safe_text}</div>", unsafe_allow_html=True)
            time.sleep(speed)

    def progress_bar_effect(self, steps: int = 15, label: str = "Loading"):
        """Анимация прогресс-бара"""
        placeholder = st.empty()
        for i in range(steps + 1):
            percent = i / steps
            bar = "█" * int(percent * 30) + "░" * (30 - int(percent * 30))
            safe_label = html.escape(label)
            placeholder.markdown(f"<div class='terminal-text cyan'>[*] {safe_label}: [{bar}] {int(percent * 100)}%</div>", unsafe_allow_html=True)
            time.sleep(0.05)

    def hex_reveal_effect(self, text: str, color_class: str = "cyan", duration: float = 2.5):
        """Анимация Hex-дампа в Streamlit"""
        placeholder = st.empty()
        chars = list(text)
        chunk_size = 16
        lines = [chars[i:i+chunk_size] for i in range(0, len(chars), chunk_size)]
        
        iterations = int(duration / 0.1)
        for step in range(iterations):
            prob = (step / iterations) ** 1.5
            output = ""
            for i, line_chars in enumerate(lines):
                offset = f"0x{i*chunk_size:04x}"
                hex_list = []
                ascii_list = []
                
                for char in line_chars:
                    if char == ' ' or random.random() < prob:
                        hex_list.append(f"{ord(char) % 256:02x}")
                        ascii_list.append(char)
                    else:
                        hex_list.append(f"{random.randint(0, 255):02x}")
                        ascii_list.append(random.choice(self.glitch_chars))
                        
                hex_part = " ".join(hex_list)
                padding = "   " * (chunk_size - len(line_chars))
                ascii_part = html.escape("".join(ascii_list))
                output += f"{offset}  {hex_part}{padding} |{ascii_part}|\n"
                
            placeholder.markdown(f"<div class='terminal-text {color_class}'>{output}</div>", unsafe_allow_html=True)
            time.sleep(0.1)
            
        # Схлопывание в финальный текст
        time.sleep(0.5)
        safe_text = html.escape(text)
        placeholder.markdown(f"<div class='terminal-text green'>[+] DECRYPTED: {safe_text}</div>", unsafe_allow_html=True)

    def bruteforce_effect(self, target: str, color_class: str = "green", duration: float = 2.0):
        """Эффект подбора символов (брутфорс)"""
        placeholder = st.empty()
        chars = list(target)
        pool = self.glitch_chars + self.rus_glitch
        
        current = [' ' if c == ' ' else random.choice(pool) for c in chars]
        locked = [True if c == ' ' else False for c in chars]
        
        iterations = int(duration / 0.05)
        if iterations < 1: iterations = 1
        
        for step in range(iterations):
            lock_prob = (step / iterations) ** 1.5 
            
            for i in range(len(chars)):
                if not locked[i]:
                    if random.random() < lock_prob:
                        locked[i] = True
                        current[i] = chars[i]
                    else:
                        current[i] = random.choice(pool)
            
            display_text = html.escape("".join(current))
            placeholder.markdown(f"<div class='terminal-text {color_class}'>{display_text}</div>", unsafe_allow_html=True)
            time.sleep(0.05)
            
        safe_target = html.escape(target)
        placeholder.markdown(f"<div class='terminal-text {color_class}'>{safe_target}</div>", unsafe_allow_html=True)

    def bruteforce_and_type(self, prefix: str, suffix: str, prefix_duration: float = 0.8):
        """Комбинированный эффект: брутфорс префикса, затем печать суффикса на той же строке"""
        placeholder = st.empty()
        chars = list(prefix)
        pool = self.glitch_chars + self.rus_glitch
        current = [' ' if c == ' ' else random.choice(pool) for c in chars]
        locked = [True if c == ' ' else False for c in chars]
        
        iterations = int(prefix_duration / 0.05)
        
        # 1. Брутфорс префикса
        for step in range(iterations):
            lock_prob = (step / iterations) ** 1.5 
            for i in range(len(chars)):
                if not locked[i]:
                    if random.random() < lock_prob:
                        locked[i] = True
                        current[i] = chars[i]
                    else:
                        current[i] = random.choice(pool)
            
            display_text = html.escape("".join(current))
            placeholder.markdown(f"<div class='terminal-text'><span class='green'>{display_text}</span></div>", unsafe_allow_html=True)
            time.sleep(0.05)
            
        # 2. Допечатываем суффикс
        full_suffix = f"  ↳ {suffix}"
        current_suffix = ""
        for char in full_suffix:
            current_suffix += char
            safe_prefix = html.escape(prefix)
            safe_suffix = html.escape(current_suffix)
            html_content = f"<span class='green'>{safe_prefix}</span><span class='yellow'>{safe_suffix}</span>"
            placeholder.markdown(f"<div class='terminal-text'>{html_content}</div>", unsafe_allow_html=True)
            time.sleep(0.02)

    def draw_ascii_flower(self):
        """Отрисовка цветного ASCII-арт цветка для Streamlit с защитой от сжатия пробелов"""
        ascii_art = r'''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░`                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░`                      `░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░                           `░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░`                              `░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░                                 `░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░'                                  :░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░                                    ░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░                                    ░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░                                    ░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░        >.      ¿▒µ      .<        .░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░       j╫╫╫╫K╦▒▒▒▒▒▒╦▒▒▒▒▒        ░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░      j╫╫╫╫╫╫╫╫▒▒▒▒▒▒▒▒▒▒       ░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░     j▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░   j▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░`    ;▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     "░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░`       j▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        `░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░          j▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           ░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░             ▒▒▒╫╫╫╫╫▒▒▒▒▒▒▒▒▒              ░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░                ╨╫╫╫╫╫╫╫▒▒▒▒▒▒▒                `░░░░░░░░░░░░░░
░░░░░░░░░░░░                  `╨╝╫╫▓╫▒▒╫M╨`                   ░░░░░░░░░░░░░
░░░░░░░░░░░                       `╨▓▀`    .                   ░░░░░░░░░░░░
░░░░░░░░░░                   ╫▓▓▓µ  ▓  ╥▄▓▓▓▓▓▓▄                ░░░░░░░░░░░
░░░░░░░░░                    ▐▓▓▓▓▓µ▓.╫▓▓▓▓▓▓▓▓▓▓µ              `░░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌▓▒▓▓▓▓▓▓▀▀▀▀▀M               ░░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌▓▒▓▓▓▓▓▌                     :░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌▓▒▓▓▓▓▓▌                     :░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌▓▒▓▓▓▓▓▓                     :░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌▓▒▓▓▓▓▓▌                     ░░░░░░░░░░
░░░░░░░░░                    ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▓                    .░░░░░░░░░░
░░░░░░░░░░                   ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▓                    ░░░░░░░░░░░
░░░░░░░░░░░                  ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▓                   ░░░░░░░░░░░░
░░░░░░░░░░░░                 ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▌                  ░░░░░░░░░░░░░
░░░░░░░░░░░░░                ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▌                 ░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░              ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▌               :░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░.            ╫▓▓▓▓▓▌╫▒▓▓▓▓▓▓             .░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░          j▓▓▓▓▓▌╫▒▓▓▓▓▓▌           ░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░        ╨▓▓▓▓▌╫╫▓▓▓▓▀        .:░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░.     ╙▀▀▀╫▒▀▀╩`    ..░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░~.╫░.~░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'''
        
        placeholder = st.empty()
        lines = ascii_art.split('\n')
        background_chars = set('░"\'.:`~ ')
        full_html = ""
        
        for i, line in enumerate(lines):
            colored_line = ""
            for char in line:
                # Превращаем пробелы в HTML неразрывные пробелы, чтобы они не исчезали!
                if char == " ":
                    safe_char = "&nbsp;"
                else:
                    safe_char = html.escape(char)
                
                if char in background_chars:
                    colored_line += f"<span class='pink'>{safe_char}</span>"
                elif i <= 21:
                    colored_line += f"<span class='red'>{safe_char}</span>"
                else:
                    colored_line += f"<span class='green'>{safe_char}</span>"
            
            # Заменяем \n на <br> для гарантированного переноса
            full_html += colored_line + "<br>"
            
            if i % 2 == 0 or i == len(lines) - 1:
                # Рисуем внутри div с классом terminal-text
                placeholder.markdown(f"<div class='terminal-text' style='font-size: 13px; line-height: 1.15;'>{full_html}</div>", unsafe_allow_html=True)
                time.sleep(0.05)


def run_greeting():
    """Запуск всей цепочки поздравления"""
    animator = StreamlitAnimator()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Phase 1: Connection
    animator.type_text("═" * 80, "cyan", 0.005)
    animator.type_text("[INTERCEPTING ENCRYPTED HANDSHAKE...]", "cyan", 0.03)
    st.markdown("<br>", unsafe_allow_html=True)
    
    secret_payload = "CLASSIFIED_PAYLOAD: [MENTOR_APPRECIATION_PROTOCOL_V8.3_INITIATED]"
    animator.hex_reveal_effect(secret_payload, "cyan", 2.0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("[*] Handshake memory dump analyzed.", "cyan", 0.02)
    time.sleep(0.5)
    
    # Phase 2: Decryption
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("═" * 80, "yellow", 0.005)
    animator.type_text("[INITIATING BRUTEFORCE PROTOCOL]", "yellow", 0.03)
    animator.type_text("═" * 80, "yellow", 0.005)
    st.markdown("<br>", unsafe_allow_html=True)
    
    animator.progress_bar_effect(steps=20, label="Cracking Progress")
    time.sleep(0.5)
    animator.type_text("[+] ✓ PAYLOAD DECRYPTED", "green", 0.03)
    time.sleep(0.5)
    
    # Phase 3: Message
    st.markdown("<br>", unsafe_allow_html=True)
    animator.bruteforce_effect("С 8 МАРТА! 🌷", "pink", 2.0)
    st.markdown("<br>", unsafe_allow_html=True)
    
    animator.draw_ascii_flower()
    st.markdown("<br>", unsafe_allow_html=True)
    
    greeting_lines = [
        "Спасибо за то, что учите находить уязвимости в системах",
        "и выстраивать железобетонную защиту."
    ]
    for line in greeting_lines:
        animator.bruteforce_effect(line, "pink", 1.2)
        
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("Пусть в вашей жизни будет:", "cyan", 0.02)
    st.markdown("<br>", unsafe_allow_html=True)
    
    benefits = [
        ("[+] 0 дней простоев", "Zero-Days только в виде отдыха"),
        ("[+] 100% Uptime", "хорошего настроения"),
        ("[+] Никакого брутфорса", "нервной системы"),
        ("[+] DDoS защита от стресса", "с полной отдачей"),
        ("[+] Encryption для здоровья", "с максимальной приватностью")
    ]
    
    for prefix, suffix in benefits:
        animator.bruteforce_and_type(prefix, suffix, 0.8)
        
    time.sleep(1)
    st.markdown("<br>", unsafe_allow_html=True)
    closing_msg = "Вы — потрясающий наставник и крутой профессионал!"
    animator.bruteforce_effect(closing_msg, "pink", 2.0)
    
    # Phase 4: Closure
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("═" * 80, "cyan", 0.005)
    animator.progress_bar_effect(steps=15, label="Connection Closure")
    animator.type_text("[+] Connection securely closed.", "green", 0.04)
    animator.type_text("[+] Transmission complete. Safe travels!", "green", 0.04)
    animator.type_text("═" * 80, "cyan", 0.005)

# Блок для скрытия начального интерфейса после запуска
ui_container = st.empty()

with ui_container.container():
    st.markdown("<h3 style='text-align: center; color: #00ff00; font-family: monospace;'>[ TERMINAL ACCESS SECURED ]</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaaaaa; font-family: monospace;'>System stands by for authorization sequence.</p>", unsafe_allow_html=True)

    # Центрируем кнопку
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        start_button = st.button("INITIATE PROTOCOL")

if start_button:
    # Очищаем кнопку и заголовки, чтобы текст занимал всю ширину контейнера
    ui_container.empty()
    run_greeting()