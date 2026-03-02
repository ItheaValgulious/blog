---
title: How to use GPU in WSL2
tags:
  - programming
  - tips
date: 2025-12-09 14:30:07
---


# How to use GPU in WSL2

Write this in `.bashrc`

```bash
export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
export MESA_LOADER_DRIVER_OVERRIDE=d3d12
export GALLIUM_DRIVER=d3d12
```

And test by

```
glxinfo -B
```

to see if there is `DEVICE` is `llvm` or `d3d12`

And this may only work for vulkan rather than opengl.

Vegetable WSL!