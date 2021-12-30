# Create a cnot gate with the bits in position 01
qc = QuantumCircuit(2,2)
qc.x(0)
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
qc.draw()

# Observe output of the circuit designed above
sim = Aer.get_backend('aer_simulator') 
result = sim.run(qc_encode).result()
counts = result.get_counts()
plot_histogram(counts)

# 2-input half adder
qc_ha = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc_ha.x(0) # For a=0, remove this line. For a=1, leave it.
qc_ha.x(1) # For b=0, remove this line. For b=1, leave it.
qc_ha.barrier()
# use cnots to write the XOR of the inputs on qubit 2
qc_ha.cx(0,2)
qc_ha.cx(1,2)
# use ccx to write the AND of the inputs on qubit 3
qc_ha.ccx(0,1,3)
qc_ha.barrier()
# extract outputs
qc_ha.measure(2,0) # extract XOR value
qc_ha.measure(3,1)

qc_ha.draw()

# 3-input half adder
qc_ha_3 = QuantumCircuit(5,2)
# encode inputs in qubits 0 and 1
qc_ha_3.barrier()
# use cnots to write the XOR of the inputs on qubit 3
qc_ha_3.cx(0,3)
qc_ha_3.cx(1,3)
qc_ha_3.cx(2,3)
# use ccx to write the AND of the inputs on qubit 3
qc_ha_3.ccx(0,1,4)
qc_ha_3.ccx(0,2,4)
qc_ha_3.ccx(1,2,4)
qc_ha_3.barrier()
# extract outputs
qc_ha_3.measure(3,0) # extract XOR value
qc_ha_3.measure(4,1)

qc_ha_3.draw()

# Initializing qubit to a state other than zero. |0> state is represented by a vector [1,0] and |1> by [0,1]
qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc.draw()  # Let's view our circuit

# Either of a save operation on state vectors or a measurement on the qubit can enable us to fetch state of qubits
# Save vector operation doesn't alter the superposition of qubit while measurement collapses the superposition of qubit 
# and bring it to either of the possible classical states
# Through save vector as below
qc.save_statevector()   # Tell simulator to save statevector
qobj = assemble(qc)     # Create a Qobj from the circuit for the simulator to run
result = sim.run(qobj).result() # Do the simulation and return the result
out_state = result.get_statevector()
print(out_state) # Display the output state vector

# Through measurement as below
qc.measure_all()
qc.draw()
qobj = assemble(qc)
result = sim.run(qobj).result()
out_state = result.get_statevector()
print(out_state) # Display the output state vector

# Qubit state can be plotted in the bloch sphere using the spherical co-ordinates as below
from qiskit_textbook.widgets import plot_bloch_vector_spherical
coords = [pi/2,3*pi/2,1] # [Theta, Phi, Radius]
plot_bloch_vector_spherical(coords) # Bloch Vector with spherical coordinates

# From the circuit, the same can be passed through as the statevector as below
# Let's see the result
qc.save_statevector()
qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
plot_bloch_multivector(state)
