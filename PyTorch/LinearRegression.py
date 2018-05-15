import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt


# Hyper-parameters
input_size = 1
output_size = 1
num_epochs = 600
learning_rate = 0.00001


filename = "/home/atas/data.txt"

x_train = np.loadtxt(filename,skiprows=0)[:,0]
x_train = np.asarray(x_train, dtype=np.float32).reshape(-1,1)


x_train =  np.reshape(x_train,(-1,1))



y_train = np.loadtxt(filename,skiprows=0)[:,1]
y_train = np.asarray(y_train, dtype=np.float32).reshape(-1,1)
y_train =  np.reshape(y_train,(-1,1))

print(x_train, y_train)


model = nn.Linear(input_size, output_size)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  

# Train the model
for epoch in range(num_epochs):
    # Convert numpy arrays to torch tensors
    inputs = torch.from_numpy(x_train)
    targets = torch.from_numpy(y_train)

    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 5 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# Plot the graph
predicted = model(torch.from_numpy(x_train)).detach().numpy()
plt.plot(x_train, y_train, 'ro', label='Original data')
plt.plot(x_train, predicted, label='Fitted line')
plt.legend()
plt.show()
plt.xlabel('Reading(microV)')
plt.ylabel('Pressure(mmHg)')
# Save the model checkpoint
torch.save(model.state_dict(), 'model.ckpt')

































