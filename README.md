<div align="center">
<img src="https://raw.githubusercontent.com/YZUCAM/SLM_control/main/docsrc/SLM_ui_example.png"><br><br>
</div>


# Spatial Light Modulator Control
Update phase hologram pattern to arbitrary position of SLM.

In optical neural network (ONN), most of case the light need to be modulated for later matrix vector multiplication. However, the hologram phase pattern is intensively used in the ONN. SLM is the device to generate the desire phase pattern. So upload the phase pattern into particular location on SLM is required. This script gives a visulized procedure for user to upload the phase pattern into SLM and display it in the device.

## Installation
pip install pyqt5<br>

## How to use
The main program is slm_control_main.py. Directly run the program.<br>
The slm_control.py is the customerized python script for Meadowlard Spatial Light Modulator.

The program can support maximum 2 SLM working in parallel.
