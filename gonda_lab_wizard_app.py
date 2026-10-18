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
st.markdown('<div class="sub-title">Answer 4 quick questions to find the Bar-Ilan neuroscience labs that best match your research goals.</div>', unsafe_allow_html=True)

# Complete Gonda Labs Database
LABS = [
    # CORE FACULTY
    {
        "pi": "Prof. Izhar Bar-Gad",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Center Director)",
        "lab": "Neural Interfaces Laboratory / Basal Ganglia & Neuromodulation",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Basal Ganglia & Movement Disorders", "Deep Brain Stimulation (DBS)", "Tourette Syndrome & Motor Tics", "Closed-loop Neuromodulation"],
        "tools": ["Multi-electrode Extracellular Recording", "Closed-loop DBS Systems", "LFP Signal Processing", "Neural Network Computational Modeling"],
        "models": ["Rodents", "Primates", "Clinical DBS Cohorts"],
        "clinical": "Parkinson's, Tourette Syndrome, Movement Disorders",
        "summary": "Investigates cortico-striatal circuits and develops adaptive closed-loop DBS algorithms for movement and neuropsychiatric disorders.",
        "pubs": "Handbook of Clinical Neurology: Neuromodulation in Basal Ganglia Disorders (2026); Motor tics evoked by striatal disinhibition (Frontiers)."
    },
    {
        "pi": "Prof. Elana Zion-Golumbic",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Undergrad Program Head)",
        "lab": "Human Brain Dynamics and Real-Life Ecological Attention Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Auditory Attention & Speech Tracking", "Cocktail Party Effect", "ADHD & Auditory Distraction", "VR Ecological Environments"],
        "tools": ["High-density EEG", "Magnetoencephalography (MEG)", "In-school Mobile EEG", "Virtual Reality (VR Classroom/Café)", "Temporal Response Functions (TRF)"],
        "models": ["Humans"],
        "clinical": "ADHD, Neurodevelopmental Attention Disorders",
        "summary": "Studies dynamic speech tracking, selective attention in noisy environments, and auditory distraction using MEG, mobile EEG, and VR.",
        "pubs": "Toward precision EEG: assessing individual ERP reliability (Frontiers, 2026); Selective attention in Virtual Classroom (eLife, 2024)."
    },
    {
        "pi": "Prof. Dana Cohen",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Grad Advisor)",
        "lab": "Electrophysiology of Learning and Behavior Laboratory",
        "domain": "Computational Neuroscience & Neuro-AI",
        "subtopics": ["Deep Learning & Spike Classification", "Motor Skill Learning", "Cerebellar-Basal Ganglia Dynamics", "Population Coding"],
        "tools": ["Chronic Multi-channel Electrophysiology", "Deep Learning (CNNs / Transformers)", "Spike Sorting Pipelines", "Optical Cerebellar Imaging"],
        "models": ["Rodents", "Cross-species Datasets"],
        "clinical": "Motor Learning Deficits, Ataxia",
        "summary": "Uses deep neural networks (CNNs/Transformers) to classify electrophysiological neuronal cell types and investigates motor population dynamics.",
        "pubs": "A deep-learning strategy to identify cell types across species from high-density extracellular recordings (Nature Methods, 2024)."
    },
    {
        "pi": "Prof. Vadim Axelrod",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience and Consciousness Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Mind-Wandering & Spontaneous Thought", "Consciousness & Self-Awareness", "Face Perception", "Intracranial Decoding"],
        "tools": ["fMRI (MVPA)", "Human Intracranial EEG (iEEG/ECoG)", "Magnetoencephalography (MEG)", "Non-invasive tDCS/tACS Stimulation"],
        "models": ["Humans"],
        "clinical": "Neurosurgical Patient Cohorts, Psychiatric Disorders",
        "summary": "Combines human intracranial ECoG and machine learning decoding to map spontaneous thought dynamics, face perception, and meta-awareness.",
        "pubs": "Intracranial decoding of spontaneous thought (Cerebral Cortex, 2024-2025); tDCS modulation of spontaneous self-directed thoughts (PNAS)."
    },
    {
        "pi": "Prof. Moshe Bar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Cognitive Neuroscience Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Top-Down Predictive Brain", "Default Mode Network (DMN)", "Digital Therapeutics for Depression", "Curiosity & Thought Dynamics"],
        "tools": ["Combined fMRI / MEG", "Gamified Digital Apps (FTP)", "Top-Down Predictive Computational Models", "Remote AI Optical Speckle Analysis"],
        "models": ["Humans"],
        "clinical": "Clinical Depression, Anxiety, Mood Disorders",
        "summary": "Explores top-down predictive processing and develops digital health applications (Facilitating Thought Progression) for clinical depression.",
        "pubs": "Facilitating Thought Progression via a gamified app for depression (Behavior Therapy, 2026); Thought Dynamics and Mood Disorders (2026)."
    },
    {
        "pi": "Prof. Michal Ben-Shachar",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center (Interdisciplinary Unit Head)",
        "lab": "Neurobiology of Language and Reading Plasticity Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Language Development & Plasticity", "Dyslexia & Reading Pathways", "White Matter Tractography", "Stuttering Circuits"],
        "tools": ["Diffusion MRI (dMRI / DTI / HARDI)", "Automated Fiber Quantification (AFQ)", "Functional MRI (fMRI)", "Psycholinguistics"],
        "models": ["Humans"],
        "clinical": "Developmental Dyslexia, Persistent Stuttering, Preterm Infants",
        "summary": "Uses diffusion MRI tractography to examine white matter pathways (arcuate fasciculus) in reading, language acquisition, and developmental stuttering.",
        "pubs": "White matter correlates of sensorimotor synchronization in persistent developmental stuttering (J. Commun. Disord., 2025)."
    },
    {
        "pi": "Prof. Rafi Haddad",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Learning, Decision-Making, Olfaction & Neural Circuits Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Olfactory Neural Coding", "Piriform Cortex Micro-circuits", "Interhemispheric Synchronization", "Decision-Making Circuits"],
        "tools": ["Multi-channel Electrophysiology", "Optogenetics", "Viral Circuit Tracing (Rabies/AAV)", "Optical Odor Imaging"],
        "models": ["Rodents"],
        "clinical": "Olfactory & Sensory Processing Deficits",
        "summary": "Investigates interhemispheric synchronization and feedforward inhibitory micro-circuits in the primary olfactory cortex.",
        "pubs": "Bilateral odor coding and interhemispheric synchronization in piriform cortex (2024-2025)."
    },
    {
        "pi": "Prof. Hamutal Slovin",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Visual Processing and Artificial Vision Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Visual Population Dynamics", "Visual Prostheses & Brain-Machine Interfaces", "Image Reconstruction / Brain Reading", "Microsaccades & V1 Synchronization"],
        "tools": ["Wide-field Voltage-Sensitive Dye Imaging (VSDI)", "Multi-electrode Arrays", "Spiking Neural Networks (SNNs)", "Electrical Microstimulation"],
        "models": ["Primates", "Rodents"],
        "clinical": "Blindness Restoration, Visual Prostheses",
        "summary": "Uses VSDI optical imaging and neuromorphic spiking neural networks to study visual cortical dynamics and artificial vision prostheses.",
        "pubs": "Effects of Microsaccades in Primary Visual Cortex: Increased Synchronization in Fovea (J. Neurosci., 2025)."
    },
    {
        "pi": "Dr. David Zada",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Social Brain and Behavior Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Sleep & Single-Neuron DNA Repair", "Social Motion & Collective Behavior", "Transparent Animal Models", "Genetic Avatars"],
        "tools": ["Transparent Danionella cerebrum Glassfish", "In Vivo 2-Photon Whole-Brain Imaging", "Multi-animal Visual VR", "CRISPR & Single-cell RNA-seq"],
        "models": ["Danionella cerebrum Glassfish", "Zebrafish"],
        "clinical": "Neurodevelopmental Social Disorders, Aging, DNA Damage",
        "summary": "Maps whole-brain social circuits in transparent micro glassfish and investigates sleep-dependent chromosome dynamics and DNA repair.",
        "pubs": "Convergent thyroid-ATPase interactions regulate collective behavior in Danionella (Cell Reports, 2026)."
    },
    {
        "pi": "Prof. Adam Zaidel",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Multisensory Processing Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Multisensory Integration (Visual/Vestibular/Auditory)", "Spatial Orientation & Self-Motion", "Bayesian Optimal Decision Modeling", "Sensory Recalibration"],
        "tools": ["3D MOOG Multisensory Motion Simulator", "Single-unit Primate Electrophysiology", "Bayesian Computational Modeling", "Human Psychophysics"],
        "models": ["Humans", "Primates", "Rodents"],
        "clinical": "Parkinson's Disease, Autism Spectrum Disorder (Sensory Processing)",
        "summary": "Combines Israel's 3D MOOG motion simulator with single-unit electrophysiology and Bayesian modeling to study multisensory orientation.",
        "pubs": "Contrary neuronal recalibration in different multisensory cortical areas (eLife)."
    },
    {
        "pi": "Prof. Ari Zivotofsky",
        "status": "Core Faculty",
        "dept": "Gonda Brain Research Center",
        "lab": "Ocular Motor and Visual Perception Laboratory",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Oculomotor Control & Saccades", "Eye-Tracking Biomarkers for Neurodegeneration", "Unintentional Gait Synchronization", "Neuro-ethics"],
        "tools": ["High-speed Video-Oculography", "Eye-Tracking Systems", "Visual Psychophysics", "Gait Synchronization Analysis"],
        "models": ["Humans"],
        "clinical": "Motor Neurone Disease, Early Alzheimer's / Parkinson's Detection",
        "summary": "Develops non-invasive video-oculography eye-tracking biomarkers for early detection of neurodegenerative and motor neurone diseases.",
        "pubs": "Oculomotor atypicalities in motor neurone disease: a systematic review (Frontiers in Neuroscience, 2024)."
    },
    # KEY AFFILIATED LABS
    {
        "pi": "Prof. Alon Korngreen",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Cellular Neurophysiology Laboratory",
        "domain": "Systems & Circuit Neuroscience",
        "subtopics": ["Subthalamic Nucleus & Globus Pallidus Biophysics", "Ion Channel Kinetics", "Basal Ganglia Micro-circuits"],
        "tools": ["Whole-cell Patch-clamp Electrophysiology", "2-Photon Calcium Imaging", "Hodgkin-Huxley Modeling", "Optogenetics"],
        "models": ["Rodents"],
        "clinical": "Parkinson's Disease",
        "summary": "Investigates cellular biophysics and synaptic plasticity of basal ganglia micro-circuits using patch-clamp and computational modeling.",
        "pubs": "Long-term plasticity of glutamatergic inputs in basal ganglia; Biophysics of Subthalamic Nucleus."
    },
    {
        "pi": "Prof. Lior Appelbaum",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Molecular & Developmental Neuroscience Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Sleep Regulation & Synaptic Plasticity", "Chromosome Dynamics & DNA Repair", "Neurodevelopmental Genetics"],
        "tools": ["Transgenic Zebrafish", "3D Live Confocal / 2-Photon Imaging", "High-throughput Sleep Tracking", "CRISPR"],
        "models": ["Zebrafish"],
        "clinical": "MCT8 Deficiency, Neurodevelopmental Disorders",
        "summary": "Uses transgenic zebrafish to study genetic and cellular regulation of sleep, chromosome dynamics, and synaptic maintenance.",
        "pubs": "Parp1 promotes sleep, which enhances DNA repair in neurons (Molecular Cell)."
    },
    {
        "pi": "Prof. Eitan Okun",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Neurodevelopment & Neurodegeneration Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Microglial Neuroinflammation", "Alzheimer's Disease Pathogenesis", "Toll-like Receptors (TLRs)", "Exercise Neuroprotection"],
        "tools": ["Transgenic Alzheimer's Mouse Models", "Immunohistochemistry", "Microglial Morphology Analysis", "Behavioral Mazes"],
        "models": ["Rodents"],
        "clinical": "Alzheimer's Disease, Down Syndrome",
        "summary": "Studies microglial neuroinflammation, TLR pathways, and exercise-induced neurogenesis in Alzheimer's disease models.",
        "pubs": "TLR pathways mediating neuroinflammation in cognitive decline; Exercise-induced neurogenesis."
    },
    {
        "pi": "Dr. Shahar Alon",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Engineering",
        "lab": "Spatial Genomics Group",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["Spatial Transcriptomics", "Expansion Microscopy (ExM)", "In Situ RNA Sequencing", "RNA Editing"],
        "tools": ["Expansion Sequencing (ExSeq)", "High-throughput Fluorescence Microscopy", "Single-cell Spatial Algorithms"],
        "models": ["Mammals", "Cephalopods"],
        "clinical": "Neurodegenerative Transcriptomics",
        "summary": "Develops expansion sequencing and spatial transcriptomics to map nanoscale gene expression in neural circuits.",
        "pubs": "Trade-off between transcriptome plasticity and genome evolution (Cell); Spatial transcriptomics in neural tissue."
    },
    {
        "pi": "Prof. Gal Yadid",
        "status": "Affiliated Faculty",
        "dept": "Faculty of Life Sciences",
        "lab": "Neuropsychopharmacology Laboratory",
        "domain": "Cellular, Molecular & Genetic Neuroscience",
        "subtopics": ["PTSD & Traumatic Memory Erasure", "Addiction Memory Remodeling", "Nanoparticle BBB Drug Delivery"],
        "tools": ["Targeted Bio-nanoparticles", "In Vivo Microdialysis", "Operant Self-Administration", "Deep Brain Electrical Stimulation"],
        "models": ["Rodents"],
        "clinical": "Post-Traumatic Stress Disorder (PTSD), Substance Addiction",
        "summary": "Develops targeted nanoparticle drug delivery across the blood-brain barrier for PTSD memory erasure and addiction treatment.",
        "pubs": "Targeted nanoparticle delivery across the blood-brain barrier for PTSD treatment."
    },
    {
        "pi": "Prof. Avi Goldstein",
        "status": "Affiliated Faculty",
        "dept": "Department of Psychology",
        "lab": "Electromagnetic Brain Imaging Unit",
        "domain": "Cognitive & Behavioral Neuroscience",
        "subtopics": ["Executive Control Oscillations", "MEG Signal Processing", "Language Processing in Autism"],
        "tools": ["248-channel Whole-head MEG", "High-density EEG", "Source Localization Algorithms"],
        "models": ["Humans"],
        "clinical": "Autism Spectrum Disorder, Cognitive Impairments",
        "summary": "Operates the 248-channel MEG system investigating neural oscillations during executive control and language perception.",
        "pubs": "MEG neural dynamics of cognitive control and executive functioning."
    },
    {
        "pi": "Prof. Ido Kanter",
        "status": "Affiliated Faculty",
        "dept": "Department of Physics",
        "lab": "Complex Systems and Computational Neuroscience Laboratory",
        "domain": "Computational Neuroscience & Neuro-AI",
        "subtopics": ["Ultrafast Biological Learning Rules", "Dendritic Computing Beyond Backprop", "Physics-Inspired Neural Networks"],
        "tools": ["Biophysical Neural Simulations", "Non-linear Dynamics", "Mathematical Network Modeling"],
        "models": ["Computational Models", "In Vitro Neuronal Cultures"],
        "clinical": "AI Architecture Optimization, Epilepsy Dynamics",
        "summary": "Discovers ultrafast biological learning rules in individual dendrites that inspire non-backprop artificial intelligence.",
        "pubs": "Dendritic learning rules outperforming traditional deep neural network training."
    }
]

