from enum import Enum
import os


def get_content(element: str, md_dir: str) -> str:
    return open(f"{os.getenv('APP_PATH')}/elements/{md_dir}/{element}.md").read()


class Default(Enum):
    ICON_PACK = "simple-icons"


class Languages(Enum):
    TITLE = "Lenguajes"
    MD_PATH = "langs"
    ITEMS = {
        "python": {
            "title": "Python",
            "content": get_content("python", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:python",
        },
        "javascript": {
            "title": "JavaScript",
            "content": get_content("javascript", MD_PATH),
            "icon": "material-symbols:javascript",
        },
        "csharp": {
            "title": "C#",
            "content": get_content("csharp", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:csharp",
        },
        "java": {
            "title": "Java",
            "content": get_content("java", MD_PATH),
            "icon": "ri:java-line",
        },
        "html": {
            "title": "HTML",
            "content": get_content("html", MD_PATH),
            "icon": "akar-icons:html-fill",
        },
        "cplusplus": {
            "title": "C++",
            "content": get_content("cplusplus", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:cplusplus",
        },
        "typescript": {
            "title": "TypeScript",
            "content": get_content("typescript", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:typescript",
        },
        "go": {
            "title": "Go",
            "content": get_content("go", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:go",
        },
        "c": {
            "title": "C",
            "content": get_content("c", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:c",
        },
        "rust": {
            "title": "Rust",
            "content": get_content("rust", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:rust",
        },
        "ruby": {
            "title": "Ruby",
            "content": get_content("ruby", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:ruby",
        },
        "php": {
            "title": "PHP",
            "content": get_content("php", MD_PATH),
            "icon": "devicon-plain:php",
        },
        "dart": {
            "title": "Dart",
            "content": get_content("dart", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:dart",
        },
        "kotlin": {
            "title": "Kotlin",
            "content": get_content("kotlin", MD_PATH),
            "icon": "cib:kotlin",
        },
        "swift": {
            "title": "Swift",
            "content": get_content("swift", MD_PATH),
            "icon": f"{Default.ICON_PACK.value}:swift",
        },
    }


class DevOps(Enum):
    TITLE = "DevOps"
    MD_DIR = "devops"
    ITEMS = {
        "git": {
            "title": "Git",
            "content": get_content("git", MD_DIR),
            "icon": f"{Default.ICON_PACK.value}:git",
        },
        "docker": {
            "title": "Docker",
            "content": get_content("docker", MD_DIR),
            "icon": f"{Default.ICON_PACK.value}:docker",
        },
        "kubernetes": {
            "title": "Kubernetes",
            "content": get_content("kubernetes", MD_DIR),
            "icon": f"{Default.ICON_PACK.value}:kubernetes",
        },
        "ci-cd": {
            "title": "CI/CD",
            "content": get_content("ci-cd", MD_DIR),
            "icon": "clarity:ci-cd-line",
        },
        "bash": {
            "title": "Bash",
            "content": get_content("bash", MD_DIR),
            "icon": "devicon-plain:bash",
        },
        "powershell": {
            "title": "PowerShell",
            "content": get_content("powershell", MD_DIR),
            "icon": f"{Default.ICON_PACK.value}:powershell",
        },
    }
