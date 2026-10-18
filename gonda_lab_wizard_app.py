import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Gonda Brain Center - Lab Discovery Wizard",
    page_icon="🧠",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 15px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .core-badge {
        background-color: #FEF3C7;
        color: #92400E;
        font-size: 0.8rem;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 4px;
        border: 1px solid #F59E0B;
    }
    .aff-badge {
        background-color: #E0E7FF;
        color: #3730A3;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 Gonda Brain Center - Lab Match Wizard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Find your ideal research laboratory at Bar-Ilan University in 4 easy steps.</div>', unsafe_allow_html=True)

# Lab Data Directory
LABS = [
    {
        "pi": "Prof. Izhar Bar-Gad",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Neural Interfaces & Basal Ganglia Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Basal Ganglia Circuits", "Deep Brain Stimulation (DBS)", "Parkinsonism", "Movement Disorders", "Neural Signal Processing"],
        "tools": ["In Vivo Electrophysiology", "Closed-loop DBS", "LFP Dynamics", "Computational Modeling"],
        "models": ["Rodents / Primates"],
        "clinical": "Parkinson's & Movement Disorders, Tourette Syndrome",
        "summary": "Investigates basal ganglia circuit dynamics in movement/behavioral disorders and develops adaptive closed-loop DBS systems.",
        "pubs": "Handbook of Clinical Neurology: Neuromodulation (2026); Motor tics evoked by striatal disinhibition."
    },
    {
        "pi": "Prof. Elana Zion-Golumbic",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Human Brain Dynamics & Ecological Attention Lab",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Auditory Attention & Speech Tracking", "Natural Speech Processing", "ADHD Attention", "Ecological Cognition"],
        "tools": ["Human Neuroimaging & Electrophysiology", "High-density EEG", "MEG", "Virtual Reality", "Mobile EEG"],
        "models": ["Humans"],
        "clinical": "ADHD & Neurodevelopment",
        "summary": "Studies neural tracking of continuous natural speech, conversational turn-taking, and auditory selective attention in real-life environments.",
        "pubs": "Neural tracking of multi-speaker speech; VR classroom attention paradigms in ADHD."
    },
    {
        "pi": "Prof. Vadim Axelrod",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience & Consciousness Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Consciousness & Spontaneous Thought", "Face Perception", "Brain Decoding", "Machine Learning"],
        "tools": ["fMRI / MVPA", "Intracranial iEEG / ECoG", "MEG", "Non-invasive Neuromodulation"],
        "models": ["Humans"],
        "clinical": "Consciousness Disorders, Neuropsychiatry",
        "summary": "Decodes internal subjective experiences (daydreaming, mind-wandering), visual face perception, and humor using fMRI and intracranial iEEG.",
        "pubs": "Decoding subjective visual experience with intracranial recordings; Face processing in occipito-temporal cortex."
    },
    {
        "pi": "Prof. Moshe Bar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience & Predictive Brain Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Predictive Brain", "Top-Down Object Recognition", "Default Mode Network", "Digital Therapeutics", "Optical AI Decoding"],
        "tools": ["fMRI", "MEG", "Optical Speckle Pattern AI Decoding", "Computational Modeling"],
        "models": ["Humans"],
        "clinical": "Depression & Mood Disorders",
        "summary": "Explores proactive brain predictions, curiosity, Default Mode Network dynamics, and non-contact optical AI decoding of inner speech.",
        "pubs": "Predictive visual object recognition; Facilitating Thought Progression digital intervention for depression."
    },
    {
        "pi": "Prof. Michal Ben-Shachar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Neurobiology of Language & Reading Plasticity Lab",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Language Development", "Reading Plasticity", "Developmental Dyslexia", "Stuttering", "White Matter Tracts"],
        "tools": ["Diffusion MRI (dMRI/DTI)", "Automated Fiber Quantification (AFQ)", "fMRI"],
        "models": ["Humans"],
        "clinical": "Dyslexia & Speech Disorders",
        "summary": "Maps human language acquisition, reading pathways, and structural white matter tract changes in dyslexia and persistent stuttering.",
        "pubs": "White matter microstructural changes following reading intervention; Arcuate fasciculus tractography."
    },
    {
        "pi": "Prof. Ari Zivotofsky",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Ocular Motor & Visual Perception Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Oculomotor Biomarkers", "Eye Movements & Saccades", "Visual Perception", "Cognitive Control"],
        "tools": ["High-frequency Video-oculography", "Eye-tracking", "Psycholinguistic Paradigms"],
        "models": ["Humans"],
        "clinical": "Parkinson's & Movement Disorders, Motor Neurone Disease",
        "summary": "Investigates cognitive control of saccadic eye movements and develops oculomotor biomarkers for neurodegenerative and motor neurone diseases.",
        "pubs": "Oculomotor atypicalities in motor neurone disease: systematic review (Frontiers in Neuroscience, 2024)."
    },
    {
        "pi": "Prof. Hamutal Slovin",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Visual Processing & Artificial Vision Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Visual Cortex Dynamics", "Artificial Vision Prostheses", "Spiking Neural Networks", "Voltage-Sensitive Dye"],
        "tools": ["Voltage-Sensitive Dye Imaging (VSDI)", "In Vivo Electrophysiology", "Spiking Neural Networks (SNNs)"],
        "models": ["Rodents / Primates"],
        "clinical": "Blindness & Visual Prostheses",
        "summary": "Maps visual cortex population responses and builds cortical visual prostheses and biologically plausible neural network models.",
        "pubs": "Visual cortical population dynamics during perception; Cortical micro-stimulation for visual prostheses."
    },
    {
        "pi": "Prof. Adam Zaidel",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Multisensory Processing & Decision Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Multisensory Integration", "Spatial Orientation", "Bayesian Decision Models", "Self-Motion Perception"],
        "tools": ["3D MOOG Motion Simulator", "Human Neuroimaging & Electrophysiology", "Eye-tracking"],
        "models": ["Humans", "Rodents / Primates"],
        "clinical": "Vestibular & Balance Disorders",
        "summary": "Studies visual-vestibular-auditory multisensory calibration and Bayesian decision-making during spatial navigation and self-motion.",
        "pubs": "Bayesian multisensory integration in spatial orientation; Vestibular recalibration dynamics."
    },
    {
        "pi": "Dr. David Zada",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Social Brain & Behavior Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Sleep Genetics", "DNA Repair in Neurons", "Single-Cell Transcriptomics", "Chromosome Dynamics"],
        "tools": ["2-photon Imaging", "Single-cell RNA-seq", "CRISPR", "Live Chromosome Assays"],
        "models": ["Zebrafish / Transparent Glassfish"],
        "clinical": "ADHD & Neurodevelopment, Rare Genetic Disorders",
        "summary": "Investigates single-neuron sleep mechanisms, DNA damage repair (Parp1) during sleep, and genetic avatars of neurodevelopmental disorders.",
        "pubs": "Parp1 promotes sleep-dependent DNA repair in live neurons; Single-cell dynamics of sleep."
    },
    {
        "pi": "Prof. Dana Cohen",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Electrophysiology of Learning & Behavior Lab",
        "domain": "Computational Neuroscience & Neuro-AI",
        "subtopics": ["Machine Learning & Deep Learning", "Spike Sorting & Waveform Classification", "Cerebellar Networks", "Motor Learning"],
        "tools": ["Multi-electrode Arrays", "Deep Learning Transformers/CNNs", "In Vivo Electrophysiology"],
        "models": ["Rodents / Primates"],
        "clinical": "Parkinson's & Movement Disorders, Ataxia",
        "summary": "Applies deep convolutional and transformer networks to sort spike waveforms and decode motor learning in cerebellar circuits.",
        "pubs": "Transformer architectures for extracellular spike classification; Cerebellar network dynamics in motor adaptation."
    },
    {
        "pi": "Prof. Gal Yadid",
        "status": "Affiliated Faculty",
        "dept": "Department of Life Sciences",
        "lab": "Neuropsychopharmacology Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["PTSD & Memory Erasure", "Targeted Bio-nanoparticles", "Addiction Relapse", "Mesenchymal Stem Cells"],
        "tools": ["Bio-nanoparticles", "In Vivo Microdialysis", "Deep Brain Stimulation"],
        "models": ["Rodents / Primates"],
        "clinical": "PTSD & Trauma, Addiction",
        "summary": "Develops targeted nanoparticles crossing the blood-brain barrier for PTSD treatment and traumatic memory erasure.",
        "pubs": "Targeted nanoparticle delivery across the blood-brain barrier for PTSD treatment."
    },
    {
        "pi": "Prof. Eitan Okun",
        "status": "Affiliated Faculty",
        "dept": "Department of Life Sciences",
        "lab": "Neurodevelopment & Neurodegeneration Lab",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Microglial Neuroinflammation", "Alzheimer's Pathogenesis", "Toll-like Receptors", "Exercise Neuroprotection"],
        "tools": ["Transgenic AD Mouse Models", "Immunohistochemistry", "Microglial Profiling"],
        "models": ["Rodents / Primates"],
        "clinical": "Alzheimer's & Neurodegeneration, Down Syndrome",
        "summary": "Studies microglial TLR signaling pathways in Alzheimer's disease and neuroprotective benefits of physical exercise.",
        "pubs": "TLR pathways mediating neuroinflammation in cognitive decline; Exercise-induced neurogenesis."
    },
    {
        "pi": "Dr. Shahar Alon",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Engineering",
        "lab": "Spatial Genomics Group",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Spatial Transcriptomics", "Expansion Microscopy", "In Situ Sequencing", "RNA Editing"],
        "tools": ["Expansion Sequencing (ExSeq)", "High-throughput Fluorescence Microscopy", "Spatial Genomics"],
        "models": ["Rodents / Primates", "Drosophila / Invertebrates"],
        "clinical": "Alzheimer's & Neurodegeneration, Cancer",
        "summary": "Pioneers spatial genomics and in situ RNA sequencing to map gene expression directly within intact brain tissue.",
        "pubs": "Expansion sequencing: Spatially resolved RNA sequencing in intact tissue."
    },
    {
        "pi": "Prof. Yuri Rassovsky",
        "status": "Affiliated Faculty",
        "dept": "Department of Psychology",
        "lab": "Clinical Neuropsychology & VR Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Executive Control & Neuro-rehabilitation", "Virtual Reality TBI Assessment", "Cognitive Enhancement"],
        "tools": ["Virtual Reality", "Psychoneuropsychological Batteries", "Autonomic Psychophysiology"],
        "models": ["Humans"],
        "clinical": "PTSD & Trauma, TBI, Schizophrenia",
        "summary": "Uses immersive virtual reality cognitive rehabilitation protocols to improve real-world functional outcomes in TBI and psychiatric patients.",
        "pubs": "VR-based cognitive rehabilitation improving functional outcomes in clinical TBI."
    },
    {
        "pi": "Prof. Sharon Armon-Lotem & Prof. Natalia Meir",
        "status": "Affiliated Faculty",
        "dept": "Department of English Literature & Linguistics",
        "lab": "Bilingualism & Developmental Language Disorders Lab",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Language Development", "Eye-Tracking & Psycholinguistic Paradigms", "Bilingual Reading", "Developmental Language Disorder"],
        "tools": ["Eye-tracking", "Psycholinguistic Paradigms", "Linguistic Testing"],
        "models": ["Humans"],
        "clinical": "Dyslexia & Speech Disorders",
        "summary": "Uses high-speed eye-tracking to study real-time sentence processing, bilingual reading, and language impairment in children.",
        "pubs": "Eye-tracking indicators of real-time sentence processing in bilingual children with DLD."
    }
]

