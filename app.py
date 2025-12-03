import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="Full-Width Rectangle", layout="wide")
st.title("Rectangle Stretching Full Width of Page")

#============================BPM Select============================

# Initialize session state if not exists
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
if "bpm" not in st.session_state:
    st.session_state.bpm = 60  # default value

# Slider
st.session_state.bpm = st.slider(
    "Set the BPM",
    min_value=10,
    max_value=120,
    value=st.session_state.bpm,
    step=1,
    disabled=st.session_state.button_clicked
)



#============================Button============================
# Initialize session state variables if they don't exist
if "startGame" not in st.session_state:
    st.session_state.startGame = False
# Function to set startGame and disable button
def set_true():
    st.session_state.startGame = True
    st.session_state.button_clicked = True
st.button(
    "Set True",
    on_click=set_true,
    disabled=st.session_state.button_clicked  # disables after first click
)

#=========================Variables================================

noteImgQuarter = "♩"
heighOfTarget = 150  # Python variable
widthOfTarget = 70

startGame = st.session_state.startGame #Check if game has been started
start_pos = 0      # starting position in pixels from left
stop_pos = 200       # stopping position in pixels from left
distance = 500

bpm = 80
noteType = 1/4
stop = 1400
song = ["a", "a", "b", "g"]
notes = [
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "C"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.5,  "noteKey": "E"},
    
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.5,  "noteKey": "D"},
    
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.5,  "noteKey": "E"},
    
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "C"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "E"},    
    {"noteVal": 0.25, "noteKey": "E"},

    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 0.25, "noteKey": "E"},
    {"noteVal": 0.25, "noteKey": "D"},
    {"noteVal": 1,  "noteKey": "C"}
]

    
def populateNotes():
    for n in notes:
        n["noteShape"] = "♩"
populateNotes()

# Generate HTML for each note
note_divs = ""
for i, note in enumerate(notes):
    note_divs += f"""
    <div id="music-block-{i}" style="
        position:absolute;
        top:50%;
        right:0px;
        width:{widthOfTarget}px;
        height:{heighOfTarget}px;
        background:none;
        margin-top:-{heighOfTarget//2}px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:{heighOfTarget * 1.0}px;
        color:black;
    ">
        A
    </div>
    <div style="
        position:absolute;
        top:50%;
        left:0;
        width:8%;
        height:{heighOfTarget}px;     /* rectangle height */
        background:#e3dfde;
        margin-top:-{heighOfTarget//2}px;  /* vertically center */
    "></div>
    <div style="
        position:absolute;
        top:50%;
        right:0;
        width:8%;
        height:{heighOfTarget}px;     /* rectangle height */
        background:#e3dfde;
        margin-top:-{heighOfTarget//2}px;  /* vertically center */
    "></div>
    """



# JavaScript to animate all notes
animate_js = "<script>\n"

