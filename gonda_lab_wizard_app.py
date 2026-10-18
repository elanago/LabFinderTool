import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Gonda Brain Center Lab Discovery Wizard",
    page_icon="🧠",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .core-badge {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 5px 12px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #F59E0B;
        display: inline-block;
    }
    .aff-badge {
        background-color: #F3F4F6;
        color: #374151;
        padding: 5px 12px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid #D1D5DB;
        display: inline-block;
    }
    .card {
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 18px;
        background-color: #FFFFFF;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 Gonda Brain Center Lab Discovery Wizard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Find the Bar-Ilan neuroscience laboratories that best match your research interests.</div>', unsafe_allow_html=True)

# Complete Gonda Labs Database with Strict Mappings
LABS = [
    # CORE FACULTY
    {
        "pi": "Prof. Izhar Bar-Gad",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Center Director)",
        "lab": "Neural Interfaces Laboratory / Basal Ganglia & Neuromodulation",
        "domain": "Systems & Circuit Neuroscience",
        "methods": ["In Vivo Multi-electrode Recording", "Closed-loop DBS Neuromodulation", "Signal Processing & LFP Analysis", "Biophysical & Circuit Simulations"],
        "topics": ["Basal Ganglia & Movement Disorders", "Deep Brain Stimulation (DBS)", "Tourette Syndrome & Motor Tics", "Parkinsonism & Cortico-striatal Loops"],
        "models": ["Rodents", "Primates"],
        "clinical": ["Parkinson's & Movement Disorders", "Tourette Syndrome & Tics"],
        "summary": "Investigates cortico-striatal circuits and develops adaptive closed-loop DBS algorithms for movement and neuropsychiatric disorders.",
        "pubs": "Handbook of Clinical Neurology: Neuromodulation in Basal Ganglia Disorders (2026); Motor tics evoked by striatal disinhibition (Frontiers)."
    },
    {
        "pi": "Prof. Elana Zion-Golumbic",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Undergrad Program Head)",
        "lab": "Human Brain Dynamics and Real-Life Ecological Attention Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["Human Neuroimaging (EEG / MEG / Mobile EEG)", "Virtual Reality (VR) Ecological Paradigms", "Auditory Psychophysics & Eye-Tracking", "Neural Signal Processing & TRF Modeling"],
        "topics": ["Auditory Selective Attention ('Cocktail Party Effect')", "Natural Speech Tracking & Conversational Dynamics", "ADHD & Sensitivity to Auditory Distractions", "Neuroeducation & Mobile EEG"],
        "models": ["Humans"],
        "clinical": ["ADHD & Neurodevelopmental Attention Disorders"],
        "summary": "Studies dynamic speech tracking, selective attention in noisy environments, and auditory distraction using MEG, mobile EEG, and VR.",
        "pubs": "Toward precision EEG: assessing individual ERP reliability (Frontiers, 2026); Selective attention in Virtual Classroom (eLife, 2024)."
    },
    {
        "pi": "Prof. Dana Cohen",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Grad Advisor)",
        "lab": "Electrophysiology of Learning and Behavior Laboratory",
        "domain": "Computational Neuroscience & Neuro-AI",
        "methods": ["Machine Learning & Deep Learning (CNNs / Transformers)", "In Vivo Multi-channel Electrophysiology", "Spike Sorting & Waveform Classification", "Optical Cerebellar Imaging"],
        "topics": ["Deep Learning Strategy for Cell-Type Identification", "Motor Skill Acquisition & Population Dynamics", "Cerebellar & Basal Ganglia Micro-circuits"],
        "models": ["Rodents", "Cross-species Datasets"],
        "clinical": ["Motor Learning & Ataxia"],
        "summary": "Uses deep neural networks (CNNs/Transformers) to classify electrophysiological neuronal cell types and investigates motor population dynamics.",
        "pubs": "A deep-learning strategy to identify cell types across species from high-density extracellular recordings (Nature Methods, 2024)."
    },
    {
        "pi": "Prof. Vadim Axelrod",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience and Consciousness Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["Functional MRI (fMRI / MVPA Decoding)", "Intracranial EEG (iEEG / ECoG) in Neurosurgery Cohorts", "Magnetoencephalography (MEG)", "Non-invasive Brain Stimulation (tDCS/tACS)"],
        "topics": ["Mind-Wandering, Daydreaming & Spontaneous Thought Decoding", "Consciousness & Subjective Internal Experiences", "Face Perception & Occipito-temporal Cortex"],
        "models": ["Humans"],
        "clinical": ["Neurosurgical & Psychiatric Patient Cohorts"],
        "summary": "Combines human intracranial ECoG and machine learning decoding to map spontaneous thought dynamics, face perception, and meta-awareness.",
        "pubs": "Intracranial decoding of spontaneous thought (Cerebral Cortex, 2025); tDCS modulation of spontaneous self-directed thoughts (PNAS)."
    },
    {
        "pi": "Prof. Moshe Bar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["Combined fMRI & Magnetoencephalography (MEG)", "Digital Therapeutics & Gamified Interventions", "Predictive Computational Modeling", "AI-Driven Remote Optical Speckle Analysis"],
        "topics": ["Top-Down Predictive Visual Object Recognition", "Default Mode Network (DMN) & Associative Processing", "Facilitating Thought Progression (FTP) for Depression", "Curiosity & Architectural Aesthetics"],
        "models": ["Humans"],
        "clinical": ["Depression, Anxiety & Mood Disorders"],
        "summary": "Explores top-down predictive processing and develops digital health applications (Facilitating Thought Progression) for clinical depression.",
        "pubs": "Facilitating Thought Progression via a gamified app for depression (Behavior Therapy, 2026); Thought Dynamics and Mood Disorders (2026)."
    },
    {
        "pi": "Prof. Michal Ben-Shachar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Interdisciplinary Unit Head)",
        "lab": "Neurobiology of Language and Reading Plasticity Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["Diffusion MRI (dMRI / DTI / CHARMED / HARDI)", "Automated Fiber Quantification (AFQ / Tractography)", "Functional MRI (fMRI)", "Psycholinguistics & Reading Testing"],
        "topics": ["Language Development & Neural Plasticity", "Developmental Dyslexia & Reading Pathways (Arcuate Fasciculus)", "Persistent Stuttering & Motor Speech Control", "Cerebellar Contributions to Written Word Production"],
        "models": ["Humans"],
        "clinical": ["Dyslexia, Speech Disorders & Preterm Birth"],
        "summary": "Uses diffusion MRI tractography to examine white matter pathways (arcuate fasciculus) in reading, language acquisition, and developmental stuttering.",
        "pubs": "White matter correlates of sensorimotor synchronization in persistent developmental stuttering (J. Commun. Disord., 2025)."
    },
    {
        "pi": "Prof. Rafi Haddad",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Learning, Decision-Making, Olfaction & Neural Circuits Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "methods": ["In Vivo Multi-channel Electrophysiology", "Optogenetics & Cell-Type Manipulation", "Viral Circuit Tracing (Rabies / AAV)", "Optical Odor Imaging"],
        "topics": ["Olfactory Neural Coding & Spatial Odor Maps", "Piriform Cortex Micro-circuits & Feedforward Inhibition", "Interhemispheric Synchronization & Odor Perceptual Unity", "Perceptual Decision-Making"],
        "models": ["Rodents"],
        "clinical": ["Sensory & Olfactory Processing Deficits"],
        "summary": "Investigates interhemispheric synchronization and feedforward inhibitory micro-circuits in the primary olfactory cortex.",
        "pubs": "Bilateral odor coding and interhemispheric synchronization in piriform cortex (2025)."
    },
    {
        "pi": "Prof. Hamutal Slovin",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Visual Processing and Artificial Vision Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "methods": ["Wide-field Voltage-Sensitive Dye Imaging (VSDI)", "Multi-electrode Array Electrophysiology", "Neuromorphic Spiking Neural Networks (SNNs)", "Electrical Microstimulation & Visual Psychophysics"],
        "topics": ["Visual Cortical Population Dynamics & V1 Coherence", "Cortical Visual Prostheses & Artificial Vision", "Brain Reading & Image Reconstruction", "Microsaccades & Foveal Synchronization"],
        "models": ["Primates", "Rodents"],
        "clinical": ["Blindness & Visual Prostheses"],
        "summary": "Uses VSDI optical imaging and neuromorphic spiking neural networks to study visual cortical dynamics and artificial vision prostheses.",
        "pubs": "Effects of Microsaccades in Primary Visual Cortex: Increased Synchronization in Fovea (J. Neurosci., 2025)."
    },
    {
        "pi": "Dr. David Zada",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Social Brain and Behavior Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "methods": ["In Vivo 2-Photon Whole-Brain Imaging", "Multi-animal Visual Virtual Reality (VR)", "CRISPR & Single-cell RNA-seq Transcriptomics", "Parp1 & Chromosome Dynamics Assays"],
        "topics": ["Single-Neuron Sleep Function & DNA Repair (Parp1)", "Social Motion Perception & Collective Behavior", "Transparent Micro Glassfish (Danionella cerebrum) Model", "Genetic Avatars for Rare Neurodevelopmental Disorders"],
        "models": ["Danionella cerebrum Glassfish", "Zebrafish"],
        "clinical": ["Neurodevelopmental Social Disorders & DNA Damage"],
        "summary": "Maps whole-brain social circuits in transparent micro glassfish and investigates sleep-dependent chromosome dynamics and DNA repair.",
        "pubs": "Convergent thyroid-ATPase interactions regulate collective behavior in Danionella (Cell Reports, 2026)."
    },
    {
        "pi": "Prof. Adam Zaidel",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Multisensory Processing Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "methods": ["3D MOOG Multisensory Motion Simulator", "Primate & Human Electrophysiology", "Bayesian Optimal Decision Modeling", "Human Visual-Vestibular Psychophysics"],
        "topics": ["Visual-Vestibular-Auditory Multisensory Integration", "Spatial Orientation & Self-Motion Perception", "Adaptive Multisensory Recalibration", "Atypical Sensory Weighting in Autism"],
        "models": ["Humans", "Primates", "Rodents"],
        "clinical": ["Parkinson's Disease & Autism Spectrum Disorder"],
        "summary": "Combines Israel's 3D MOOG motion simulator with single-unit electrophysiology and Bayesian modeling to study multisensory orientation.",
        "pubs": "Contrary neuronal recalibration in different multisensory cortical areas (eLife)."
    },
    {
        "pi": "Prof. Ari Zivotofsky",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Ocular Motor and Visual Perception Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["High-frequency Video-Oculography & Eye-Tracking", "Computerized Visual Psychophysics", "Gait & Unintentional Synchronization Analysis"],
        "topics": ["Oculomotor Control (Saccades & Smooth Pursuit)", "Eye-Tracking Biomarkers for Motor Neurone Disease", "Cognitive vs. Reflexive Saccadic Control", "Neuro-ethics & Human Performance"],
        "models": ["Humans"],
        "clinical": ["Motor Neurone Disease, Early Parkinson's / Alzheimer's"],
        "summary": "Develops non-invasive video-oculography eye-tracking biomarkers for early detection of neurodegenerative and motor neurone diseases.",
        "pubs": "Oculomotor atypicalities in motor neurone disease: a systematic review (Frontiers in Neuroscience, 2024)."
    },

    # AFFILIATED FACULTY
    {
        "pi": "Prof. Alon Korngreen",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Cellular Neurophysiology Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "methods": ["Whole-cell Patch-clamp Electrophysiology", "2-Photon Calcium Imaging", "Hodgkin-Huxley Biophysical Modeling", "Optogenetics"],
        "topics": ["Subthalamic Nucleus & Globus Pallidus Biophysics", "Ion Channel Kinetics & Synaptic Plasticity", "Basal Ganglia Micro-circuit Dynamics"],
        "models": ["Rodents"],
        "clinical": ["Parkinson's Disease"],
        "summary": "Investigates cellular biophysics and synaptic plasticity of basal ganglia micro-circuits using patch-clamp and computational modeling.",
        "pubs": "Biophysics of Subthalamic Nucleus and basal ganglia plasticity."
    },
    {
        "pi": "Prof. Lior Appelbaum",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Molecular & Developmental Neuroscience Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "methods": ["Live 3D Confocal & 2-Photon Imaging", "Transgenic Zebrafish Genetics", "High-throughput Behavioral Sleep Tracking", "CRISPR Gene Editing"],
        "topics": ["Sleep Regulation & Synaptic Plasticity", "Chromosome Dynamics & Single-Neuron DNA Repair", "Genetic Neurodevelopmental Disorders"],
        "models": ["Zebrafish"],
        "clinical": ["MCT8 Deficiency & Neurodevelopmental Disorders"],
        "summary": "Uses transgenic zebrafish to study genetic and cellular regulation of sleep, chromosome dynamics, and synaptic maintenance.",
        "pubs": "Parp1 promotes sleep, which enhances DNA repair in neurons (Molecular Cell)."
    },
    {
        "pi": "Prof. Eitan Okun",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Neurodevelopment & Neurodegeneration Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "methods": ["Transgenic Rodent Disease Models", "Immunohistochemistry & Microglial Imaging", "Behavioral Mazes & Cognitive Testing", "Cytokine & Molecular Profiling"],
        "topics": ["Microglial Neuroinflammation", "Alzheimer's Disease Pathogenesis", "Toll-like Receptors (TLRs) in Cognition", "Exercise-Induced Neurogenesis"],
        "models": ["Rodents"],
        "clinical": ["Alzheimer's Disease & Down Syndrome"],
        "summary": "Studies microglial neuroinflammation, TLR pathways, and exercise-induced neurogenesis in Alzheimer's disease models.",
        "pubs": "TLR pathways mediating neuroinflammation in cognitive decline."
    },
    {
        "pi": "Dr. Shahar Alon",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Engineering",
        "lab": "Spatial Genomics Group",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "methods": ["Expansion Sequencing (ExSeq)", "Spatial Transcriptomics & In Situ Sequencing", "High-throughput Fluorescence Microscopy", "Single-Cell Spatial Algorithms"],
        "topics": ["Spatial Transcriptomics of Neural Circuits", "In Situ RNA Sequencing & Expansion Microscopy", "RNA Editing in Cephalopods & Mammals"],
        "models": ["Mammals", "Cephalopods"],
        "clinical": ["Neurodegenerative Spatial Genomics"],
        "summary": "Develops expansion sequencing and spatial transcriptomics to map nanoscale gene expression in neural circuits.",
        "pubs": "Trade-off between transcriptome plasticity and genome evolution (Cell)."
    },
    {
        "pi": "Prof. Gal Yadid",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Neuropsychopharmacology Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "methods": ["Targeted Bio-nanoparticle Delivery", "In Vivo Microdialysis", "Operant Self-Administration Paradigms", "Deep Brain Electrical Stimulation"],
        "topics": ["PTSD & Traumatic Memory Erasure", "Addiction Memory Remodeling", "Nanoparticle Blood-Brain Barrier (BBB) Crossing"],
        "models": ["Rodents"],
        "clinical": ["PTSD & Trauma", "Substance Addiction"],
        "summary": "Develops targeted nanoparticle drug delivery across the blood-brain barrier for PTSD memory erasure and addiction treatment.",
        "pubs": "Targeted nanoparticle delivery across the blood-brain barrier for PTSD treatment."
    },
    {
        "pi": "Prof. Avi Goldstein",
        "status": "Affiliated Faculty",
        "dept": "Department of Psychology",
        "lab": "Electromagnetic Brain Imaging Unit",
        "domain": "Cognitive & Behavioral Neuroscience",
        "methods": ["248-channel Whole-head MEG", "High-density EEG", "MEG Signal Processing & Source Localization"],
        "topics": ["Executive Control Oscillations", "Language Processing in Autism", "Auditory Neural Dynamics"],
        "models": ["Humans"],
        "clinical": ["Autism Spectrum Disorder & Cognitive Impairments"],
        "summary": "Operates the 248-channel MEG system investigating neural oscillations during executive control and language perception.",
        "pubs": "MEG neural dynamics of cognitive control and executive functioning."
    },
    {
        "pi": "Prof. Ido Kanter",
        "status": "Affiliated Faculty",
        "dept": "Department of Physics",
        "lab": "Complex Systems and Computational Neuroscience Laboratory",
        "domain": "Computational Neuroscience & Neuro-AI",
        "methods": ["Biophysical Neural Simulations", "Non-linear Dynamics & Physics Modeling", "Mathematical Network Science"],
        "topics": ["Ultrafast Biological Learning Rules", "Dendritic Computing Beyond Backprop", "Physics-Inspired Neural Architectures"],
        "models": ["Computational Models", "In Vitro Neuronal Cultures"],
        "clinical": ["AI Architecture Optimization & Epilepsy"],
        "summary": "Discovers ultrafast biological learning rules in individual dendrites that inspire non-backprop artificial intelligence.",
        "pubs": "Dendritic learning rules outperforming traditional deep neural network training."
    }
]

