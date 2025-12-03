import streamlit as st

st.set_page_config(layout="wide")


# ------------------ PAGE STATE ------------------
if "page" not in st.session_state:
  st.session_state.page = "question1"
if "pianoAccuracy" not in st.session_state:
    st.session_state.pianoAccuracy = 100

# Navigation callbacks

def go_q1():
    st.session_state.page = "question1"

def go_q2():
    st.session_state.page = "question2"

def go_q3():
    st.session_state.page = "question3"

def go_q4():
    st.session_state.page = "question4"

def go_q5():
    st.session_state.page = "question5"

def go_chordsIntroPage():
   st.session_state.page = "chordsIntroPage"

def go_Tq1():
    st.session_state.page = "questionT1"

def go_Tq2():
    st.session_state.page = "questionT2"

def go_Tq3():
    st.session_state.page = "questionT3"

def go_Tq4():
    st.session_state.page = "questionT4"

def go_Tq5():
    st.session_state.page = "questionT5"

def go_summary():
    st.session_state.page = "summary"

# ------------------ Definitions ------------------

def question1():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">I cannot read music at all</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">I can identify basic notes on the staff but read slowly</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">I can read music fluently at a moderate tempo</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">I can sight-read complex pieces at performance tempo</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ1Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 1")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following best describes your experience with reading musical notation?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q1Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q1Key")
    def printPage():
       print(st.session_state.page)

    if response and hasattr(response, "getQ1Response"):
        st.session_state.q1Score = response.getQ1Response   # <-- no parentheses
        go_q2()
        st.rerun()

def question2():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">How loud or soft the music is</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">The speed of the music</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">The emotional feeling of the music</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">The instrument being played</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ2Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 2")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    In music, what does the term "tempo" refer to?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q2Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q2Key")

    if response and hasattr(response, "getQ2Response"):
        st.session_state.q2Score = response.getQ2Response
        go_q3()
        st.rerun()

def question3():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">1 beat</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">1.5 beats</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">2 beats</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">3 beats</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ3Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 3")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
     How many beats does a dotted quarter note receive in 4/4 time?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q3Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q3Key")

    if response and hasattr(response, "getQ3Response"):
        st.session_state.q3Score = response.getQ3Response
        go_q4()
        st.rerun()

def question4():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">C - D - E - F - G - A - B - C</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">C - D - E♭ - F - G - A - B♭ - C</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">C - D - E - F# - G - A - B - C</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">C - D♭ - E♭ - F - G - A♭ - B♭ - C</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ4Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 4")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following is the correct order of notes in a C major scale?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q4Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q4Key")

    if response and hasattr(response, "getQ4Response"):
        st.session_state.q4Score = response.getQ4Response
        go_q5()
        st.rerun()

def question5():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">I've never practiced a musical instrument</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">I've tried learning but practice less than once a month</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">I practice 1-3 times per week</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">I practice daily or almost daily</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQ5Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("Question 5")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    Which of the following best describes your musical practice habits?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q5Key",
        html=html_code,
        js=js_code
    )

    response = component(key="q5Key")

    if response and hasattr(response, "getQ5Response"):
        st.session_state.q5Score = response.getQ5Response
        go_chordsIntroPage()
        st.rerun()

def chordsIntroPage():

    html_code = """
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 50vh;
            padding-top: 100px;  /* Adjust this to move text higher or lower */
            background-color: white;
            font-family: Arial, sans-serif;
        ">
            <div style="
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 0px;  /* Space between text and button */
            ">
                Chord Recognition Section
            </div>
        </div>




        <button id="submitBtn">Continue</button>
        <style>
        #submitBtn {
            padding: 12px 26px;
            border-radius: 8px;
            border: none;
            background: #2563eb;
            color: white;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        #submitBtn:hover {
            background: #1d4ed8;
        }
        </style>
    """

    # THIS IS THE CORRECT FORMAT — your previous JS was missing the wrapper function.
    js_code = """
export default function(component) {
    const { setTriggerValue } = component;
    const parent = component.parentElement;

    const submitBtn = parent.querySelector("#submitBtn");

    if (submitBtn) {
        submitBtn.addEventListener("click", () => {
            setTriggerValue("clicked", true);
        });
    }
}
"""

    component = st.components.v2.component(
        "testKey",
        html=html_code,
        js=js_code
    )

    response = component(key="testKey")

    if response and hasattr(response, "clicked"):
        go_Tq1()
        print("YoYO")        # <-- This will print in terminal
        st.rerun()           # not required but matches your style

def questionT1():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">C Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">C Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">A Minor</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">G Major</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT1Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 1")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: C - E - G?
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q1Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q1Tkey")

    if response and hasattr(response, "getQT1Response"):
        st.session_state.q1TScore = response.getQT1Response
        go_Tq2()
        st.rerun()