if st.session_state.startGame:
    animate_js += """
    // Define globals
    let startTime = performance.now();
    window.elapsedTime = 0;  // global variable you can use anywhere
    function updateTime() {
        const now = performance.now();
        window.elapsedTime = (now - startTime) / 1000;
        const timeElement = document.getElementById("elapsed-time");
        if (timeElement) {
            timeElement.innerText = "Time: " + window.elapsedTime.toFixed(2) + " s";
        }
        requestAnimationFrame(updateTime);
    }
    updateTime();
    """
    sumDistance = 0
    for i, note in enumerate(notes):
        animate_js += f"""
        const block{i} = document.getElementById("music-block-{i}");
        let rightPos{i} = 0;
        const stopRight{i} = {stop};
        block{i}.innerText = "{notes[i]["noteShape"]}";
        function animate{i}() {{
            if(rightPos{i} < stopRight{i}){{
                rightPos{i} = window.elapsedTime*{(st.session_state.bpm*distance)/(60*(4*noteType))}-{sumDistance};
                block{i}.style.right = rightPos{i} + "px";
                requestAnimationFrame(animate{i});
            }}
        }}
        animate{i}();
        """
        sumDistance+=(4*notes[i]["noteVal"])*distance

    durations = [n["noteVal"] for n in notes]
    durations_js = json.dumps(durations)

    noteKeys = [n["noteKey"] for n in notes]
    noteKeys_js = json.dumps(noteKeys)

    animate_js += f"""
    const durations = {durations_js};
    const noteKeys = {noteKeys_js};
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    const ctx = new AudioContext();

    // Function to get frequency from note
    function getNoteFreq(noteChar) {{
        const noteFreqMap = {{
            "C": 261.63,  // C4
            "D": 293.66,  // D4
            "E": 329.63,  // E4
            "F": 349.23,  // F4
            "G": 392.00,  // G4
            "A": 440.00,  // A4
            "B": 493.88   // B4
        }};
        const freq = noteFreqMap[noteChar.toUpperCase()];
        if (!freq) {{
            console.warn("Invalid note:", noteChar);
            return null;
        }}
        return freq;
    }}

    // Updated playPiano to accept frequency directly
    function playPiano(freq, duration) {{
        if (!freq) return;  // ignore invalid frequencies

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        const now = ctx.currentTime;

        // ADSR envelope
        const attack = 0.01;
        const decay = 0.15;
        const release = 0.5;

        gain.gain.setValueAtTime(0.0001, now);
        gain.gain.exponentialRampToValueAtTime(1.0, now + attack);
        gain.gain.exponentialRampToValueAtTime(0.6, now + decay);
        gain.gain.setValueAtTime(0.6, now + duration);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + duration + release);

        // Harmonic overtones
        const real = new Float32Array([0, 1.0, 0.6, 0.3, 0.15]);
        const imag = new Float32Array(real.length);
        const wave = ctx.createPeriodicWave(real, imag);
        osc.setPeriodicWave(wave);

        osc.type = "sine";
        osc.frequency.setValueAtTime(freq, now);
        osc.connect(gain).connect(ctx.destination);

        osc.start(now);
        osc.stop(now + duration + release + 0.1);
    }}




    window.addEventListener("keydown", (e) => {{
        if (e.code === "Space") {{
            for (let i = 0; i < {len(notes)}; i++) {{
                const block = document.getElementById("music-block-" + i);
                const blockRightPos = parseFloat(window.getComputedStyle(block).right);
                const blockLeftPos = parseFloat(window.getComputedStyle(block).right)+parseFloat(window.getComputedStyle(block).width);;

                const target = document.getElementById("target");
                const targetRightPos = parseFloat(window.getComputedStyle(target).right);
                const targetLeftPos = parseFloat(window.getComputedStyle(target).right)+parseFloat(window.getComputedStyle(target).width);;

                function getAccuracyAndColor() {{
                    const blockCenter = blockLeftPos - (blockLeftPos - blockRightPos) / 2;
                    const targetCenter = targetLeftPos - (targetLeftPos - targetRightPos) / 2;
                    const dist = blockCenter - targetCenter;
                    const absDist = Math.abs(dist);
                    let accuracy = 0;
                    let colour = "red";  // default if outside 100px

                    if (absDist <= 10) {{
                        accuracy = 1;
                        colour = "blue";
                    }} else if (absDist <= 50) {{
                        accuracy = 1 - (absDist - 10) * (0.1 / (50 - 10));
                        colour = "green";
                    }} else if (absDist <= 100) {{
                        accuracy = 0.9 - (absDist - 50) * (0.9 / (100 - 50));
                        colour = "yellow";
                    }}

                    // signed accuracy: positive if block is before target center, negative if after
                    accuracy = dist >= 0 ? accuracy : -accuracy;

                    return {{ accuracy: accuracy, colour: colour }};
                }}

                const result = getAccuracyAndColor();
                const accuracy = result.accuracy;
                const colour = result.colour;

                if (blockRightPos>=targetRightPos && blockLeftPos<=targetLeftPos && block.style.color == "black"){{
                    block.style.color = colour;
                    console.log("YIPEEE");
                    playPiano(getNoteFreq(noteKeys[i]) + 10*accuracy, ((4*durations[i]*{distance} - (blockRightPos-targetRightPos) - 70) / (4*durations[i]*{distance})) * ((60 * (4 * durations[i])) / {st.session_state.bpm}));
                }}
            }}
        }}
    }});
    """
scores = []

animate_js += "\n</script>"



html_code = f"""
<div id="container" style="
    position:relative;
    width:100%;
    height:{heighOfTarget + 50}px;   /* container height */
    margin:0;
    background:white;
    overflow:hidden;
">

    <!-- Rectangle stretching full width -->
    <div style="
        position:absolute;
        top:50%;
        left:0;
        width:100%;
        height:{heighOfTarget}px;     /* rectangle height */
        background:#f2ebeb;
        margin-top:-{heighOfTarget//2}px;  /* vertically center */
    "></div>
    <div div id="target" style="
        position:absolute;
        top:50%;
        right:800px;
        width:300px;
        height:{heighOfTarget}px;     /* rectangle height */
        background:#d8ebce;
        margin-top:-{heighOfTarget//2}px;  /* vertically center */
    "></div>
    <div style="
        position:absolute;
        top:50%;
        right:{800+150-2}px;
        width:4px;
        height:{heighOfTarget}px;     /* rectangle height */
        background:black;
        margin-top:-{heighOfTarget//2}px;  /* vertically center */
    "></div>
    {note_divs}
</div>
<!-- Add this somewhere in your HTML container -->
<div id="elapsed-time" style="
    position:absolute;
    top:10px;
    left:10px;
    color:black;
    font-size:18px;
    font-weight:bold;
    display:none;
">Time: 0.00 s</div>

{animate_js}
"""


# Remove the width argument so it can take full page width
components.html(html_code, height=200)

