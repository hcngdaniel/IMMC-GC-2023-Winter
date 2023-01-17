#!/usr/bin/env python3
import torch
from torch import nn
import torch.nn.functional
import torch.optim
from torch.utils.tensorboard import SummaryWriter


lr = 1
start_epoch = 1
end_epoch = 1000
restart = True

if restart:
    w = torch.zeros((8, 23), dtype=torch.float32, requires_grad=True)
else:
    w = torch.load("weights.pth")

optim = torch.optim.SGD(params=[w], lr=lr)

data = torch.load("dataset.pth")
label = torch.load("label.pth")

writer = SummaryWriter(
    log_dir='logs'
)

for epoch in range(start_epoch, end_epoch + 1):
    h = torch.zeros(label.size(0), 8)
    for i in range(len(data)):
        for j in range(8):
            h[i][j] = torch.dot(nn.functional.softmax(w[j], 0), data[i][j])
    loss = nn.functional.mse_loss(h, label)
    optim.zero_grad()
    loss.backward()
    optim.step()
    print(f"epoch {epoch}: {loss.detach().numpy():.8f}")
    writer.add_scalar(
        "loss",
        loss.detach().numpy(),
        epoch
    )

print(w)
torch.save(w, "weights.pth")
