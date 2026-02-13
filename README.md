# Real-Time Co-Simulation Framework for Smart Grid Resilience
## Integrating AI, MATLAB/Simulink, and DIgSILENT PowerFactory for EV & Hydrogen Systems

### 📌 Project Overview
As power systems transition toward carbon neutrality, the stochastic nature of **Electric Vehicle (EV)** loads poses significant stability challenges. This project develops a high-performance **real-time co-simulation environment** to synchronize AI-driven decision-making with physical grid constraints, utilizing **Hydrogen Fuel Cells (HFC)** as dynamic buffers.

### 🚀 Technical Architecture & Integration
The framework establishes a tri-platform synchronization pipeline to handle complex grid dynamics:
* **Analytical Layer (Python/AI)**: Executes deep learning models for millisecond-level demand forecasting and adaptive control logic.
* **Control Layer (MATLAB/Simulink)**: Models high-fidelity **Hydrogen Fuel Cell** dynamics and power electronic interfaces for rapid frequency/voltage support.
* **Physical Simulation Layer (DIgSILENT PowerFactory)**: Validates system-wide impact through continuous, quasi-dynamic load flow analysis via the **Python-PowerFactory API**.

### 🛠 Core Engineering & Real-Time Capabilities
* **Dynamic Congestion Management**: Implemented a real-time "Smart Charging" coordinator that modulates EV charging rates based on instantaneous transformer thermal limits.
* **Hybrid Energy Buffering**: Engineered a logic-gate system where HFCs act as a real-time buffer to shave peak loads during transient spikes in EV demand.
* **Automated Data Pipeline**: Developed custom Python scripts to poll grid states every 1-5 seconds, ensuring the AI model operates on fresh, real-time telemetry.

### 📈 Technical Stack
* **Simulation**: DIgSILENT PowerFactory, MATLAB/Simulink.
* **AI/Programming**: Python (TensorFlow, API Integration), MATLAB Engine API.
* **Methodology**: Real-time steady-state stability, Voltage Profile Optimization.

---
**Lead Researcher: Le Dinh Quyen** | GPA: 3.78/4.0
*Faculty of Electrical Engineering, University of Science and Technology - UD*