def questionT2():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">F Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">F Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">C Minor</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">D Minor</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT2Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 2")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: F - A♭ - C
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q2Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q2Tkey")

    if response and hasattr(response, "getQT2Response"):
        st.session_state.q2TScore = response.getQT2Response
        go_Tq3()
        st.rerun()

def questionT3():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">G Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">G Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">G7</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">C7</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT3Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 3")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: G - B - D - F
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q3Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q3Tkey")

    if response and hasattr(response, "getQT3Response"):
        st.session_state.q3TScore = response.getQT3Response
        go_Tq4()
        st.rerun()

def questionT4():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">E Major</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">A Minor</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">G Major</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">E Minor</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT4Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 4")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: E - G - B
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q4Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q4Tkey")

    if response and hasattr(response, "getQT4Response"):
        st.session_state.q4TScore = response.getQT4Response
        go_Tq5()
        st.rerun()

def questionT5():
    submitted = st.session_state.get("submitted_mcq", False)
    submitted_js = str(submitted).lower()

    html_code = """
<div id="root">
  <div class="pane">
    <div class="grid">
      <div class="option" id="opt1" style="background-color: #d9d9d9;">
        <div class="label">A</div>
        <div class="text">D Minor</div>
      </div>
      <div class="option" id="opt2" style="background-color: #d9d9d9;">
        <div class="label">B</div>
        <div class="text">D Major</div>
      </div>
      <div class="option" id="opt3" style="background-color: #d9d9d9;">
        <div class="label">C</div>
        <div class="text">A Major</div>
      </div>
      <div class="option" id="opt4" style="background-color: #d9d9d9;">
        <div class="label">D</div>
        <div class="text">G Major</div>
      </div>
    </div>

    <div class="actions">
      <button id="submitBtn" disabled>Submit</button>
    </div>
  </div>
</div>

<style>
:root {
  --block-bg: #d9d9d9;
  --block-hover: #c0c0c0;
  --block-selected: #a0a0a0;
  --pane-bg: #fafafa;
  --text-color: #111;
  --label-color: #333;
  --shadow-color: rgba(0,0,0,0.1);
}

.pane {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: var(--pane-bg);
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: min(800px, 100%);
}

.option {
  background: var(--block-bg);
  padding: 24px;
  border-radius: 12px;
  min-height: 140px;
  cursor: pointer;
  user-select: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px var(--shadow-color);
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.option:hover {
  background: var(--block-hover);
  transform: translateY(-2px);
}

.option.selected {
  background: var(--block-selected);
  transform: scale(1.02);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.option.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.label {
  font-weight: 700;
  font-size: 20px;
  color: var(--label-color);
  margin-bottom: 10px;
}

.text {
  font-size: 18px;
  line-height: 1.4;
  text-align:center;
}

.actions {
  margin-top: 30px;
  width: 100%;
  display: flex;
  justify-content: center;
}

#submitBtn {
  padding: 12px 26px;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #1d4ed8;
}

#submitBtn:disabled {
  background: #a1a1aa;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
"""

    js_code = f"""
export default function(component) {{
    const {{ setTriggerValue }} = component;
    const parent = component.parentElement;

    let submitted = {submitted_js};
    const opts = Array.from(parent.querySelectorAll(".option"));
    const submitBtn = parent.querySelector("#submitBtn");
    let selected = null;

    function updateSubmit() {{
        submitBtn.disabled = submitted || selected === null;
    }}

    function lockUI() {{
        opts.forEach(o => o.classList.add("disabled"));
        submitBtn.disabled = true;
    }}

    if (!submitted) {{
        opts.forEach((o, idx) => {{
            o.addEventListener("click", () => {{
                if (submitted) return;
                opts.forEach(x => x.classList.remove("selected"));
                o.classList.add("selected");
                selected = idx + 1;
                updateSubmit();
            }});
        }});

        submitBtn.addEventListener("click", () => {{
            if (selected === null || submitted) return;
            submitted = true;
            lockUI();
            setTriggerValue("getQT5Response", selected);
        }});
    }} else {{
        lockUI();
    }}

    updateSubmit();
}}
"""
    
    st.title("question 5")
    st.write("")
    st.markdown("""
    <h2 style="font-size:24px;">
    What is this Chord: D - F# - A
    </h2>
    """, unsafe_allow_html=True)
    st.write("")

    component = st.components.v2.component(
        "q5Tkey",
        html=html_code,
        js=js_code
    )

    response = component(key="q5Tkey")

    if response and hasattr(response, "getQT5Response"):
        st.session_state.q5TScore = response.getQT5Response
        go_summary()
        st.rerun()

