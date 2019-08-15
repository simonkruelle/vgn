import torch
import torch.nn as nn
import torch.nn.functional as F


def get_model(name):
    name = name.lower()
    if name == 'small_conv':
        return SmallConv()


class SmallConv(nn.Module):
    def __init__(self):
        super(SmallConv, self).__init__()
        self.conv1 = nn.Conv3d(1, 16, 7, padding=3)
        self.conv2 = nn.Conv3d(16, 32, 5, padding=2)

        self.conv_score_out = nn.Conv3d(32, 1, 3, padding=1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))

        score_out = torch.sigmoid(self.conv_score_out(x))

        return score_out


if __name__ == '__main__':
    device = torch.device('cuda')
    model = get_model('conv_small').to(device)
    trace = torch.randn(32, 1, 60, 60, 60).to(device)
    out = model(trace)

    assert out.shape[0] == trace.shape[0], 'batch size is not the same'
    assert out.shape[1] == 1, 'number of output channels is wrong'
    assert out.shape[2:] == trace.shape[2:], 'voxel dimensions are wrong'

    raw_input('Press any key to continue')