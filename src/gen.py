import torch
from copy import deepcopy

def scale(data):
    return torch.max(torch.tensor(0), torch.min(data, torch.tensor(1)))

def gen(model, init_vec, real_label, loss, notstart=True, num_examples=1, epsilon=1e-5):
    lr = 0.01
    iteration = 0; equal = 0
    data = []
    dim = (model.n_window)
    for restart in range(num_examples):
        init = deepcopy(init_vec)
        if not notstart:
            data.append(init); continue
        init.requires_grad = True
        copyz = 10; optimizer = torch.optim.AdamW([init] , lr=lr); zs = []
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
        for _ in range(1000):
            copy = deepcopy(init.data)
            res = model(init)
            z = loss(res, real_label)
            optimizer.zero_grad(); z.backward(); optimizer.step(); scheduler.step()
            init.data = scale(init.data)
            equal = equal + 1 if torch.all(abs(copy - init.data) < 1e-6) or (0 < copyz - z.item() < epsilon) else 0
            if equal > 30: break
            copyz = z.item()
            iteration += 1
        init.requires_grad = False
        data.append(init)
    return data