def summary():
    import streamlit as st
    import streamlit.components.v1 as components  # For rendering HTML

    # -----------------------------
    # Answer Keys
    # -----------------------------
    answer_key_Q = {1:4, 2:2, 3:2, 4:1, 5:4}
    answer_key_T = {1:1, 2:2, 3:3, 4:4, 5:2}

    # -----------------------------
    # Scores (must exist in session_state beforehand)
    # -----------------------------
    quiz_correct = sum([
        st.session_state.get(f"q{i}Score") == answer_key_Q[i] for i in range(1,6)
    ])

    training_correct = sum([
        st.session_state.get(f"q{i}TScore") == answer_key_T[i] for i in range(1,6)
    ])

    piano_accuracy = st.session_state.get("pianoAccuracy", 0)         # % out of 100
    quiz_percent = (quiz_correct/5)*100                               # %
    training_percent = (training_correct/5)*100                       # %

    # -----------------------------
    # Overall Score Calculation
    # -----------------------------
    overall_score = round((quiz_percent + training_percent + piano_accuracy)/3)

    # Rank assignment
    if overall_score <= 40:
        rank = "Sound Explorer"
        next_rank = "Rising Virtuoso"
    elif overall_score <= 70:
        rank = "Rising Virtuoso"
        next_rank = "Stage Performer"
    elif overall_score <= 90:
        rank = "Stage Performer"
        next_rank = "Maestro"
    else:
        rank = "Maestro"
        next_rank = "—"

    # -----------------------------
    # UI Layout
    # -----------------------------
    st.markdown(f"""
    # **Overall Rank: {rank}**  
    *(Next rank: {next_rank})*
    """)

    # CATEGORY TABLE
    st.write("")
    st.markdown("### **Category Performance**")

    def progress_bar(value):
        st.progress(value/100)

    col1, col2, col3 = st.columns([2,1,2])

    with col1:
        st.write("**Category**")
        st.write("Musical Experience Quiz")
        st.write("Rhythm Training")
        st.write("Chord Recognition")
    with col2:
        st.write("**Score**")
        st.write(f"{quiz_correct} / 5")
        st.write(f"{piano_accuracy}% Accuracy")
        st.write(f"{training_correct} / 5 Correct")
    with col3:
        st.write("**Progress Bar**")
        progress_bar(quiz_percent)
        progress_bar(piano_accuracy)
        progress_bar(training_percent)

    # OVERALL RESULT
    st.markdown(f"""
    ### **Overall Score: {overall_score}% — {rank}**
    ---
    """)

    # -----------------------------
    # RANK TABLE - Improved with HTML
    # -----------------------------
    st.markdown("### **Rank Titles**")

    rank_colors = {
        "Sound Explorer": "#FFCDD2",
        "Rising Virtuoso": "#FFF9C4",
        "Stage Performer": "#BBDEFB",
        "Maestro": "#C8E6C9"
    }

    table_html = """
    <table style="width:100%; border-collapse: collapse;">
        <tr>
            <th style="border-bottom: 2px solid #000; padding:8px; text-align:left;">Score Range</th>
            <th style="border-bottom: 2px solid #000; padding:8px; text-align:left;">Rank Title</th>
            <th style="border-bottom: 2px solid #000; padding:8px; text-align:left;">Description</th>
        </tr>
    """

    rows = [
        ("0–40%", "Sound Explorer", "Just getting started — finding your rhythm."),
        ("41–70%", "Rising Virtuoso", "Learning fast and hitting the right notes."),
        ("71–90%", "Stage Performer", "Solid timing and sharp ears — keep rocking."),
        ("91–100%", "Maestro", "You've mastered this session — encore.")
    ]

    for score, title, desc in rows:
        color = rank_colors.get(title, "#FFFFFF")
        table_html += f"""
        <tr style="background-color:{color};">
            <td style="padding:8px;">{score}</td>
            <td style="padding:8px;"><b>{title}</b></td>
            <td style="padding:8px;">{desc}</td>
        </tr>
        """

    table_html += "</table>"

    # Render HTML table correctly
    components.html(table_html, height=250)



# ------------------ Logic ------------------
if st.session_state.page == "question1":
  question1()
elif st.session_state.page == "question2":
  question2()
elif st.session_state.page == "question3":
  question3()
elif st.session_state.page == "question4":
  question4()
elif st.session_state.page == "question5":
  question5()
elif st.session_state.page == "chordsIntroPage":
  chordsIntroPage()
elif st.session_state.page == "questionT1":
  questionT1()
elif st.session_state.page == "questionT2":
  questionT2()
elif st.session_state.page == "questionT3":
  questionT3()
elif st.session_state.page == "questionT4":
  questionT4()
elif st.session_state.page == "questionT5":
  questionT5()
elif st.session_state.page == "summary":
  summary()