# Initialize Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Progress Bar
if st.session_state.step <= 4:
    progress_val = max(0.0, min(1.0, (st.session_state.step - 1) / 4.0))
    st.progress(progress_val)
    st.caption(f"Step {st.session_state.step} of 4")
else:
    st.progress(1.0)
    st.caption("Matches Complete! 🎯")

# --- STEP 1: DOMAIN ---
if st.session_state.step == 1:
    st.subheader("Step 1: Which broad neuroscience domain excites you most?")
    domain_choice = st.radio(
        "Select one primary field:",
        [
            "Cognitive & Behavioral Neuroscience (Human cognition, attention, speech, language, memory, consciousness)",
            "Systems & Circuit Neuroscience (Neural circuits, sensory processing, motor control, basal ganglia, visual/olfactory systems)",
            "Computational Neuroscience & Neuro-AI (Deep learning, machine learning, signal processing, mathematical neuroscience)",
            "Cellular, Molecular & Genetic Neuroscience (Sleep genetics, DNA repair, spatial transcriptomics, neuroinflammation, neurogenetics)"
        ]
    )
    
    if st.button("Next ➔", type="primary"):
        clean_domain = domain_choice.split(" (")[0]
        st.session_state.answers['domain'] = clean_domain
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: SUBTOPIC ---
elif st.session_state.step == 2:
    selected_domain = st.session_state.answers.get('domain', '')
    st.subheader(f"Step 2: What specific topics or methods within {selected_domain} interest you?")
    
    topic_options = []
    if "Cognitive" in selected_domain:
        topic_options = [
            "Auditory Attention & Speech Tracking in Noise ('Cocktail Party Effect')",
            "Consciousness, Mind-Wandering & Spontaneous Thought Decoding",
            "Top-Down Predictive Brain & Digital Therapeutics for Depression",
            "Language Development, Reading Plasticity & Dyslexia Pathways",
            "Eye-Tracking & Oculomotor Control Biomarkers",
            "Executive Control, Neuro-rehabilitation & Virtual Reality"
        ]
    elif "Systems" in selected_domain:
        topic_options = [
            "Basal Ganglia Circuits, Deep Brain Stimulation (DBS) & Parkinsonism",
            "Visual Cortical Population Dynamics & Artificial Vision Prostheses",
            "Olfactory Coding & Interhemispheric Synchronization",
            "Multisensory Integration (Visual/Vestibular/Auditory) & Self-Motion",
            "Cellular Biophysics & Patch-clamp of Cortical/Subcortical Micro-circuits"
        ]
    elif "Computational" in selected_domain:
        topic_options = [
            "Neural Signal Processing & Time-Series Analysis (Filtering, Wavelets, LFP/EEG Dynamics)",
            "Machine Learning, Deep Learning, Transformers & LLMs / NLP",
            "Advanced Statistics, Data Science & Multivariate Dimensionality Reduction",
            "Biophysical, Spiking Neural Network (SNN) & Circuit Modeling",
            "Network Science, Graph Theory, Connectomics & Spatial Data Analysis"
        ]
    else: # Cellular/Molecular
        topic_options = [
            "Sleep-dependent Chromosome Dynamics & Single-Neuron DNA Repair",
            "Microglial Neuroinflammation & Alzheimer's Pathogenesis",
            "Spatial Transcriptomics, Expansion Microscopy & In Situ Sequencing",
            "Social Behavior Circuits & Collective Motion in Transparent Fish",
            "Targeted Bio-nanoparticle BBB Drug Delivery for PTSD & Memory Erasure"
        ]
        
    selected_topics = st.multiselect("Select 1 to 3 specific sub-topics:", topic_options)
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Next ➔", type="primary"):
            st.session_state.answers['subtopics'] = selected_topics
            st.session_state.step = 3
            st.rerun()

