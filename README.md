# qchack_team37
QCHack 2021 Team 37: Discord name: Wabinab#2774, Rupayan CsMP#2520, NobodySpecial#1874, Rahul Bhardwaj(he/him)#8579, Simran jakhodia#4891. 

## IBM Creative Challenge
Note that we do not have a single project but multiple small project to discuss the interference. This is because we don't think there is a particular single idea to discuss about interference and different people might be able to grasp the concept differently hence offers different approaches to the idea. 

The first is the MainWabinab.ipynb file which contains using Bernstein Vazirani algorithm for demonstration and how addition of noises could affect the readout to collapse (i.e. constructively interfere) on a different channel (i.e. different bit string) than the expected channel. 

The second is QKD_Wabinab.ipynb which contains information of implementing Quantum Key Distribution algorithm and how the addition of "virus" (noises) with a large enough rotational phase could affect the actual key even without measuring, and the idea that small phase change could go unnoticed (which could be treated as a virus package), or even with large phase change might change a harmless strings of bits into one harmful to a (classical/quantum) computer **after** measurement (without measuring it takes no effect). However these ideas are very vague and may or may not prove useful or perhaps even directing in the wrong direction, and without proper research nothing could be confirmed. 

The third is Artistic_Wabinab.ipynb, containing demonstration of interference from the artistic point of view, by stacking repetitive gates of H, S, T, Sdg and Tdg in a certain order such to see how they interfere with each other when increasing their repetition count. We demonstrated some repetition count constructively interfere to a single value while others have several child interference at lower values and a main interference bit string value. And some repetition gives destructive interference and they gradually decrease to become balance (all probability approaches equal probability for all available bit strings, balanced). 

The fourth is Rupayan_useful_algo.ipynb. @Rupayan CsMP demonstrated a useful usage of interference from the mathematical point of view and how given a probability distribution we could implement this probability distribution we wanted on the quantum computer. For this point due to time constraint and for simplicity we would apply to 1-qubit problem, which could be expanded to multi-qubit problem as well (not discussed). 

In the **helper** folder contains the helper file in .py format which is imported into the .ipynb files when required to use their function. 

In the **result** folder contains the job run on IBM Quantum devices (both on ibmq_quito 5-qubit Falcon r4 type processor 16 Quantum Volume device), which could be retrieved from their respective folder. Artistic folder is for Artistic_Wabinab.ipynb's run, and Rupayan for Rupayan_useful_algo.ipynb's run. 
