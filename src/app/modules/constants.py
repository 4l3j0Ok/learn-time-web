from enum import Enum
import os


def get_content(technology: str, md_dir: str) -> str:
    return open(f"{os.getenv('APP_PATH')}/technologies/{md_dir}/{technology}.md").read()


class App(Enum):
    name = "Learn Time"
    author = "Alejo Sarmiento"
    version = "v1"
    url = os.getenv("APP_URL", "https://learn.alejoide.com")


class Default(Enum):
    icon_pack = "simple-icons"


class Languages(Enum):
    title = "Lenguajes"
    md_path = "langs"
    items = {
        "python": {
            "title": "Python",
            "content": get_content("python", md_path),
            "icon": f"{Default.icon_pack.value}:python",
        },
        "javascript": {
            "title": "JavaScript",
            "content": get_content("javascript", md_path),
            "icon": "material-symbols:javascript",
        },
        "csharp": {
            "title": "C#",
            "content": get_content("csharp", md_path),
            "icon": f"{Default.icon_pack.value}:csharp",
        },
        "java": {
            "title": "Java",
            "content": get_content("java", md_path),
            "icon": "ri:java-line",
        },
        "html": {
            "title": "HTML",
            "content": get_content("html", md_path),
            "icon": "akar-icons:html-fill",
        },
        "cplusplus": {
            "title": "C++",
            "content": get_content("cplusplus", md_path),
            "icon": f"{Default.icon_pack.value}:cplusplus",
        },
        "typescript": {
            "title": "TypeScript",
            "content": get_content("typescript", md_path),
            "icon": f"{Default.icon_pack.value}:typescript",
        },
        "go": {
            "title": "Go",
            "content": get_content("go", md_path),
            "icon": f"{Default.icon_pack.value}:go",
        },
        "c": {
            "title": "C",
            "content": get_content("c", md_path),
            "icon": f"{Default.icon_pack.value}:c",
        },
        "rust": {
            "title": "Rust",
            "content": get_content("rust", md_path),
            "icon": f"{Default.icon_pack.value}:rust",
        },
        "ruby": {
            "title": "Ruby",
            "content": get_content("ruby", md_path),
            "icon": f"{Default.icon_pack.value}:ruby",
        },
        "php": {
            "title": "PHP",
            "content": get_content("php", md_path),
            "icon": "devicon-plain:php",
        },
        "dart": {
            "title": "Dart",
            "content": get_content("dart", md_path),
            "icon": f"{Default.icon_pack.value}:dart",
        },
        "kotlin": {
            "title": "Kotlin",
            "content": get_content("kotlin", md_path),
            "icon": "cib:kotlin",
        },
        "swift": {
            "title": "Swift",
            "content": get_content("swift", md_path),
            "icon": f"{Default.icon_pack.value}:swift",
        },
    }


class DevOps(Enum):
    title = "Infraestructura y DevOps"
    md_dir = "devops"
    items = {
        "git": {
            "title": "Git",
            "content": get_content("git", md_dir),
            "icon": f"{Default.icon_pack.value}:git",
        },
        "docker": {
            "title": "Docker",
            "content": get_content("docker", md_dir),
            "icon": f"{Default.icon_pack.value}:docker",
        },
        "kubernetes": {
            "title": "Kubernetes",
            "content": get_content("kubernetes", md_dir),
            "icon": f"{Default.icon_pack.value}:kubernetes",
        },
        "ci-cd": {
            "title": "CI/CD",
            "content": get_content("ci-cd", md_dir),
            "icon": "clarity:ci-cd-line",
        },
        "bash": {
            "title": "Bash",
            "content": get_content("bash", md_dir),
            "icon": "devicon-plain:bash",
        },
        "powershell": {
            "title": "PowerShell",
            "content": get_content("powershell", md_dir),
            "icon": f"{Default.icon_pack.value}:powershell",
        },
    }