# --- STEP 3: TOOLS & METHODOLOGY ---
elif st.session_state.step == 3:
    st.subheader("Step 3: Which experimental or computational toolkits do you want to work with?")
    tool_options = st.multiselect(
        "Select your preferred methodologies:",
        [
            "Human Neuroimaging & Electrophysiology (fMRI, MEG, High-density EEG, Mobile EEG)",
            "Intracranial Recordings & Clinical Patients (iEEG / ECoG, DBS patients, Neurosurgery)",
            "Non-invasive Neuromodulation & VR (tDCS, tACS, Virtual Reality Cafés/Classrooms)",
            "In Vivo Electrophysiology & Optical Imaging (Multi-electrode arrays, 2-photon imaging, VSDI, Optogenetics)",
            "Cellular, Molecular & Genetics (Patch-clamp, Single-cell RNA-seq, CRISPR, Spatial Genomics, Bio-nanoparticles)",
            "Machine Learning & Computational Modeling (Deep learning, Transformers, Spiking Neural Networks, Bayesian models, Physics-based nets)"
        ]
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Next ➔", type="primary"):
            st.session_state.answers['tools'] = tool_options
            st.session_state.step = 4
            st.rerun()

# --- STEP 4: MODEL SYSTEMS & CLINICAL FOCUS ---
elif st.session_state.step == 4:
    st.subheader("Step 4: Do you have a preferred model system or clinical application?")
    
    col_a, col_b = st.columns(2)
    with col_a:
        model_pref = st.radio(
            "Preferred Model System:",
            ["No preference / Open to all", "Humans", "Rodents / Primates", "Zebrafish / Transparent Glassfish", "Drosophila / Invertebrates"]
        )
    with col_b:
        clinical_pref = st.multiselect(
            "Clinical / Disease Focus (optional):",
            ["Parkinson's & Movement Disorders", "Alzheimer's & Neurodegeneration", "ADHD & Neurodevelopment", "Depression & Mood Disorders", "PTSD & Trauma", "Dyslexia & Speech Disorders", "Blindness & Visual Prostheses"]
        )
        
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("Get My Matches! 🎯", type="primary"):
            st.session_state.answers['model'] = model_pref
            st.session_state.answers['clinical'] = clinical_pref
            st.session_state.step = 5
            st.rerun()

# --- STEP 5: RESULTS PAGE ---
elif st.session_state.step == 5:
    st.subheader("🎯 Your Personalized Gonda Lab Matches")
    st.write("Based on your preferences, here are the top laboratories at Bar-Ilan University tailored for you:")
    
    ans = st.session_state.answers
    
    # Calculate match scores for all labs
    scored_labs = []
    for lab in LABS:
        score = 0
        reasons = []
        
        # Domain match
        if lab['domain'] == ans.get('domain'):
            score += 30
            reasons.append(f"Domain match: **{lab['domain']}**")
            
        # Subtopic match
        for user_sub in ans.get('subtopics', []):
            words = [w.strip() for w in user_sub.replace("(", " ").replace(")", " ").replace("/", " ").split() if len(w.strip()) > 3]
            for lab_sub in lab.get('subtopics', []):
                if any(w.lower() in lab_sub.lower() for w in words):
                    score += 15
                    reasons.append(f"Matching topic: {lab_sub}")
                    break
                    
        # Tool match
        for user_tool in ans.get('tools', []):
            words = [w.strip() for w in user_tool.replace("(", " ").replace(")", " ").replace("/", " ").split() if len(w.strip()) > 3]
            for lab_tool in lab.get('tools', []):
                if any(w.lower() in lab_tool.lower() for w in words):
                    score += 12
                    reasons.append(f"Matching methodology: {lab_tool}")
                    break
                    
        # Model match
        user_model = ans.get('model', '')
        if user_model != "No preference / Open to all":
            for lab_model in lab.get('models', []):
                if user_model.split()[0].lower() in lab_model.lower():
                    score += 10
                    reasons.append(f"Model system: {lab_model}")
                    break
                    
        # Clinical match
        for user_clin in ans.get('clinical', []):
            clin_words = [w.strip() for w in user_clin.split() if len(w.strip()) > 3]
            if any(w.lower() in lab.get('clinical', '').lower() for w in clin_words):
                score += 10
                reasons.append(f"Clinical focus: {user_clin}")
                
        # CORE FACULTY PRIORITY BOOST (1.4x multiplier)
        if lab['status'] == 'Core Faculty':
            score *= 1.4
            
        scored_labs.append({
            "lab": lab,
            "score": round(score, 1),
            "reasons": list(set(reasons))
        })
        
    # Sort by score descending
    scored_labs.sort(key=lambda x: x['score'], reverse=True)
    top_5 = scored_labs[:5]
    
    # Display Top 5 Cards
    for idx, item in enumerate(top_5, 1):
        lab = item['lab']
        is_core = lab['status'] == "Core Faculty"
        badge_html = '<span class="core-badge">★ CORE GONDA FACULTY</span>' if is_core else '<span class="aff-badge">AFFILIATED FACULTY</span>'
        
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h3 style="margin: 0; color: #1E3A8A;">#{idx}. {lab['pi']}</h3>
                {badge_html}
            </div>
            <p style="font-weight: 600; color: #374151; margin-bottom: 6px;">{lab['lab']} — <em>{lab['dept']}</em></p>
            <p style="color: #4B5563; font-size: 0.95rem; margin-bottom: 12px;">{lab['summary']}</p>
            <p style="font-size: 0.9rem; margin-bottom: 4px;"><strong>🧪 Primary Tools:</strong> {', '.join(lab['tools'])}</p>
            <p style="font-size: 0.9rem; margin-bottom: 4px;"><strong>🐭 Model Systems:</strong> {', '.join(lab['models'])}</p>
            <p style="font-size: 0.88rem; color: #1F2937; margin-bottom: 0;"><strong>📚 Recent Work:</strong> {lab['pubs']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Start Over", type="secondary"):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()
