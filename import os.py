import os

folders = [
    "core",
    "planet/terrain",
    "planet/climate",
    "planet/hydrology",
    "planet/atmosphere",
    "biosphere/biomes",
    "biosphere/foodweb",
    "biosphere/evolution",
    "civilization/society",
    "civilization/economy",
    "civilization/warfare",
    "civilization/culture",
    "data/assets",
    "data/world_seeds",
    "data/mods",
    "renderer/map3d",
    "renderer/ui",
    "renderer/debug_overlay",
    "interface",
    "tests"
]

files = {
    "main.py": "",
    "README.md": "# Procedural Universe Engine\n\nSimulation of planet, ecosystem, and civilization dynamics.",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n.vscode/\n.idea/\nbuild/\ndist/",
    "data/serialization.py": "# Handles data loading/saving logic.",
    "interface/scenario_runner.py": "# CLI scenario runner.",
    "interface/monitoring_tools.py": "# Tools for dev metrics and debugging.",
    "core/clock.py": "# Global simulation clock.",
    "core/graph_manager.py": "# Dependency-based update graph.",
    "core/state_manager.py": "# Save/load simulation state."
}

# Create folders and add __init__.py
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    init_path = os.path.join(folder, "__init__.py")
    open(init_path, "a").close()

# Create top-level files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Folder structure generated.")
