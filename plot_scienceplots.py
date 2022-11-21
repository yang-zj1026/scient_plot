import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'bright'])

x = [i for i in range(6)]
x_labels = [8, 16, 32, 48, 64, 128]
y1 = [0.02, 0.28, 0.36, 0.61, 0.62, 0.86]
y2 = [0.02, 0.09, 0.90, 2.43, 5.36, 8.63]
y3 = [0.00, 0.08, 0.16, 0.23, 0.29, 1.37]

pparam = dict(xlabel='Num. of agents', ylabel=r'Num. of collisions')
fig, ax = plt.subplots()

ax.plot(x, y1, '-^', markersize=2.5, label='From scratch')
plt.plot(x, y2, '--*', markersize=4, label='Pretrained')
ax.plot(x, y3, '-o', lw=1, markersize=2, label='Pretrained + finetune')

ax.set_xticks(x, x_labels, size='small')
ax.legend(title='')
ax.set_ylim(bottom=0, top=1.5)
# ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/collisions_all.pdf')
fig.savefig('figures/collisions_all.jpg', dpi=300)