# Initialize Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Progress Bar Math safely bounded between 0.0 and 1.0
current_step = st.session_state.step
progress_val = min(1.0, max(0.0, (current_step - 1) / 4.0))
st.progress(progress_val)
if current_step <= 4:
    st.caption(f"Step {current_step} of 4")
else:
    st.caption("Step 4 of 4: Completed 🎯")


# Helper Function to get valid choices for remaining labs
def get_available_options(domain_filter=None, method_filters=None):
    valid_labs = LABS
    if domain_filter:
        valid_labs = [l for l in valid_labs if l['domain'] == domain_filter]
    
    if method_filters and len(method_filters) > 0:
        filtered = []
        for lab in valid_labs:
            # Check if lab matches at least one selected method
            if any(m in lab['methods'] for m in method_filters):
                filtered.append(lab)
        if len(filtered) > 0: # preserve if non-empty
            valid_labs = filtered

    methods = sorted(list(set(m for l in valid_labs for m in l['methods'])))
    topics = sorted(list(set(t for l in valid_labs for t in l['topics'])))
    models = sorted(list(set(m for l in valid_labs for m in l['models'])))
    clinical = sorted(list(set(c for l in valid_labs for c in l['clinical'])))
    
    return methods, topics, models, clinical


# --- STEP 1: DOMAIN ---
if st.session_state.step == 1:
    st.subheader("Step 1: Select your primary neuroscience domain")
    
    domains = [
        "Cognitive & Behavioral Neuroscience",
        "Systems & Circuit Neuroscience",
        "Computational Neuroscience & Neuro-AI",
        "Cellular, Molecular & Genetic Neuroscience"
    ]
    
    domain_choice = st.radio(
        "Choose your core scientific direction:",
        domains,
        help="This filters the wizard to laboratories specializing in this primary field."
    )
    
    if st.button("Next ➔", type="primary"):
        st.session_state.answers['domain'] = domain_choice
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: METHODOLOGY & TOOLKIT ---
elif st.session_state.step == 2:
    selected_domain = st.session_state.answers.get('domain', '')
    st.subheader(f"Step 2: Methodologies in {selected_domain}")
    st.write("Select the research tools or experimental/computational techniques you want to use:")
    
    available_methods, _, _, _ = get_available_options(domain_filter=selected_domain)
    
    selected_methods = st.multiselect(
        "Select 1 or more methodologies (showing only methods used by labs in this domain):",
        options=available_methods
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Next ➔", type="primary"):
            st.session_state.answers['methods'] = selected_methods
            st.session_state.step = 3
            st.rerun()

# --- STEP 3: SPECIFIC RESEARCH TOPICS ---
elif st.session_state.step == 3:
    selected_domain = st.session_state.answers.get('domain', '')
    selected_methods = st.session_state.answers.get('methods', [])
    
    st.subheader("Step 3: Specific Research Topics")
    st.write("Select specific questions or biological phenomena you are interested in investigating:")
    
    _, available_topics, _, _ = get_available_options(
        domain_filter=selected_domain, 
        method_filters=selected_methods
    )
    
    selected_topics = st.multiselect(
        "Select 1 to 3 research topics (dynamically filtered based on your previous selections):",
        options=available_topics
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Next ➔", type="primary"):
            st.session_state.answers['topics'] = selected_topics
            st.session_state.step = 4
            st.rerun()

# --- STEP 4: MODEL SYSTEM & CLINICAL FOCUS ---
elif st.session_state.step == 4:
    selected_domain = st.session_state.answers.get('domain', '')
    selected_methods = st.session_state.answers.get('methods', [])
    
    st.subheader("Step 4: Model System & Clinical/Disease Focus")
    
    _, _, available_models, available_clinical = get_available_options(
        domain_filter=selected_domain, 
        method_filters=selected_methods
    )
    
    col_a, col_b = st.columns(2)
    with col_a:
        model_pref = st.selectbox(
            "Preferred Model System:",
            ["No preference / Open to all"] + available_models
        )
    with col_b:
        clinical_pref = st.multiselect(
            "Clinical / Disease Focus (optional):",
            options=available_clinical
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
    st.write("Here are the Gonda Brain Research Center laboratories strictly matched to your preference combination:")
    
    ans = st.session_state.answers
    
    scored_labs = []
    for lab in LABS:
        score = 0
        reasons = []
        
        # 1. Domain Match (Required baseline)
        if lab['domain'] == ans.get('domain'):
            score += 35
            reasons.append(f"Domain match: **{lab['domain']}**")
        else:
            continue # Skip labs from other domains to avoid impossible/mismatched combinations
            
        # 2. Method match
        user_methods = ans.get('methods', [])
        matched_m = [m for m in lab['methods'] if m in user_methods]
        if matched_m:
            score += len(matched_m) * 15
            reasons.append(f"Matching methodology: {', '.join(matched_m)}")
            
        # 3. Topic match
        user_topics = ans.get('topics', [])
        matched_t = [t for t in lab['topics'] if t in user_topics]
        if matched_t:
            score += len(matched_t) * 15
            reasons.append(f"Matching research topic: {', '.join(matched_t)}")
            
        # 4. Model match
        user_model = ans.get('model', '')
        if user_model != "No preference / Open to all" and user_model in lab['models']:
            score += 10
            reasons.append(f"Model system: {user_model}")
            
        # 5. Clinical match
        user_clin = ans.get('clinical', [])
        matched_c = [c for c in lab['clinical'] if c in user_clin]
        if matched_c:
            score += len(matched_c) * 10
            reasons.append(f"Clinical focus: {', '.join(matched_c)}")
            
        # CORE FACULTY PRIORITY ENFORCEMENT (1.5x multiplier to always prioritize Core Faculty)
        if lab['status'] == 'Core Faculty':
            score *= 1.5
            
        scored_labs.append({
            "lab": lab,
            "score": round(score, 1),
            "reasons": list(dict.fromkeys(reasons)) # deduplicate preserving order
        })
        
    # Sort by score descending (Core faculty boosted to top)
    scored_labs.sort(key=lambda x: x['score'], reverse=True)
    
    if not scored_labs:
        st.warning("No laboratories matched all of your strict criteria. Try going back and broadening your selections!")
    else:
        for idx, item in enumerate(scored_labs[:6], 1):
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
                <p style="font-size: 0.9rem; margin-bottom: 4px;"><strong>🧪 Primary Methodologies:</strong> {', '.join(lab['methods'])}</p>
                <p style="font-size: 0.9rem; margin-bottom: 4px;"><strong>🐭 Model Systems:</strong> {', '.join(lab['models'])}</p>
                <p style="font-size: 0.88rem; color: #1F2937; margin-bottom: 0;"><strong>📚 Recent Work (2024–2026):</strong> {lab['pubs']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    if st.button("🔄 Start Over"):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()
