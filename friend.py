import streamlit as st
import time
import random
import html

# Настройка страницы
st.set_page_config(page_title="С 8 Марта!", page_icon="�", layout="wide")

# CSS для праздничной открытки
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top, #fff3f8 0%, #fffaf0 45%, #ffe6f2 100%);
        color: #4a2c3a;
    }
    .terminal-text {
        font-family: 'Segoe UI', 'Trebuchet MS', sans-serif;
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 0px;
        /* Оставляем переносы и выравниваем в центр */
        white-space: pre-wrap !important; 
        overflow-x: auto;
        text-align: center;
    }
    .green { color: #3d7b4f; }
    .pink { color: #d95a8f; }
    .cyan { color: #4a90a4; }
    .yellow { color: #c9a227; }
    .red { color: #c73d5b; }
    .white { color: #4a2c3a; }
    
    /* Стилизация кнопки Streamlit */
    div.stButton > button {
        background-color: #fff0f6;
        color: #b3476b;
        border: 1px solid #ff8bb5;
        font-family: 'Segoe UI', 'Trebuchet MS', sans-serif;
        font-weight: 600;
        width: 100%;
        margin-top: 20px;
        border-radius: 999px;
        padding: 0.6rem 1rem;
        box-shadow: 0 6px 16px rgba(217, 90, 143, 0.2);
    }
    div.stButton > button:hover {
        background-color: #ff8bb5;
        color: #ffffff;
        border: 1px solid #ff8bb5;
    }
</style>
""", unsafe_allow_html=True)

class StreamlitAnimator:
    """Аниматор, адаптированный под рендеринг Streamlit"""
    
    def __init__(self):
        self.glitch_chars = "01#$%&<>?{}[]/~X@!|"
        self.rus_glitch = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"

    def type_text(self, text: str, color_class: str = "pink", speed: float = 0.02):
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
            placeholder.markdown(f"<div class='terminal-text pink'>[*] {safe_label}: [{bar}] {int(percent * 100)}%</div>", unsafe_allow_html=True)
            time.sleep(0.05)

    def hex_reveal_effect(self, text: str, color_class: str = "pink", duration: float = 2.5):
        """Анимация волшебного раскрытия текста"""
        placeholder = st.empty()
        chars = list(text)
        sparkles = "✦✧★❀♡"

        iterations = int(duration / 0.08)
        if iterations < 1:
            iterations = 1

        for step in range(iterations):
            prob = (step / iterations) ** 1.5
            output_chars = []
            for char in chars:
                if char == " ":
                    output_chars.append(" ")
                elif random.random() < prob:
                    output_chars.append(char)
                else:
                    output_chars.append(random.choice(sparkles))

            safe_line = html.escape("".join(output_chars))
            placeholder.markdown(
                f"<div class='terminal-text {color_class}'>{safe_line}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.08)

        time.sleep(0.4)
        safe_text = html.escape(text)
        placeholder.markdown(
            f"<div class='terminal-text {color_class}'>✨ {safe_text}</div>",
            unsafe_allow_html=True
        )

    def bruteforce_effect(self, target: str, color_class: str = "pink", duration: float = 2.0):
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
        ascii_art = r'''    █████████      ████████      ██████   ██████                                       ███
   ███░░░░░███    ███░░░░███    ░░██████ ██████                                       ░███
  ███     ░░░    ░███   ░███     ░███░█████░███   ██████   ████████  ███████  ██████  ░███
 ░███            ░░████████      ░███░░███ ░███  ░░░░░███ ░░███░░███░░░███░  ░░░░░███ ░███
 ░███             ███░░░░███     ░███ ░░░  ░███   ███████  ░███ ░███  ░███    ███████ ░███
 ░░███     ███   ░███   ░███     ░███      ░███  ███░░███  ░███ ░███  ░███   ███░░███ ░░░ 
  ░░█████████    ░░████████      █████     █████░░████████ ░███████   ░███  ░░████████ ███
   ░░░░░░░░░      ░░░░░░░░      ░░░░░     ░░░░░  ░░░░░░░░  ░███░░░    ░░░    ░░░░░░░░ ░░░ 
                                                           ░███                           
                                                           █████                          
                                                           ░░░░░                           '''
        lines = ascii_art.split("\n")

        placeholder = st.empty()
        full_html = ""

        for i, line in enumerate(lines):
            safe_line = html.escape(line).replace(" ", "&nbsp;")
            color_class = "pink"
            full_html += f"<span class='{color_class}'>{safe_line}</span><br>"
            placeholder.markdown(
                f"<div class='terminal-text' style='font-size: 24px; line-height: 1.2; font-family: \"Courier New\", Courier, monospace; white-space: pre !important; text-align: left; display: inline-block;'>{full_html}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.05)


def run_greeting():
    """Запуск всей цепочки поздравления"""
    animator = StreamlitAnimator()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Phase 1: Подготовка
    animator.type_text("•" * 80, "pink", 0.005)
    animator.type_text("✨ Готовим весенний сюрприз...", "pink", 0.03)
    st.markdown("<br>", unsafe_allow_html=True)
    
    secret_payload = "Секретный букет: Поздравление для самой прекрасной подруги"
    animator.hex_reveal_effect(secret_payload, "pink", 2.0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("Сегодня — про тепло, улыбки и вдохновение.", "pink", 0.02)
    time.sleep(0.5)
    
    # Phase 2: Настроение
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("•" * 80, "pink", 0.005)
    animator.type_text("🌸 Собираем добрые пожелания", "pink", 0.03)
    animator.type_text("•" * 80, "pink", 0.005)
    st.markdown("<br>", unsafe_allow_html=True)
    
    animator.progress_bar_effect(steps=20, label="Наполняем открытку теплом")
    time.sleep(0.5)
    animator.type_text("Готово! Открываем поздравление 💌", "pink", 0.03)
    time.sleep(0.5)
    
    # Phase 3: Message
    st.markdown("<br>", unsafe_allow_html=True)
    animator.bruteforce_effect("С 8 Марта! 🌷", "pink", 2.0)
    st.markdown("<br>", unsafe_allow_html=True)

    greeting_lines = [
        "Желаю, чтобы ты всегда находилась в самом мощном ресурсном состоянии, а твой внутренний ребенок радовался каждому дню.",
        "Пусть все учебные (и не только) гештальты закрываются легко и без стресса, личные границы будут крепче любой брони, а уровень дофамина зашкаливает от крутых событий этой весной!",
        "Ты заслуживаешь только самого светлого, доброго и вдохновляющего каждый день 💖"
    ]
    for line in greeting_lines:
        animator.bruteforce_effect(line, "pink", 1.2)

    st.markdown("<br>", unsafe_allow_html=True)
    animator.draw_ascii_flower()
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Phase 4: Финальные слова
    st.markdown("<br>", unsafe_allow_html=True)
    animator.type_text("•" * 80, "pink", 0.005)
    animator.progress_bar_effect(steps=15, label="Дарим виртуальные объятия")
    animator.type_text("💗 Спасибо за твою красоту, ум и доброту!", "pink", 0.04)
    animator.type_text("✨ Пусть каждый день будет особенным.", "pink", 0.04)
    animator.type_text("•" * 80, "pink", 0.005)
    animator.type_text("                                                                        WinDustick" , "pink", 0.005)

# Блок для скрытия начального интерфейса после запуска
ui_container = st.empty()

with ui_container.container():
    st.markdown("<h2 style='text-align: center; color: #d95a8f; font-family: "
                "Segoe UI, Trebuchet MS, sans-serif;'>🌸 С 8 Марта! 🌸</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6b4a57; font-family: "
                "Segoe UI, Trebuchet MS, sans-serif;'>Нажми кнопку, чтобы открыть праздничную открытку.</p>", unsafe_allow_html=True)

    # Центрируем кнопку
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        start_button = st.button("Открыть поздравление")

if start_button:
    # Очищаем кнопку и заголовки, чтобы текст занимал всю ширину контейнера
    ui_container.empty()
    run_greeting()