import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def gerar_tomografia_completa(n_pontos=8, velocidades=None, seed=None):
    """
    Gera duas figuras lado a lado para tomografia acústica de troncos de árvore:
    - Caminhos entre sensores com cores baseadas na velocidade
    - Heatmap interpolado do tronco mostrando regiões de maior e menor velocidade
    Os sensores são numerados na figura da esquerda.
    """
    if seed is not None:
        np.random.seed(seed)

    # Sensores distribuídos uniformemente em círculo
    theta = np.linspace(0, 2*np.pi, n_pontos, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    # Se não houver matriz de velocidades fornecida, gerar aleatória
    if velocidades is None:
        velocidades = np.random.uniform(800, 2000, size=(n_pontos, n_pontos))
    
    # Garantir simetria
    for i in range(n_pontos):
        for j in range(i+1, n_pontos):
            if velocidades[i, j] == 0:
                velocidades[i, j] = velocidades[j, i] = 1500

    # Criar figura lado a lado
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # ---------------------------
    # 1) Caminhos entre sensores
    # ---------------------------
    axs[0].set_aspect("equal")
    axs[0].scatter(x, y, color="black", zorder=5)

    # Numerar sensores
    for idx, (xi, yi) in enumerate(zip(x, y)):
        axs[0].text(xi*1.05, yi*1.05, str(idx), fontsize=12, ha="center", va="center", fontweight="bold")

    # Desenhar caminhos coloridos
    for i in range(n_pontos):
        for j in range(i+1, n_pontos):
            v = velocidades[i, j]
            axs[0].plot([x[i], x[j]], [y[i], y[j]],
                        color=plt.cm.plasma_r((v-800)/1200), alpha=0.7)

    axs[0].set_title("Caminhos entre sensores")
    axs[0].axis("off")

    # ---------------------------
    # 2) Interpolação tomográfica
    # ---------------------------
    grid_x, grid_y = np.mgrid[-1:1:200j, -1:1:200j]

    # Para interpolação, usar velocidades médias associadas aos sensores
    vel_sensores = np.mean(velocidades, axis=1)

    # Interpolação
    grid_vel = griddata((x, y), vel_sensores, (grid_x, grid_y), method="cubic")

    # Limitar região ao círculo do tronco
    mask = grid_x**2 + grid_y**2 > 1
    grid_vel[mask] = np.nan

    # Plotar heatmap
    im = axs[1].imshow(grid_vel.T, extent=(-1, 1, -1, 1),
                       origin="lower", cmap="plasma_r")
    circle = plt.Circle((0, 0), 1, color="black", fill=False)
    axs[1].add_artist(circle)
    axs[1].set_aspect("equal")
    axs[1].set_title("Interpolação de velocidades")
    axs[1].axis("off")
    fig.colorbar(im, ax=axs[1], shrink=0.7, label="Velocidade (m/s)")

    plt.tight_layout()
    return fig