# Initialize Session State for Wizard Steps
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Progress Bar
progress = (st.session_state.step - 1) / 3.0
st.progress(progress)
st.caption(f"Step {st.session_state.step} of 4")

# --- STEP 1: DOMAIN ---
if st.session_state.step == 1:
    st.subheader("Step 1: Which broad neuroscience domain excites you most?")
    domain_choice = st.radio(
        "Select one primary field:",
        [
            "Cognitive & Behavioral Neuroscience (Human cognition, attention, speech, language, memory, consciousness)",
            "Systems & Circuit Neuroscience (Neural circuits, sensory processing, motor control, basal ganglia, visual/olfactory systems)",
            "Computational Neuroscience & Neuro-AI (Deep learning, neural network modeling, spike sorting, mathematical neuroscience)",
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
    selected_domain = st.session_state.answers['domain']
    st.subheader(f"Step 2: What specific topics within {selected_domain} interest you?")
    
    # Dynamic options based on domain
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
            "Deep Learning & Transformers for Neural Waveform Classification",
            "Neuromorphic Spiking Neural Networks (SNNs) for Visual Processing",
            "Bayesian Optimal Decision Modeling & Sensory Recalibration",
            "Ultrafast Biological Learning Rules & Dendritic Computing",
            "Computational Neural Network Simulations of Basal Ganglia Circuits"
        ]
    else: # Cellular/Molecular
        topic_options = [
            "Sleep-dependent Chromosome Dynamics & Single-Neuron DNA Repair",
            "Microglial Neuroinflammation & Alzheimer's Pathogenesis",
            "Spatial Transcriptomics, Expansion Microscopy & In Situ Sequencing",
            "Social Behavior Circuits & Collective Motion in Transparent Fish",
            "Targeted Bio-nanoparticle BBB Drug Delivery for PTSD & Memory Erasure",
            "Microbiome-Gut-Brain Axis & Microfluidic Organs-on-a-Chip"
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
            for lab_sub in lab.get('subtopics', []):
                if any(k.lower() in lab_sub.lower() for k in user_sub.split()):
                    score += 15
                    reasons.append(f"Matching topic: {lab_sub}")
                    break
                    
        # Tool match
        for user_tool in ans.get('tools', []):
            for lab_tool in lab.get('tools', []):
                if any(k.lower() in lab_tool.lower() for k in user_tool.split()):
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
            if any(k.lower() in lab.get('clinical', '').lower() for k in user_clin.split()):
                score += 10
                reasons.append(f"Clinical focus: {user_clin}")
                break
                
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
            <p style="font-size: 0.88rem; color: #1F2937; margin-bottom: 0;"><strong>📚 Recent Work (2024–2026):</strong> {lab['pubs']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    if st.button("🔄 Start Over"):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()
